# coding: utf-8
# импорт библиотек
from fastapi import FastAPI, Query
from difflib import SequenceMatcher

# основная точка взаимодействия для создания API.
app = FastAPI()


@app.get("/analysis")
async def analysis_description(new_post: str = Query(), posts: list[str] = Query()):
    """Проанализировать описание поста с
    сущесвующими описаниями постов"""
    finalsim = 0
    count = len(posts)
    for post in posts:
        finalsim += SequenceMatcher(None, new_post, post).ratio()
    res = round(1 - (finalsim / count), 2)
    return {"result": res * 100}

