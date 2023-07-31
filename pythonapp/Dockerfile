FROM python:3.9-slim 

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y libx11-6  tk-dev && rm -rf /var/lib/apt/lists/*

CMD ["python","main.py"]

