FROM python:3.13-slim-bookworm

RUN useradd -ms /bin/bash api
USER api

WORKDIR /api
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV PATH=/home/api/.local/bin:${PATH}
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY . ./
ENV PYTHONPATH "${PYTHONPATH}:/api/src"

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
