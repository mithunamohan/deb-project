FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

EXPOSE 8000

# Install the application dependencies.
WORKDIR /app
# Ensure uv is up to date
RUN uv venv
RUN uv pip install --upgrade uv

# Manually install motor
RUN uv pip install motor

# Run the dependency sync
RUN uv sync --frozen --no-cache

# Run the application.
CMD ["/app/.venv/bin/uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]

