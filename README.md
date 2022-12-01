# microservices-arc

Демострационный пример для лекции по микросервисной архитектуре

1. Приложение позволяет добавлять посты и просматривать все добавленные посты
2. Сыграть с компьютером в игру "Камень, ножницы, бумага" 
***
<h1><a href="https://arc-micro.deta.dev/">Демо</a></h1>

## Архитектура приложения

<img width="943" alt="image" src="https://user-images.githubusercontent.com/78900834/205141386-edcdd2b8-2ce3-4ef6-a686-7b742440435b.png">

## Как запустить

### 1. Установлен docker

1. После скачивания в корне проект запустить команду в консоли
> docker-compose up

Из <a href="https://hub.docker.com/repository/docker/vaynbaum/prj">из репозитория docker-hub</a> образы буду получены

или 

1. в docker-compose.yaml прописать
```docker
version: "3.6"

services:

  game:
    image: game
    restart: always
    networks:
      - microservices
    ports:
      - 3000:3000

  post:
    image: post
    restart: always
    networks:
      - microservices
    ports:
      - 3001:3001

  similarity:
    image: similarity
    restart: always
    networks:
      - microservices
    ports:
      - 3002:3002
  
  gateway:
    image: gateway
    restart: always
    networks:
      - microservices
    ports:
      - 3003:3003

  frontend:
    image: frontend
    restart: always
    networks:
      - microservices
    ports:
      - 3004:3004
networks:
    microservices:
```

2. В директории `./frontend` в консоли ввести
> docker build -t frontend .

3. В директории `./backend/game` в консоли ввести
> docker build -t game .

4. В директории `./backend/gateway` в консоли ввести
> docker build -t gateway .

5. В директории `./backend/chain/post` в консоли ввести
> docker build -t post .

6. В директории `./backend/chain/similarity` в консоли ввести
> docker build -t similarity .

7. После создания образов в корне проекта в консоли ввести команду 
> docker-compose up
