FROM python:3.8-slim

WORKDIR /app

COPY backend/req.txt .
RUN pip install  -r req.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]