FROM python:3.13-bookworm

ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install -y gcc libpq-dev ghostscript

WORKDIR /app


COPY backend/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

