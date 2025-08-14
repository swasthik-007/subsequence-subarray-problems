#!/bin/bash

echo "🚀 Setting up your live question bank..."
echo ""

# Check if git is available
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install Git first:"
    echo "   Windows: https://git-scm.com/download/win"
    echo "   Mac: brew install git"
    echo "   Linux: sudo apt install git"
    exit 1
fi

# Get user input
echo "📝 Please provide the following information:"
read -p "Your GitHub username: " username
read -p "Repository name (press enter for 'subsequence-subarray-problems'): " repo_name

# Set default repo name if empty
if [ -z "$repo_name" ]; then
    repo_name="subsequence-subarray-problems"
fi

echo ""
echo "🔧 Setting up repository..."

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    git init
    echo "✅ Git repository initialized"
fi

# Add all files
git add .
echo "✅ Files added to git"

# Commit
git commit -m "Add subsequence and subarray question bank with live links"
echo "✅ Files committed"

# Add remote
git remote add origin "https://github.com/$username/$repo_name.git"
echo "✅ Remote repository added"

# Set main branch
git branch -M main

echo ""
echo "📤 Ready to push to GitHub!"
echo ""
echo "⚠️  IMPORTANT: Before running 'git push':"
echo "1. Go to https://github.com/$username/$repo_name"
echo "2. Create the repository if it doesn't exist"
echo "3. Make sure it's public"
echo ""
echo "Then run: git push -u origin main"
echo ""
echo "🌐 After pushing, enable GitHub Pages:"
echo "1. Go to repository Settings"
echo "2. Scroll to 'Pages' section"
echo "3. Source: Deploy from a branch"
echo "4. Branch: main, Folder: / (root)"
echo "5. Click Save"
echo ""
echo "🎉 Your live link will be:"
echo "   https://$username.github.io/$repo_name/"
echo ""
echo "📱 Share this link with anyone for instant access to your question bank!"
