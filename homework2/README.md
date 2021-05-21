## Usage

### python:
start app:
`python app.py`

make request on running server:
`python make_request.py`

testing:
`pytest tests/`

### docker:

`docker login`

build:

`docker build -t lainer991/homework2:latest .`

run:

`docker run -p 8000:8000 lainer991/homework2:latest`

push:

`docker push lainer991/homework2:latest`

pull:

`docker pull lainer991/homework2:latest`

## Decreasing size

Для уменьшения размера образа был использован python-slim version, также в сервисе использовалась уже обученная модель, без пайплайна по ее созданию

## Self-review

|  |Task|Ball|
|---|-------------------------------------------------------------------------------------------------------------|:-------------:|
|1.|inference модели "обернут" в rest сервис с использованием FastAPI|3|
|2.|Написан тест для /predict|3|
|3.|Написан скрипт, который может делать запросы к сервису |2|
|4.|Валидация не делалась|0|
|5.|Написан dockerfile, на его основе собран образ|4|
|6.|Размер docker image оптимизирован|3|
|7.|Образ опубликован в https://hub.docker.com/|2|
|8.|В readme написаны корректные команды docker pull/run|1|
|9.|Проведена самооценка|1|
<br>
<br>
Итого 19 баллов.
<br>
<br>


