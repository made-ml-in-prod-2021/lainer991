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

To size decrease used python-slim version

## Self-review

|  |Task|Ball|
|---|-------------------------------------------------------------------------------------------------------------|:-------------:|
|1.|inference with FastAPI|3|
|2.|test for /predict|3|
|3.|Was build script for server requests|2|
|4.|No validation|0|
|5.|Was build docker container |4|
|6.|Docker image was decreased by python-slim version|3|
|7.|Docker image pushed to https://hub.docker.com/|2|
|8.|In readme there is commands for docker pull/run|1|
|9.|Self-review done|1|
<br>
<br>
Overall 19 points
<br>
<br>


