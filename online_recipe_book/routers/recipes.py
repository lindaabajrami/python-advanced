from fastapi import APIRouter
from models.recipe import Recipe
from database import get_db

router = APIRouter()

@router.post("/recipes")
def create_recipe(recipe: Recipe):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO recipes (title, description, category_id) VALUES (?, ?, ?)",
        (recipe.title, recipe.description, recipe.category_id)
    )

    conn.commit()
    recipe_id = cursor.lastrowid
    conn.close()

    return {"id": recipe_id}


@router.get("/recipes")
def get_recipes():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]