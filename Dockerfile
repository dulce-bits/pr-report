FROM python:3.10.14-alpine3.20
ADD . .
RUN pip install -r requirements.txt
CMD [“python”, “./script.py”]