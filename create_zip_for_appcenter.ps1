# PowerShell скрипт для создания ZIP архива для AppCenter

Write-Host "Creating ZIP archive for AppCenter..." -ForegroundColor Green
Write-Host ""

# Проверяем наличие проекта
if (-not (Test-Path "ReminderApp.xcodeproj")) {
    Write-Host "ERROR: ReminderApp.xcodeproj not found!" -ForegroundColor Red
    Write-Host "Make sure you are in the ReminderApp folder" -ForegroundColor Red
    exit 1
}

# Проверяем наличие папки с кодом
if (-not (Test-Path "ReminderApp")) {
    Write-Host "ERROR: ReminderApp folder not found!" -ForegroundColor Red
    exit 1
}

# Удаляем старый ZIP если есть
if (Test-Path "ReminderApp.zip") {
    Remove-Item "ReminderApp.zip" -Force
    Write-Host "Removed old ZIP archive" -ForegroundColor Yellow
}

# Создаем ZIP архив
Write-Host "Creating ReminderApp.zip..." -ForegroundColor Cyan
try {
    Compress-Archive -Path "ReminderApp.xcodeproj", "ReminderApp" -DestinationPath "ReminderApp.zip" -Force
    
    if (Test-Path "ReminderApp.zip") {
        $zipSize = (Get-Item "ReminderApp.zip").Length / 1MB
        Write-Host ""
        Write-Host "SUCCESS! ZIP archive created: ReminderApp.zip" -ForegroundColor Green
        Write-Host "Size: $([math]::Round($zipSize, 2)) MB" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Next steps:" -ForegroundColor Yellow
        Write-Host "1. Go to https://appcenter.ms" -ForegroundColor White
        Write-Host "2. Sign up / Login" -ForegroundColor White
        Write-Host "3. Create new iOS app" -ForegroundColor White
        Write-Host "4. Upload this ZIP file (ReminderApp.zip)" -ForegroundColor White
        Write-Host "5. Configure build settings" -ForegroundColor White
        Write-Host "6. Build and download IPA" -ForegroundColor White
        Write-Host ""
        Write-Host "See APP_CENTER_GUIDE.md for detailed instructions" -ForegroundColor Cyan
    } else {
        Write-Host "ERROR: Failed to create ZIP archive" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

