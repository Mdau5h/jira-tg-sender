import uvicorn
from app.app import create_app
from config import config

app = create_app()


if __name__ == '__main__':
    uvicorn.run('asgi:app', host=config.HOST,  port=config.PORT, log_level='debug')
