FROM ghcr.io/astral-sh/uv:0.11.32 AS uv

FROM python:3.12-slim

COPY --from=uv /uv /uvx /usr/local/bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PROJECT_ENVIRONMENT=/opt/venv

WORKDIR /workspace

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

COPY main.py README.md ./

CMD ["uv", "run", "--locked", "main.py"]
