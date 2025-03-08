import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# /start 명령어 처리
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('안녕하세요! 저는 텔레그램 봇입니다.')

# 일반 메시지 처리
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'당신이 보낸 메시지: {update.message.text}')

def main():
    # BotFather로부터 받은 API 토큰
    TOKEN = os.environ.get("TELEGRAM_API_KEY")

    # Application 객체 생성
    application = Application.builder().token(TOKEN).build()

    # 핸들러 등록
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 봇 실행
    application.run_polling()

if __name__ == '__main__':
    main()

