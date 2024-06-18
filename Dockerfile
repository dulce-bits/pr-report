FROM python:3.10.12-alpine3.18
ADD . .
RUN pip install -r requirements.txt
WORKDIR /script
RUN pwd && \
    # List files in the current directory
    ls -al
CMD ["python", "your_script.py", "7"]