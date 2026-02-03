#!/bin/bash
# Install git hooks script
#
# Usage: ./tools/install-hooks.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
GIT_HOOKS_DIR="$REPO_ROOT/.git/hooks"
TOOLS_HOOKS_DIR="$SCRIPT_DIR/hooks"

echo "🔧 Installing git hooks..."
echo "   Repository: $REPO_ROOT"
echo "   Hooks source: $TOOLS_HOOKS_DIR"
echo "   Hooks target: $GIT_HOOKS_DIR"
echo ""

# Check if .git directory exists
if [ ! -d "$REPO_ROOT/.git" ]; then
    echo "❌ Error: Not a git repository"
    exit 1
fi

# Create hooks directory if not exists
mkdir -p "$GIT_HOOKS_DIR"

# Copy hooks
for hook in "$TOOLS_HOOKS_DIR"/*; do
    if [ -f "$hook" ]; then
        hook_name=$(basename "$hook")
        target="$GIT_HOOKS_DIR/$hook_name"
        
        # Backup existing hook if it exists and is different
        if [ -f "$target" ]; then
            if ! diff -q "$hook" "$target" > /dev/null 2>&1; then
                echo "   📋 Backing up existing $hook_name to $hook_name.bak"
                cp "$target" "$target.bak"
            fi
        fi
        
        # Copy hook
        cp "$hook" "$target"
        chmod +x "$target"
        echo "   ✅ Installed: $hook_name"
    fi
done

echo ""
echo "🎉 Git hooks installed successfully!"
echo ""
echo "Available hooks:"
for hook in "$GIT_HOOKS_DIR"/*; do
    if [ -f "$hook" ] && [ -x "$hook" ]; then
        hook_name=$(basename "$hook")
        if [[ ! "$hook_name" == *.* ]]; then
            echo "   - $hook_name"
        fi
    fi
done
