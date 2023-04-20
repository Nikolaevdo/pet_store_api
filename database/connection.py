import sqlite3
from datetime import datetime
from models.pet import PetOut, Pet


class Connection:
    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)

    def get_pets(self, limit: int) -> list[PetOut]:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM pets LIMIT{limit}")
        rows = cursor.fetchall()
        pets = []
        for row in rows:
            pet_dict = dict(zip(('id', 'name', 'age', 'pet_type', 'created_at'), row))
            pets.append(PetOut(**pet_dict))
        return pets

    def add_pet(self, pet: Pet):
        cursor = self.conn.cursor()
        created_at = datetime.now().isoformat()
        cursor.execute("INSERT INTO pets (name, age, type, created_at) VALUES (?, ?, ?, ?)",
                       (pet.name, pet.age, pet.pet_type, created_at))
        self.conn.commit()
        cursor.execute(f"SELECT * FROM pets WHERE id = {cursor.lastrowid}")
        result = cursor.fetchone()
        last_record_dict = {
            "id": result[0],
            "name": result[1],
            "age": result[2],
            "pet_type": result[3],
            "created_at": result[4]
        }
        return last_record_dict
