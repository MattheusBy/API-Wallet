FROM python:3.8.2

# Configure Poetry
ENV POETRY_VERSION=1.3.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache
# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-ansi

COPY . /app

EXPOSE 5432 6379
# Run your app
ENTRYPOINT poetry run gunicorn drf_wallet.wsgi:application --bind 0.0.0.0:8000

