from pydantic import BaseModel


class User(BaseModel):
    id: str | None # Es opcional
    username: str
    email: str