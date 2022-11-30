const express = require("express"); // подключение express
const axios = require('axios');
const app = express();              // создаем объект приложения
const jsonParser = express.json();  // создаем json парсер для данных 
const db = require("./db").db       // база данных

const URL_SIMILARITY = "http://similarity:3002/analysis"

// определяем обработчик для маршрута "/all" - получить все посты
app.get("/all", (req, res) => {
    res.send(db);   // отправляем ответ
});

// добавить пост
app.post("/add", jsonParser, (req, res) => {
    let obj = req.body
    let url = `${URL_SIMILARITY}?`
    for (let i in db)
        url += `posts=${db[i].description}&`
    axios.get(`${url}new_post=${req.body.description}`)
        .then(response => {
            obj.originality = response.data.result
            db.push(obj)
            res.send(obj)
        })
        .catch(error => {
            res.send(error)
        });
})

// начинаем прослушивать подключения на 3001 порту
app.listen(3001, () => {
    console.log("The post service is running...")
});