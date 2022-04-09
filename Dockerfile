

FROM python:3.6.1-alpine

WORKDIR /flask_web

ADD . /flask_web

RUN pip3 install -r requirements.txt

CMD [ "python3", "api.py" ]



