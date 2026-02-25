#!/bin/bash

# Safe push script - YOU run this with YOUR new token

cd /home/rifa/streamstyle-ai

echo "🚀 StreamStyle AI - GitHub Push Script"
echo "======================================"
echo ""
echo "⚠️  IMPORTANT: Use a NEW token, not the exposed one!"
echo ""
echo "Get a new token from: https://github.com/settings/tokens"
echo ""
read -p "Press Enter when you have your NEW token ready..."

# Add remote
echo ""
echo "📡 Adding remote repository..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/Tasfia-17/streamstyle.git

# Push
echo ""
echo "📤 Pushing to GitHub..."
echo ""
echo "When prompted:"
echo "  Username: Tasfia-17"
echo "  Password: [Paste your NEW token]"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Code pushed to GitHub!"
    echo ""
    echo "🌐 View at: https://github.com/Tasfia-17/streamstyle"
    echo ""
    echo "📊 Commits: 74"
    echo "📁 Files: All project files"
    echo "🎨 README: With SVG art"
    echo ""
else
    echo ""
    echo "❌ Push failed. Check:"
    echo "  1. Token has 'repo' scope"
    echo "  2. Repository exists"
    echo "  3. You used the NEW token (not old one)"
    echo ""
fi
