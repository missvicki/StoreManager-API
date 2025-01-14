
FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app

RUN pip3 install -r requirements.txt

COPY . /usr/src/app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
