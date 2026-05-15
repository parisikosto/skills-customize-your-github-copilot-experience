from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

# Task 1: Create a GET endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "FastAPI app is running"}

# Task 2: Create a path parameter endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {
        "item_id": item_id,
        "query": q,
        "name": "Example Item",
        "description": "This item was retrieved using a path parameter"
    }

# Task 3: Create a POST endpoint with JSON input
@app.post("/items")
def create_item(item: Item):
    if item.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be greater than zero")
    return {"message": "Item created successfully", "item": item}

# Example run command:
# uvicorn starter-code:app --reload
