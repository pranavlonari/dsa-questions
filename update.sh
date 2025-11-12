#!/bin/bash
# Quick update script for DSA repository
# Just run: ./update.sh

echo "=================================="
echo "  DSA Repository Updater"
echo "=================================="
echo ""

# Run the generator
python3 generate.py

# Check if successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully updated all files!"
    echo ""
    echo "📁 Files updated:"
    echo "   - questions.json"
    echo "   - README.md"
    echo "   - index.html"
    echo ""
    echo "💡 Next: Review changes and commit to git"
    echo ""
    read -p "Would you like to commit these changes? (y/n) " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git add questions.json README.md index.html
        read -p "Enter commit message (or press Enter for default): " commit_msg
        
        if [ -z "$commit_msg" ]; then
            commit_msg="Update: Auto-generated files"
        fi
        
        git commit -m "$commit_msg"
        echo ""
        echo "✅ Changes committed!"
        echo ""
        read -p "Push to GitHub? (y/n) " -n 1 -r
        echo ""
        
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git push
            echo "✅ Pushed to GitHub!"
        fi
    fi
else
    echo "❌ Error occurred. Please check the output above."
    exit 1
fi
