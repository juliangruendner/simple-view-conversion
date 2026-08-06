FROM python:latest

RUN apt update
RUN apt install -y openjdk-21-jdk-headless
RUN pip install pathling==9.8.0
RUN pip install pandas