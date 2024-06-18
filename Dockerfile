FROM python:3.10.12
ADD . .
RUN pip install -r requirements.txt
WORKDIR /script
CMD ["python", "script.py", "7"]