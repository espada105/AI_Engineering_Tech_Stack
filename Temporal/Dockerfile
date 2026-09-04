FROM python:3.13-slim AS builder
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:0.8.17 /uv /uvx /bin/
COPY pyproject.toml.uv.lock ./
RUN uv sync --locked --no-dev

FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /bin/uv /bin/uv
COPY --from=builder /bin/uvx /bin/uvx
COPY --from=builder /app/.venv /app/.venv

COPY src/ /app/src/

ENV PATH = "/app/.venv/bin:$PATH"
ENV PYTHONPATH = "/app/src"
ENV PyTHONUNBUFFERED=1

CMD ["python", "-m", "temporal_study.worker"]