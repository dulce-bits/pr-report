FROM python:3.10.12
ADD . .
RUN pip install -r requirements.txt
WORKDIR /script
RUN pwd && \
    # List files in the current directory
    ls -al
CMD ["python", "your_script.py", "7"]