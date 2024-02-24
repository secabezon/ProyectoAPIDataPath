
FROM tiangolo/uvicorn-gunicorn:python3.8-slim AS pythonimage

WORKDIR /app

COPY . .

RUN pip install -r requeriments.txt


ENV PORT=8080
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80", "--worker-class", "uvicorn.workers.UvicornWorker"]
