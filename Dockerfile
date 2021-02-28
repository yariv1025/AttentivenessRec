FROM python:3.8-slim-buster

WORKDIR /EmotionRec

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "./app.py"]
