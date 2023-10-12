FROM python:3.11-slim-buster

RUN useradd -ms /bin/bash api
USER api

WORKDIR /api
RUN pip install poetry==1.6.1
ENV PATH=/home/api/.local/bin:${PATH}
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . ./
ENV PYTHONPATH "${PYTHONPATH}:/api/src"

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
