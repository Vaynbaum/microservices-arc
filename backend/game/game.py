# импорт библиотек
from fastapi import FastAPI
import random

# база данных
DB = {
    "choice": ["камень", "ножницы", "бумага"],
    "result": ["ничья", "победа", "проигрыш"],
}

# основная точка взаимодействия для создания API.
app = FastAPI()

# сыграть с компьютером
@app.get("/play")
async def play(user_action: str):
    computer_action = random.choice(DB["choice"])
    result = ascertain_winner(user_action, computer_action)
    return {"result": result, "computer_action": computer_action}


# получить варианты выбора
@app.get("/choice")
async def get_all_choices():
    return DB["choice"]


def ascertain_winner(user_action, computer_action):
    results = DB["result"]
    if user_action == computer_action:
        return results[0]               # ничья
    elif user_action == "камень":
        if computer_action == "ножницы":
            return results[1]           # победа
        else:
            return results[2]           # проигрыш
    elif user_action == "бумага":
        if computer_action == "камень":
            return results[1]           # победа
        else:
            return results[2]           # проигрыш
    elif user_action == "ножницы":
        if computer_action == "бумага":
            return results[1]           # победа
        else:
            return results[2]           # проигрыш