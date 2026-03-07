from pydantic import BaseModel

class Recipe(BaseModel):
    title: str
    description: str
    category_id: int