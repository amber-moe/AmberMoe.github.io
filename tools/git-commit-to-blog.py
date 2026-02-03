#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Git Commit to Hexo Blog Post Generator
======================================

This tool reads git commit information and generates Hexo blog posts.
It can be triggered by git hooks to automatically create blog posts for each commit.

Usage:
    python git-commit-to-blog.py [options]

Options:
    --repo-path     Path to the git repository (default: current directory)
    --output-dir    Output directory for generated markdown files (default: ./apps/blog-hexo/source/_posts/)
    --template      Path to custom template file (default: ./tools/templates/commit-post.md)
    --commit        Specific commit hash (default: HEAD)
    --all           Process all commits (use with caution)

Author: Amber Moe
License: MIT
"""

import os
import sys
import argparse
import subprocess
import re
from datetime import datetime
from pathlib import Path


def get_git_commit_info(repo_path: str, commit_hash: str = "HEAD") -> dict:
    """Get commit information from git."""
    try:
        # Get commit hash
        result = subprocess.run(
            ["git", "-C", repo_path, "rev-parse", commit_hash],
            capture_output=True, text=True, check=True
        )
        full_hash = result.stdout.strip()
        short_hash = full_hash[:7]

        # Get commit message (subject and body)
        result = subprocess.run(
            ["git", "-C", repo_path, "log", "-1", "--format=%s%n%b", commit_hash],
            capture_output=True, text=True, check=True
        )
        lines = result.stdout.strip().split('\n')
        subject = lines[0] if lines else "No subject"
        body = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""

        # Get author info
        result = subprocess.run(
            ["git", "-C", repo_path, "log", "-1", "--format=%an%n%ae", commit_hash],
            capture_output=True, text=True, check=True
        )
        author_lines = result.stdout.strip().split('\n')
        author_name = author_lines[0] if author_lines else "Unknown"
        author_email = author_lines[1] if len(author_lines) > 1 else ""

        # Get commit date
        result = subprocess.run(
            ["git", "-C", repo_path, "log", "-1", "--format=%ci", commit_hash],
            capture_output=True, text=True, check=True
        )
        commit_date = result.stdout.strip()

        # Get changed files
        result = subprocess.run(
            ["git", "-C", repo_path, "diff-tree", "--no-commit-id", "--name-only", "-r", commit_hash],
            capture_output=True, text=True, check=True
        )
        changed_files = [f for f in result.stdout.strip().split('\n') if f]

        # Get branch name
        result = subprocess.run(
            ["git", "-C", repo_path, "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, check=True
        )
        branch = result.stdout.strip()

        return {
            "hash": full_hash,
            "short_hash": short_hash,
            "subject": subject,
            "body": body,
            "author_name": author_name,
            "author_email": author_email,
            "date": commit_date,
            "changed_files": changed_files,
            "branch": branch
        }
    except subprocess.CalledProcessError as e:
        print(f"Error getting git commit info: {e}")
        return None


def sanitize_filename(title: str) -> str:
    """Convert title to a valid filename."""
    # Remove special characters
    filename = re.sub(r'[^\w\s\-\u4e00-\u9fff]', '', title)
    # Replace spaces with hyphens
    filename = re.sub(r'\s+', '-', filename)
    # Lowercase
    filename = filename.lower()
    # Limit length
    return filename[:50] if len(filename) > 50 else filename


def generate_blog_post(commit_info: dict, template_path: str, output_dir: str) -> str:
    """Generate a Hexo blog post from commit information."""
    
    # Load template
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    else:
        # Default template
        template = """---
title: {{ title }}
date: {{ date }}
updated: {{ date }}
tags:
  - commit
  - development
categories:
  - Development Log
author: {{ author }}
---

{{ body }}

<!-- more -->

## Commit Details

- **Commit Hash**: `{{ hash }}`
- **Branch**: {{ branch }}
- **Author**: {{ author }}
- **Date**: {{ date }}

## Changed Files

{{ changed_files }}

---

*This post was automatically generated from a git commit.*
"""

    # Parse date
    try:
        dt = datetime.strptime(commit_info["date"][:19], "%Y-%m-%d %H:%M:%S")
        formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
        date_prefix = dt.strftime("%Y-%m-%d")
    except:
        formatted_date = commit_info["date"]
        date_prefix = datetime.now().strftime("%Y-%m-%d")

    # Format changed files as markdown list
    changed_files_md = '\n'.join([f"- `{f}`" for f in commit_info["changed_files"]])
    if not changed_files_md:
        changed_files_md = "- No files changed"

    # Prepare body content
    body = commit_info["body"] if commit_info["body"] else commit_info["subject"]

    # Replace placeholders
    content = template
    content = content.replace("{{ title }}", commit_info["subject"])
    content = content.replace("{{ date }}", formatted_date)
    content = content.replace("{{ author }}", commit_info["author_name"])
    content = content.replace("{{ hash }}", commit_info["short_hash"])
    content = content.replace("{{ full_hash }}", commit_info["hash"])
    content = content.replace("{{ branch }}", commit_info["branch"])
    content = content.replace("{{ body }}", body)
    content = content.replace("{{ changed_files }}", changed_files_md)

    # Generate filename
    filename = f"{date_prefix}-{sanitize_filename(commit_info['subject'])}.md"
    output_path = os.path.join(output_dir, filename)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Write file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate Hexo blog posts from git commits")
    parser.add_argument("--repo-path", default=".", help="Path to git repository")
    parser.add_argument("--output-dir", default="./apps/blog-hexo/source/_posts/", 
                        help="Output directory for markdown files")
    parser.add_argument("--template", default="./tools/templates/commit-post.md",
                        help="Path to template file")
    parser.add_argument("--commit", default="HEAD", help="Commit hash to process")
    parser.add_argument("--all", action="store_true", help="Process all commits")
    
    args = parser.parse_args()

    # Get absolute paths
    repo_path = os.path.abspath(args.repo_path)
    output_dir = os.path.abspath(args.output_dir)
    template_path = os.path.abspath(args.template)

    print(f"📝 Git Commit to Blog Post Generator")
    print(f"   Repository: {repo_path}")
    print(f"   Output: {output_dir}")
    print(f"   Template: {template_path}")
    print()

    # Get commit info
    commit_info = get_git_commit_info(repo_path, args.commit)
    if not commit_info:
        print("❌ Failed to get commit information")
        sys.exit(1)

    print(f"📋 Processing commit: {commit_info['short_hash']}")
    print(f"   Subject: {commit_info['subject']}")
    print(f"   Author: {commit_info['author_name']}")
    print(f"   Date: {commit_info['date']}")
    print()

    # Generate blog post
    output_path = generate_blog_post(commit_info, template_path, output_dir)
    print(f"✅ Generated: {output_path}")


if __name__ == "__main__":
    main()
