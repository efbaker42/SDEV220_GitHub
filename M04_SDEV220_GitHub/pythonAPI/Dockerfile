FROM python:3.11.3

WORKDIR /docker_test

COPY . .

RUN pip install -r requirements.txt

CMD["python", "./app.py"]