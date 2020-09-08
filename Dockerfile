FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt 
COPY . .
ENV FLASK_APP web_serv.py
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000

CMD ["flask", "run"]
