from app.api.models import CinemaIn, CinemaOut, CinemaUpdate
from app.api.db import cinemas, database


async def add_cinema(payload: CinemaIn):
    query = cinemas.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_cinemas():
    query = cinemas.select()
    return await database.fetch_all(query=query)


async def get_cinema(id):
    query = cinemas.select(cinemas.c.id == id)
    return await database.fetch_one(query=query)


async def delete_cinema(id: int):
    query = cinemas.delete().where(cinemas.c.id == id)
    return await database.execute(query=query)


async def update_cinema(id: int, payload: CinemaIn):
    query = (
        cinemas
        .update()
        .where(cinemas.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
