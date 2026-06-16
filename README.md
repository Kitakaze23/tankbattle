# Tank Wars — Telegram Mini App

## Файлы

| Файл | Назначение |
|------|-----------|
| `index.html` | Игра (Mini App) — единственный файл для хостинга |
| `bot.py` | Telegram-бот, открывающий игру кнопкой |
| `README.md` | Эта инструкция |

---

## Деплой: пошагово

### 1. Создай бота
1. Открой [@BotFather](https://t.me/BotFather) в Telegram
2. Отправь `/newbot`, задай имя и username
3. Скопируй **BOT_TOKEN**

### 2. Захости index.html (нужен HTTPS!)

**Вариант A — Vercel (бесплатно, 2 минуты):**
```bash
npx vercel --name tankwars
# Загрузи index.html, получи https://tankwars-xxx.vercel.app
```

**Вариант B — GitHub Pages:**
1. Создай репозиторий
2. Положи `index.html` в корень
3. Settings → Pages → Branch: main → / (root)
4. URL: `https://username.github.io/repo-name/`

**Вариант C — Nginx на VPS:**
```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com;
    root /var/www/tankwars;
    index index.html;
}
```

### 3. Включи Mini App у BotFather
```
/newapp          → для создания нового Mini App
  или
/mybots → [бот] → Bot Settings → Menu Button → Edit Menu Button URL
```
Вставь HTTPS-URL твоего `index.html`.

### 4. Запусти бота
```bash
pip install python-telegram-bot==20.*

BOT_TOKEN=xxx WEBAPP_URL=https://your-url.com python bot.py
```

---

## Telegram WebApp API — что используется в игре

| API | Назначение |
|-----|-----------|
| `tg.ready()` | Сообщает Telegram что приложение загружено |
| `tg.expand()` | Разворачивает на весь экран |
| `tg.disableVerticalSwipes()` | Отключает свайп вниз чтобы не закрыть игру |
| `tg.HapticFeedback` | Вибрация при выстреле, попадании, покупке |
| `tg.BackButton` | Кнопка "назад" в шапке Telegram |
| `tg.initDataUnsafe.user` | Имя игрока из профиля Telegram |
| `tg.showAlert()` | Нативный алерт Telegram вместо browser alert |
| CSS `env(safe-area-inset-*)` | Отступы для Dynamic Island / навигации Android |

---

## Требования к хостингу

- ✅ **HTTPS обязателен** — Telegram не открывает HTTP
- ✅ Правильный `Content-Type: text/html` 
- ✅ CORS не нужен — это статический файл
- ✅ Один файл `index.html`, никаких зависимостей
