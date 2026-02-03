#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown Blog Post Validator
============================

This tool validates markdown files for Hexo blog format requirements.
It checks for special characters, format issues, and common problems.

Usage:
    python md-validator.py [options] <file_or_directory>

Options:
    --fix           Attempt to fix some issues automatically
    --strict        Enable strict mode (more warnings)
    --output        Output format: text, json, or markdown
    --ignore        Comma-separated list of rules to ignore

Author: Amber Moe
License: MIT
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class Issue:
    """Represents a validation issue."""
    file: str
    line: int
    column: int
    rule: str
    severity: Severity
    message: str
    suggestion: Optional[str] = None


class MarkdownValidator:
    """Validates markdown files for Hexo blog format."""

    # Special characters that might cause issues
    PROBLEMATIC_CHARS = {
        '\u200b': 'Zero-width space',
        '\u200c': 'Zero-width non-joiner',
        '\u200d': 'Zero-width joiner',
        '\u2028': 'Line separator',
        '\u2029': 'Paragraph separator',
        '\ufeff': 'Byte order mark',
        '\u00a0': 'Non-breaking space',
        '\u3000': 'Ideographic space',
    }

    # Smart quotes that should be converted
    SMART_QUOTES = {
        '"': '"',  # Left double quote
        '"': '"',  # Right double quote
        ''': "'",  # Left single quote
        ''': "'",  # Right single quote
        '「': '"',  # Japanese left corner bracket
        '」': '"',  # Japanese right corner bracket
        '『': '"',  # Japanese left white corner bracket
        '』': '"',  # Japanese right white corner bracket
    }

    def __init__(self, strict: bool = False, ignore_rules: List[str] = None):
        self.strict = strict
        self.ignore_rules = ignore_rules or []
        self.issues: List[Issue] = []

    def validate_file(self, filepath: str) -> List[Issue]:
        """Validate a single markdown file."""
        self.issues = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
        except UnicodeDecodeError:
            self.issues.append(Issue(
                file=filepath,
                line=0,
                column=0,
                rule="encoding",
                severity=Severity.ERROR,
                message="File is not valid UTF-8 encoding"
            ))
            return self.issues
        except Exception as e:
            self.issues.append(Issue(
                file=filepath,
                line=0,
                column=0,
                rule="file-read",
                severity=Severity.ERROR,
                message=f"Cannot read file: {e}"
            ))
            return self.issues

        # Run all checks
        self._check_frontmatter(filepath, content, lines)
        self._check_special_chars(filepath, lines)
        self._check_smart_quotes(filepath, lines)
        self._check_links(filepath, lines)
        self._check_images(filepath, lines)
        self._check_code_blocks(filepath, content, lines)
        self._check_headings(filepath, lines)
        self._check_line_length(filepath, lines)
        self._check_trailing_whitespace(filepath, lines)
        self._check_consecutive_blank_lines(filepath, lines)

        # Filter ignored rules
        self.issues = [i for i in self.issues if i.rule not in self.ignore_rules]

        return self.issues

    def _check_frontmatter(self, filepath: str, content: str, lines: List[str]):
        """Check YAML frontmatter."""
        if not content.startswith('---'):
            self.issues.append(Issue(
                file=filepath,
                line=1,
                column=1,
                rule="frontmatter-missing",
                severity=Severity.ERROR,
                message="Missing YAML frontmatter (file should start with ---)"
            ))
            return

        # Find closing frontmatter
        second_delimiter = content.find('---', 3)
        if second_delimiter == -1:
            self.issues.append(Issue(
                file=filepath,
                line=1,
                column=1,
                rule="frontmatter-incomplete",
                severity=Severity.ERROR,
                message="Frontmatter is not properly closed (missing closing ---)"
            ))
            return

        frontmatter = content[3:second_delimiter].strip()
        
        # Check required fields
        required_fields = ['title', 'date']
        for field in required_fields:
            if not re.search(rf'^{field}:', frontmatter, re.MULTILINE):
                self.issues.append(Issue(
                    file=filepath,
                    line=1,
                    column=1,
                    rule=f"frontmatter-{field}",
                    severity=Severity.ERROR,
                    message=f"Missing required frontmatter field: {field}"
                ))

        # Check date format
        date_match = re.search(r'^date:\s*(.+)$', frontmatter, re.MULTILINE)
        if date_match:
            date_str = date_match.group(1).strip()
            # Should be YYYY-MM-DD or YYYY-MM-DD HH:MM:SS format
            if not re.match(r'^\d{4}-\d{2}-\d{2}(\s+\d{2}:\d{2}:\d{2})?$', date_str):
                self.issues.append(Issue(
                    file=filepath,
                    line=1,
                    column=1,
                    rule="frontmatter-date-format",
                    severity=Severity.WARNING,
                    message=f"Date format should be YYYY-MM-DD or YYYY-MM-DD HH:MM:SS, got: {date_str}"
                ))

    def _check_special_chars(self, filepath: str, lines: List[str]):
        """Check for problematic special characters."""
        for line_num, line in enumerate(lines, 1):
            for char, name in self.PROBLEMATIC_CHARS.items():
                col = line.find(char)
                if col != -1:
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=col + 1,
                        rule="special-char",
                        severity=Severity.WARNING,
                        message=f"Found problematic character: {name} (U+{ord(char):04X})",
                        suggestion=f"Remove or replace the {name}"
                    ))

    def _check_smart_quotes(self, filepath: str, lines: List[str]):
        """Check for smart quotes that should be converted."""
        for line_num, line in enumerate(lines, 1):
            for smart, regular in self.SMART_QUOTES.items():
                col = line.find(smart)
                if col != -1:
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=col + 1,
                        rule="smart-quote",
                        severity=Severity.INFO if not self.strict else Severity.WARNING,
                        message=f"Found smart quote: '{smart}'",
                        suggestion=f"Replace with regular quote: '{regular}'"
                    ))

    def _check_links(self, filepath: str, lines: List[str]):
        """Check markdown links."""
        link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]*)\)')
        
        for line_num, line in enumerate(lines, 1):
            for match in link_pattern.finditer(line):
                text, url = match.groups()
                col = match.start() + 1
                
                # Check empty link text
                if not text.strip():
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=col,
                        rule="link-empty-text",
                        severity=Severity.WARNING,
                        message="Link has empty text"
                    ))
                
                # Check empty URL
                if not url.strip():
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=col,
                        rule="link-empty-url",
                        severity=Severity.ERROR,
                        message="Link has empty URL"
                    ))
                
                # Check for spaces in URL
                if ' ' in url and not url.startswith('<'):
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=col,
                        rule="link-space-url",
                        severity=Severity.ERROR,
                        message="Link URL contains spaces",
                        suggestion="Encode spaces as %20 or wrap URL in angle brackets"
                    ))

    def _check_images(self, filepath: str, lines: List[str]):
        """Check markdown images."""
        image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]*)\)')
        
        for line_num, line in enumerate(lines, 1):
            for match in image_pattern.finditer(line):
                alt, src = match.groups()
                col = match.start() + 1
                
                # Check empty alt text
                if not alt.strip() and self.strict:
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=col,
                        rule="image-empty-alt",
                        severity=Severity.WARNING,
                        message="Image has empty alt text (accessibility issue)"
                    ))
                
                # Check empty source
                if not src.strip():
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=col,
                        rule="image-empty-src",
                        severity=Severity.ERROR,
                        message="Image has empty source"
                    ))

    def _check_code_blocks(self, filepath: str, content: str, lines: List[str]):
        """Check code blocks."""
        # Count code block delimiters
        code_block_count = content.count('```')
        if code_block_count % 2 != 0:
            self.issues.append(Issue(
                file=filepath,
                line=0,
                column=0,
                rule="code-block-unclosed",
                severity=Severity.ERROR,
                message="Unclosed code block (mismatched ``` delimiters)"
            ))

        # Check for code blocks without language specification
        if self.strict:
            in_code_block = False
            for line_num, line in enumerate(lines, 1):
                if line.strip().startswith('```'):
                    if not in_code_block:
                        # Opening code block
                        lang = line.strip()[3:].strip()
                        if not lang:
                            self.issues.append(Issue(
                                file=filepath,
                                line=line_num,
                                column=1,
                                rule="code-block-no-lang",
                                severity=Severity.INFO,
                                message="Code block without language specification"
                            ))
                    in_code_block = not in_code_block

    def _check_headings(self, filepath: str, lines: List[str]):
        """Check heading format."""
        prev_level = 0
        in_code_block = False
        
        for line_num, line in enumerate(lines, 1):
            # Skip code blocks
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            
            # Check ATX headings
            match = re.match(r'^(#{1,6})\s*(.*)', line)
            if match:
                level = len(match.group(1))
                text = match.group(2)
                
                # Check for no space after #
                if not text:
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=1,
                        rule="heading-empty",
                        severity=Severity.WARNING,
                        message="Empty heading"
                    ))
                
                # Check heading level jump (skip more than one level)
                if self.strict and prev_level > 0 and level > prev_level + 1:
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=1,
                        rule="heading-level-jump",
                        severity=Severity.WARNING,
                        message=f"Heading level jumps from {prev_level} to {level}"
                    ))
                
                prev_level = level

    def _check_line_length(self, filepath: str, lines: List[str]):
        """Check for very long lines."""
        if not self.strict:
            return
            
        max_length = 300
        in_code_block = False
        
        for line_num, line in enumerate(lines, 1):
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            
            if not in_code_block and len(line) > max_length:
                self.issues.append(Issue(
                    file=filepath,
                    line=line_num,
                    column=1,
                    rule="line-length",
                    severity=Severity.INFO,
                    message=f"Line is very long ({len(line)} chars)"
                ))

    def _check_trailing_whitespace(self, filepath: str, lines: List[str]):
        """Check for trailing whitespace."""
        if not self.strict:
            return
            
        for line_num, line in enumerate(lines, 1):
            if line != line.rstrip() and not line.endswith('  '):  # Ignore intentional line breaks
                self.issues.append(Issue(
                    file=filepath,
                    line=line_num,
                    column=len(line.rstrip()) + 1,
                    rule="trailing-whitespace",
                    severity=Severity.INFO,
                    message="Trailing whitespace"
                ))

    def _check_consecutive_blank_lines(self, filepath: str, lines: List[str]):
        """Check for too many consecutive blank lines."""
        if not self.strict:
            return
            
        consecutive = 0
        for line_num, line in enumerate(lines, 1):
            if line.strip() == '':
                consecutive += 1
                if consecutive > 2:
                    self.issues.append(Issue(
                        file=filepath,
                        line=line_num,
                        column=1,
                        rule="consecutive-blank-lines",
                        severity=Severity.INFO,
                        message=f"More than 2 consecutive blank lines ({consecutive})"
                    ))
            else:
                consecutive = 0


def format_output(issues: List[Issue], output_format: str) -> str:
    """Format issues for output."""
    if output_format == "json":
        return json.dumps([{**asdict(i), 'severity': i.severity.value} for i in issues], indent=2)
    
    elif output_format == "markdown":
        if not issues:
            return "# Validation Report\n\n✅ No issues found!"
        
        output = "# Validation Report\n\n"
        output += f"Found **{len(issues)}** issues:\n\n"
        
        by_file = {}
        for issue in issues:
            if issue.file not in by_file:
                by_file[issue.file] = []
            by_file[issue.file].append(issue)
        
        for filepath, file_issues in by_file.items():
            output += f"## {filepath}\n\n"
            for issue in file_issues:
                icon = "❌" if issue.severity == Severity.ERROR else "⚠️" if issue.severity == Severity.WARNING else "ℹ️"
                output += f"- {icon} **Line {issue.line}**: [{issue.rule}] {issue.message}\n"
            output += "\n"
        
        return output
    
    else:  # text
        if not issues:
            return "✅ No issues found!"
        
        output = []
        for issue in issues:
            icon = "❌" if issue.severity == Severity.ERROR else "⚠️" if issue.severity == Severity.WARNING else "ℹ️"
            output.append(f"{icon} {issue.file}:{issue.line}:{issue.column} [{issue.rule}] {issue.message}")
            if issue.suggestion:
                output.append(f"   💡 {issue.suggestion}")
        
        return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(description="Validate markdown files for Hexo blog format")
    parser.add_argument("path", nargs="?", default=".", help="File or directory to validate")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode")
    parser.add_argument("--output", choices=["text", "json", "markdown"], default="text",
                        help="Output format")
    parser.add_argument("--ignore", default="", help="Comma-separated rules to ignore")
    parser.add_argument("--fix", action="store_true", help="Attempt to fix issues (not implemented)")
    
    args = parser.parse_args()
    
    ignore_rules = [r.strip() for r in args.ignore.split(',') if r.strip()]
    validator = MarkdownValidator(strict=args.strict, ignore_rules=ignore_rules)
    
    path = Path(args.path)
    all_issues = []
    
    if path.is_file():
        all_issues = validator.validate_file(str(path))
    elif path.is_dir():
        for md_file in path.rglob("*.md"):
            issues = validator.validate_file(str(md_file))
            all_issues.extend(issues)
    else:
        print(f"❌ Path not found: {path}")
        sys.exit(1)
    
    print(format_output(all_issues, args.output))
    
    # Exit with error code if there are errors
    has_errors = any(i.severity == Severity.ERROR for i in all_issues)
    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
