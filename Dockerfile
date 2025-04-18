FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install python-telegram-bot

# Expose the port your app will run on
EXPOSE 8443

CMD ["python", "bot.py"]



