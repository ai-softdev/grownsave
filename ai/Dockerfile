FROM python:3.12

WORKDIR /ai

COPY ai/req.txt .

RUN pip install -r req.txt

COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 --forwarded-allow-ips='*'
