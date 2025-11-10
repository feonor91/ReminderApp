@echo off
REM Скрипт для создания ZIP архива для AppCenter
REM Запустите этот файл в папке ReminderApp

echo Creating ZIP archive for AppCenter...
echo.

REM Проверяем наличие папки
if not exist "ReminderApp.xcodeproj" (
    echo ERROR: ReminderApp.xcodeproj not found!
    echo Make sure you are in the ReminderApp folder
    pause
    exit /b 1
)

REM Создаем ZIP архив
echo Creating ReminderApp.zip...
powershell -Command "Compress-Archive -Path 'ReminderApp.xcodeproj', 'ReminderApp' -DestinationPath 'ReminderApp.zip' -Force"

if exist "ReminderApp.zip" (
    echo.
    echo SUCCESS! ZIP archive created: ReminderApp.zip
    echo.
    echo Next steps:
    echo 1. Go to https://appcenter.ms
    echo 2. Create new iOS app
    echo 3. Upload this ZIP file
    echo 4. Build and download IPA
    echo.
) else (
    echo ERROR: Failed to create ZIP archive
    pause
    exit /b 1
)

pause

