FROM alpine:3.20.0
ADD . .
RUN apk add --no-cache python3 py3-pip
RUN pip install -r requirements.txt
WORKDIR /script
RUN python script.py 7