from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import CinemaOut, CinemaIn, CinemaUpdate
from app.api import db_manager
from app.api.service import is_movie_present

cinema = APIRouter()

@cinema.post('/', response_model=CinemaIn, status_code=201)
async def create_cinema(payload: CinemaIn):
    for movie_id in payload.labels_id:
        if not is_movie_present(movie_id):
            raise HTTPException(status_code=404, detail=f"Movie with given id:{movie_id} not found")

    cinema_id = await db_manager.add_cinema(payload)
    response = {
        'id': cinema_id,
        **payload.dict()
    }

    return response

@cinema.get('/', response_model=List[CinemaOut])
async def get_():
    return await db_manager.get_all_cinemas()

@cinema.get('/{id}/', response_model=CinemaIn)
async def get_cinema(id: int):
    cinema = await db_manager.get_cinema(id)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found")
    return cinema

@cinema.put('/{id}/', response_model=CinemaOut)
async def update_cinema(id: int, payload: CinemaUpdate):
    cinema = await db_manager.get_cinemat(id)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found")

    update_data = payload.dict(exclude_unset=True)

    if 'labels_id' in update_data:
        for label_id in payload.labels_id:
            if not is_movie_present(label_id):
                raise HTTPException(status_code=404, detail=f"Cinema with given id:{label_id} not found")

    cinema_in_db = CinemaIn(**cinema)

    updated_cinema = cinema_in_db.copy(update=update_data)

    return await db_manager.update_cinema(id, updated_cinema)

@cinema.delete('/{id}/', response_model=None)
async def delete_cinema(id: int):
    cinema = await db_manager.get_cinema(id)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found")
    return await db_manager.delete_cinema(id)