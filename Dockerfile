FROM python:3.13
WORKDIR /app

ADD pyproject.toml /app/pyproject.toml

RUN pip install uv
RUN uv venv
RUN uv pip install .
RUN uv pip install bcrypt
RUN uv pip install "passlib[bcrypt]"
COPY ./ /app

EXPOSE 8000

CMD ["uv", "run", "main.py"]
