FROM python:3.7-alpine3.10

RUN apk add --no-cache build-base libffi-dev openssl libressl-dev musl-dev postgresql-dev gcc python3-dev musl-dev
WORKDIR /app
ENV poetry=1.0.5
RUN pip3 install "poetry==$poetry"
COPY pyproject.toml poetry.lock ./
RUN poetry install
EXPOSE 8000
COPY . /app
COPY ewardrobe/ewardrobe/secrets.docker.json /app/ewardrobe/ewardrobe/secrets.json
WORKDIR /app/ewardrobe
CMD ./entrypoint.sh