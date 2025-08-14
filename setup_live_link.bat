@echo off
echo 🚀 Setting up your live question bank...
echo.

REM Check if git is available
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git not found. Please install Git first:
    echo    Download from: https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

REM Get user input
set /p username="Your GitHub username: "
set /p repo_name="Repository name (press enter for 'subsequence-subarray-problems'): "

REM Set default repo name if empty
if "%repo_name%"=="" set repo_name=subsequence-subarray-problems

echo.
echo 🔧 Setting up repository...

REM Initialize git if not already initialized
if not exist ".git" (
    git init
    echo ✅ Git repository initialized
)

REM Add all files
git add .
echo ✅ Files added to git

REM Commit
git commit -m "Add subsequence and subarray question bank with live links"
echo ✅ Files committed

REM Add remote
git remote add origin https://github.com/%username%/%repo_name%.git
echo ✅ Remote repository added

REM Set main branch
git branch -M main

echo.
echo 📤 Ready to push to GitHub!
echo.
echo ⚠️  IMPORTANT: Before running 'git push':
echo 1. Go to https://github.com/%username%/%repo_name%
echo 2. Create the repository if it doesn't exist
echo 3. Make sure it's public
echo.
echo Then run: git push -u origin main
echo.
echo 🌐 After pushing, enable GitHub Pages:
echo 1. Go to repository Settings
echo 2. Scroll to 'Pages' section
echo 3. Source: Deploy from a branch
echo 4. Branch: main, Folder: / (root)
echo 5. Click Save
echo.
echo 🎉 Your live link will be:
echo    https://%username%.github.io/%repo_name%/
echo.
echo 📱 Share this link with anyone for instant access to your question bank!
echo.
pause
