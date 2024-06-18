FROM python:3.10.14-alpine3.20

WORKDIR /usr/src/myproject

COPY requirements.txt .

RUN PIP INSTALL --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 5100

CMD ["python3", "manage.py", "runserver"]
