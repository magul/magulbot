FROM python:3

MAINTAINER Tomasz Magulski <tomasz@magul.ski>

WORKDIR /magulbot

RUN groupadd -r magulbot && useradd -r -g magulbot magulbot

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./magulbot /magulbot

RUN chown -R magulbot:magulbot /magulbot
USER magulbot

EXPOSE 8000
