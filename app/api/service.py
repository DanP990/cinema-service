import os
import httpx

LABEL_SERVICE_HOST_URL = 'http://localhost:8020/api/v1/movies/'

def is_movie_present(movie_id: int):
    return True