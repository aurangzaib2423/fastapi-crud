from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI CRUD")

ITEMS = [
    {"id": 1, "item": "mobile"},
    {"id": 2, "item": "laptop"}
]

class Item(BaseModel):
    id: int
    item: str

@app.get("/", tags=["health"])
def health_check():
    return {"message": "API is running successfully!"}

@app.get("/v1/items", tags=["items"])
def get_items():
    return {"message": "All items fetched successfully.", "data": ITEMS}

@app.post("/v1/items", tags=["items"])
def create_item(item: Item):
    new_item = item.dict()
    ITEMS.append(new_item)
    return {"message": "Item created successfully!", "data": new_item}

@app.put("/v1/items/{item_id}", tags=["items"])
def update_item(item_id: int, item: Item):
    for i in ITEMS:
        if i["id"] == item_id:
            i["item"] = item.item
            return {"message": "Item updated successfully!", "data": i}
    return {"error": "Item not found!"}

@app.delete("/v1/items/{item_id}", tags=["items"])
def delete_item(item_id: int):
    for i in ITEMS:
        if i["id"] == item_id:
            ITEMS.remove(i)
            return {"message": "Item deleted successfully!", "data": i}
    return {"error": "Item not found!"}
