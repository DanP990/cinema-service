from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/cinemas/openapi.json", docs_url="/api/v1/cinemas/docs")

cinemas_router = APIRouter()

cinemas = [
    {
        "cinemas_id": 1,
        "name": "KinoMax",
        "description": "47",
        "visitors": "1 billion",
        "address": "123 Main Street"
    },
    {
        "cinemas_id": 2,
        "name": "Cineplex",
        "description": "47",
        "visitors": "1 billion",
        "address": "456 Elm Street"
    },
    {
        "cinemas_id": 3,
        "name": "SilverScreen",
        "description": "47",
        "visitors": "1 billion",
        "address": "789 Oak Avenue"
    },
    {
        "cinemas_id": 4,
        "name": "StarCinema",
        "description": "47",
        "visitors": "1 billion",
        "address": "1010 Maple Drive"
    },
    {
        "cinemas_id": 5,
        "name": "GoldenTheater",
        "description": "47",
        "visitors": "1 billion",
        "address": "1212 Pine Lane"
    }
]


@cinemas_router.get("/")
async def read_cinemas():
    return cinemas


@cinemas_router.get("/{cinemas_id}")
async def read_cinema(cinemas_id: int):
    for cinema in cinemas:
        if cinema['cinemas_id'] == cinemas_id:
            return cinema
    return None

app.include_router(cinemas_router, prefix='/api/v1/cinemas', tags=['cinemas'])

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
