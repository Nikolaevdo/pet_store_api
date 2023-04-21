from typing import List

from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from database.connection import Connection
from models.pet import Pet, PetOut
from database.initialize import DB_FILE

app = FastAPI()
router = APIRouter()


@router.get("/pets", response_model=List[PetOut])
async def read_pets_endpoint(limit=20):
    conn = Connection(DB_FILE)
    pets = conn.get_pets(limit)
    return pets


@router.post("/pets", response_model=PetOut)
async def add_pet_endpoint(pet: Pet):
    conn = Connection(DB_FILE)
    pet_data = conn.add_pet(pet)
    return pet_data


@router.delete("/pets")
def delete_pets_endpoint(ids: list[int]):
    conn = Connection(DB_FILE)
    result_dict = conn.delete_pets(ids)
    return JSONResponse(content=result_dict)
