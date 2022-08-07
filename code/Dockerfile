# syntax=docker/dockerfile:1

FROM python:latest

WORKDIR /app
ENV FLASK_APP app.py

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install flask-mysqldb

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]