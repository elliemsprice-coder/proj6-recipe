FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend /app/backend
COPY frontend /app/frontend
COPY credentials.ini /app/credentials.ini

ENV PYTHONPATH=/app/backend

EXPOSE 5000

CMD ["python", "backend/app.py"]