from pydantic import BaseModel


class Pet(BaseModel):
    name: str
    age: int
    pet_type: str


class PetOut(Pet):
    id: int
    created_at: str
