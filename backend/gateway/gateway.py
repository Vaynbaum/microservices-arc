# импорт библиотек
from fastapi import FastAPI
from pydantic import BaseModel
import requests

URL_GAME = "http://game:3000/"
URL_POST = "http://post:3001/"


# основная точка взаимодействия для создания API.
app = FastAPI()

# сыграть с компьютером
@app.get("/game/play")
async def game_play(user_action: str):
    res = requests.get(
        f"{URL_GAME}play?user_action={user_action}",
    )
    return res.json()


# получить варианты выбора игры
@app.get("/game/choice")
async def get_all_choices():
    res = requests.get(
        f"{URL_GAME}choice",
    )
    return res.json()


#  получить все посты
@app.get("/post/all")
async def get_all_posts():
    res = requests.get(
        f"{URL_POST}all",
    )
    return res.json()


# модель поста
class Post(BaseModel):
    name: str
    description: str
    author: str


#  получить все посты
@app.post("/post/add")
async def add_post(post: Post):
    res = requests.post(f"{URL_POST}add", json=post.dict())
    return res.json()
