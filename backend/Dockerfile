FROM python:3.11.0

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root

COPY . .

CMD ["python", "manage.py", "runserver", "0:8000"]