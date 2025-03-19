from pydantic import BaseModel

class Note(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    tags: list
    created_at: str
    updated_at: str

class UserCredentials(BaseModel):
    username: str
    password: str