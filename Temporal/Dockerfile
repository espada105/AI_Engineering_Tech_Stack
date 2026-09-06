FROM python:3.13-slim AS builder
WORKDIR /workspace
COPY --from=ghcr.io/astral-sh/uv:0.8.17 /uv /uvx /bin/
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

FROM python:3.13-slim
WORKDIR /workspace
COPY --from=builder /bin/uv /bin/uv
COPY --from=builder /bin/uvx /bin/uvx
COPY --from=builder /workspace/.venv /workspace/.venv

COPY app/ /workspace/app/

ENV PATH="/workspace/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "app.main"]
