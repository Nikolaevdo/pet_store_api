FROM python:3.10-slim

LABEL version="0.1"

WORKDIR /pet_store_api

COPY . /pet_store_api/
COPY poetry.lock  /pet_store_api/poetry.lock
COPY pyproject.toml /pet_store_api/pyproject.toml

RUN apt-get update

RUN pip install poetry

RUN apt-get install -y make

#RUN make install_dep
#RUN make build
RUN poetry install
RUN poetry build


CMD poetry run pet-store-api
