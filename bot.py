"""
Tank Wars — Telegram Bot
Запускает бота, который открывает Mini App по команде /play

Требования:
  pip install python-telegram-bot==20.*

Переменные окружения:
  BOT_TOKEN   — токен от @BotFather
  WEBAPP_URL  — HTTPS-URL, где хостится index.html
                (например https://yourdomain.com/tankwars/)
"""

import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN  = os.environ["BOT_TOKEN"]
WEBAPP_URL = os.environ["WEBAPP_URL"]   # Должен быть HTTPS!


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 *Tank Wars* — тактический артиллерийский бой!\n\n"
        "До 8 танков, случайный ландшафт, ветер, три уровня ИИ и магазин оружия.\n\n"
        "Нажми кнопку ниже чтобы начать сражение 👇",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="⚔️ Играть",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]])
    )


async def play(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await start(update, ctx)


async def help_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ *Как играть:*\n\n"
        "• Регулируй *угол* и *силу* залпа\n"
        "• Следи за *ветром* — он сносит снаряд\n"
        "• Уничтожь все вражеские танки\n"
        "• После боя трать очки в *магазине*\n\n"
        "Оружие: Снаряд · Ракета · Кассета · Ядерная · Щит · Ремонт\n\n"
        "/play — начать игру\n"
        "/help — эта справка",
        parse_mode="Markdown"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play",  play))
    app.add_handler(CommandHandler("help",  help_cmd))
    print("Tank Wars bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
