from pydantic import BaseModel

class Note(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    tags: list
    created_at: str
    updated_at: str

class EditNote(BaseModel):
    title: str
    content: str
    tags: list
    updated_at: str