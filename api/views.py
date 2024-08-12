from fastapi import APIRouter, status
from telegram import Bot
from app.schema import TGMessage
from config import config

routes = APIRouter()


@routes.post(
    "/send_message",
    status_code=status.HTTP_200_OK
)
async def main(data: TGMessage):
    bot = Bot(config.BOT_TOKEN)
    async with bot:
        await bot.send_message(text=data.message, chat_id=config.CHAT_ID)
