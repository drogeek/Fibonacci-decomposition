FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt ./
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt 
COPY . .
#ENV FLASK_APP web_serv.py
#ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE ${PORT} 

ENTRYPOINT /bin/sleep 5 && /usr/local/bin/gunicorn --access-logfile - --timeout ${TIMEOUT} -b ${IP_ADDR}:5000 web_serv:app
#CMD ["flask", "run"]
