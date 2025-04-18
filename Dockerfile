FROM python:3.9.6-alpine3.14

#WORKDIR /app

RUN pip install python-telegram-bot
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

