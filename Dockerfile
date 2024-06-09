FROM python:3.8
WORKDIR /app

ADD pyproject.toml /app/pyproject.toml

RUN pip install poetry
RUN poetry install

COPY ./ /app

EXPOSE 8000

CMD ["poetry", "run", "fastapi", "run", "app.py"]
