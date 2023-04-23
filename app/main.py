from fastapi import FastAPI
from app.database.initialize import initialize_database
from app.routers import pet
import uvicorn

app = FastAPI(
    title="Pet store API"
)
initialize_database()
app.include_router(pet.router)

if __name__ == "__main__":
    uvicorn.run(app)
