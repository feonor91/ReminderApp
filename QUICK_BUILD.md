# ⚡ Быстрая сборка IPA - 3 простых шага

## 🎯 Bitrise.io - Самый простой способ

### ✅ Что уже готово:
- ✅ Проект готов (`ReminderApp.xcodeproj`)
- ✅ ZIP архив создан (`ReminderApp.zip`)
- ✅ Все файлы на месте

---

## 📋 ШАГ 1: Загрузите проект в GitHub (5 минут)

1. **Создайте репозиторий на GitHub:**
   - https://github.com/new
   - Имя: `ReminderApp`
   - Public или Private
   - НЕ добавляйте README

2. **Загрузите проект:**
   ```bash
   cd F:\cursor\ReminderApp
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/ВАШ_USERNAME/ReminderApp.git
   git push -u origin main
   ```

**Или используйте GitHub Desktop** (проще):
- Скачайте: https://desktop.github.com
- File → Add Local Repository → выберите папку `ReminderApp`
- Publish repository

---

## 📋 ШАГ 2: Создайте приложение в Bitrise (3 минуты)

1. **Откройте:** https://bitrise.io
2. **Войдите** через GitHub
3. **Add new app** → выберите репозиторий `ReminderApp`
4. **Platform:** iOS
5. **Stack:** Xcode 15.x
6. **Finish**

---

## 📋 ШАГ 3: Настройте и соберите (5 минут)

1. **Code Signing:**
   - Settings → Code Signing
   - Add Apple ID
   - Введите Apple ID и пароль

2. **Запустите сборку:**
   - Start build
   - Ждите 10-15 минут

3. **Скачайте IPA:**
   - Artifacts → Download `.ipa`

---

## 📱 Установка на iPhone

1. Подключите iPhone к компьютеру
2. Откройте iTunes
3. Перетащите IPA на устройство
4. На iPhone: Настройки → Управление устройством → Доверьтесь

---

## ⚠️ Если нет GitHub

Можно использовать **Codemagic.io**:
1. https://codemagic.io
2. Войдите через GitHub
3. Add application → iOS
4. Загрузите ZIP или подключите Git
5. Build → Download IPA

---

**Подробная инструкция:** `BUILD_IPA_STEP_BY_STEP.md`

