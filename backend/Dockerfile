FROM python:3.8-slim

WORKDIR /back

COPY req.txt .

RUN pip install  -r req.txt

COPY . .

CMD ["ls"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
