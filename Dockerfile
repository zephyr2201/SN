FROM python:3.9-slim
WORKDIR /code

# set env
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN apt-get update
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /code/


