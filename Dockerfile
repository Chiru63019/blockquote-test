FROM python:3.9.6-alpine3.14

WORKDIR /app

RUN pip install python-telegram-bot

CMD python3 bot.py
