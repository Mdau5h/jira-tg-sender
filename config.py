from dotenv import load_dotenv
from pydantic.v1 import BaseSettings


load_dotenv()


class Config(BaseSettings):

    HOST: str
    PORT: int
    BOT_TOKEN: str
    CHAT_ID: str


config = Config()





