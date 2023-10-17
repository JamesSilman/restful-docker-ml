FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --upgrade pip

RUN apt-get update
RUN apt-get install vim -y

RUN pip install cmake

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app/. /app
