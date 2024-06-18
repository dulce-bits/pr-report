FROM alpine:3.20.0
ADD . .
RUN apk update && \
    apk add --no-cache python3 py3-pip && \
    pip3 install --upgrade pip setuptools

RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /script
RUN python script.py 7