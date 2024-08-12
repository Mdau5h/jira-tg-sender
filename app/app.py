from fastapi import FastAPI
from api.views import routes


def create_app():
    app = FastAPI(title='Jira TG Sender')
    app.include_router(routes)
    return app
