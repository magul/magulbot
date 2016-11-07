FROM python:3

MAINTAINER Tomasz Magulski <tomasz@magul.ski>

WORKDIR /magulbot

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./magulbot /magulbot

EXPOSE 8000
