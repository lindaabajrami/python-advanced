from fastapi import APIRouter
from models.category import Category
from database import get_db

router = APIRouter()

@router.post("/categories")
def create_category(category: Category):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO categories (name) VALUES (?)",
        (category.name,)
    )

    conn.commit()
    category_id = cursor.lastrowid
    conn.close()

    return {"id": category_id, "name": category.name}


@router.get("/categories")
def get_categories():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM categories")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]