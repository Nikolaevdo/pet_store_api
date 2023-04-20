from fastapi import FastAPI
from database.initialize import initialize_database
from routers import pet
import uvicorn

app = FastAPI(
    title="Pet store API"
)
app.include_router(pet.router)
initialize_database()

if __name__ == "__main__":
    uvicorn.run(app)
