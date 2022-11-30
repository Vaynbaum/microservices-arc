const express = require("express");
const axios = require('axios');
const hbs = require("hbs");
const jsonParser = express.json();
const app = express();

const URL_BACKEND = "http://gateway:3003/"


app.set("view engine", "hbs");  // движок представлений в Express
hbs.registerPartials(__dirname + "/views/partials");
app.use(express.static('.'));

app.get("/api/game", function (req, res) {
    axios.get(`${URL_BACKEND}game/play?user_action=${req.query.user_action}`)
        .then(response => {
            res.send(response.data)
        })
        .catch(error => {
            res.send(error)
        });
});

app.post("/api/post",jsonParser,  function (req, res) {
    axios.post(`${URL_BACKEND}post/add`, req.body)
        .then(response => {
            res.send(response.data)
        })
        .catch(error => {
            res.send(response.data)
        });
});

app.use("/game", (_, res) => {
    axios.get(`${URL_BACKEND}game/choice`)
        .then(response => {
            res.render("game.hbs", { title: "Игра", choices: response.data, });
        })
        .catch(error => {
            res.send(error)
        });
});

app.use("/add-post", (_, res) => {
    res.render("post.hbs", { title: "Добавить пост" });
});

app.use("/", (_, res) => {
    axios.get(`${URL_BACKEND}post/all`)
        .then(response => {
            res.render("main.hbs", { title: "Главная страница", posts: response.data });
        })
        .catch(error => {
            res.send(error)
        });
});

// начинаем прослушивать подключения на 3004 порту
app.listen(3004, () => {
    console.log("The frontend is running...")
});
