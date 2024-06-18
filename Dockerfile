FROM alpine:3.20.0
ADD . .
RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt
WORKDIR /script
RUN python script.py 7