from fastapi import FastAPI
from app.database.initialize import initialize_database
from app.routers import pet
import uvicorn

app = FastAPI(
    title="Pet store API"

)


def main():
    initialize_database()
    app.include_router(pet.router)
    uvicorn.run(app, port=3000)


if __name__ == "__main__":
    main()
