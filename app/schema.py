from pydantic import BaseModel


class TGMessage(BaseModel):
    message: str
