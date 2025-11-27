from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Vet Clinic Dog Service",
    description="Сервис для хранения информации о собаках",
    version="1.0.0"
)

class Dog(BaseModel):
    name: str
    age: int
    breed: str

dogs_db = {}
current_id = 1


@app.get("/dogs")
def get_all_dogs():
    return dogs_db


@app.get("/dogs/{dog_id}")
def get_dog(dog_id: int):
    if dog_id not in dogs_db:
        raise HTTPException(status_code=404, detail="Dog not found")
    return dogs_db[dog_id]


@app.post("/dogs")
def add_dog(dog: Dog):
    global current_id
    dogs_db[current_id] = dog
    current_id += 1
    return {"message": "Dog added", "id": current_id - 1}


@app.put("/dogs/{dog_id}")
def update_dog(dog_id: int, dog: Dog):
    if dog_id not in dogs_db:
        raise HTTPException(status_code=404, detail="Dog not found")
    dogs_db[dog_id] = dog
    return {"message": "Dog updated", "id": dog_id}


@app.delete("/dogs/{dog_id}")
def delete_dog(dog_id: int):
    if dog_id not in dogs_db:
        raise HTTPException(status_code=404, detail="Dog not found")
    del dogs_db[dog_id]
    return {"message": "Dog deleted", "id": dog_id}
