import sqlite3
from datetime import datetime
from models.pet import Pet, PetOut


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
