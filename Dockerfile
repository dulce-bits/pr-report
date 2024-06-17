FROM python:3.10.14-alpine3.20
ADD . .
RUN pip install -r requirements.txt
WORKDIR script
RUN python script.py