FROM python:3.10.12
ADD . .
RUN pip install -r requirements.txt
WORKDIR script
RUN python script.py 7