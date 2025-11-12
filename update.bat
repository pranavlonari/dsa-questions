@echo off
REM Quick update script for DSA repository (Windows)
REM Just run: update.bat

echo ==================================
echo   DSA Repository Updater
echo ==================================
echo.

REM Run the generator
python generate.py

if %errorlevel% equ 0 (
    echo.
    echo Successfully updated all files!
    echo.
    echo Files updated:
    echo    - questions.json
    echo    - README.md
    echo    - index.html
    echo.
    echo Next: Review changes and commit to git
    echo.
    
    set /p commit="Would you like to commit these changes? (y/n): "
    if /i "%commit%"=="y" (
        git add questions.json README.md index.html
        
        set /p msg="Enter commit message (or press Enter for default): "
        if "%msg%"=="" set msg=Update: Auto-generated files
        
        git commit -m "%msg%"
        echo.
        echo Changes committed!
        echo.
        
        set /p push="Push to GitHub? (y/n): "
        if /i "%push%"=="y" (
            git push
            echo Pushed to GitHub!
        )
    )
) else (
    echo Error occurred. Please check the output above.
    exit /b 1
)

pause
