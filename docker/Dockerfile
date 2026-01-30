FROM python:3.12-slim

WORKDIR /app

# I got an error without it
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libxcb1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY src/requirements.txt .

RUN uv pip install --system --no-cache-dir -r requirements.txt

COPY src/ .

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]
