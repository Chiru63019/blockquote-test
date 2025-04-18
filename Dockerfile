FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install python-telegram-bot

CMD ["python", "bot.py"]


