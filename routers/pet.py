from typing import List

from fastapi import FastAPI, APIRouter
from database.connection import Connection
from models.pet import Pet, PetOut
from database.initialize import DB_FILE

app = FastAPI()
router = APIRouter()


@router.get("/pets", response_model=List[PetOut])
async def read_pets(limit=20):
    conn = Connection(DB_FILE)
    pets = conn.get_pets(limit)
    return pets


@router.post("/pets", response_model=PetOut)
async def add_pet(pet: Pet):
    conn = Connection(DB_FILE)
    pet_data = conn.add_pet(pet)
    return pet_data
