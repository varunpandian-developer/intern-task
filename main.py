from fastapi import FastAPI,HTTPException
from connect import SessionLocal, engine
from models import Base, Item
from pydantic import BaseModel

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

#Create Basemodel 

class ItemCreate(BaseModel):
    name: str
    description: str

# Route to add a new item
@app.post("/items/")
async def add_item(item: ItemCreate):
    db = SessionLocal()
    try:
        new_item = Item(name=item.name, description=item.description)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    finally:
        db.close()

@app.post("/items/")
async def add_item(item: ItemCreate):
    db = SessionLocal()
    try:
        new_item = Item(name=item.name, description=item.description)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    finally:
        db.close()
        
# Route to get an item by ID
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    db = SessionLocal()
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"id": item.id, "name": item.name, "description": item.description}
    finally:
        db.close()