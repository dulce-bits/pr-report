FROM python:3.9 
ADD ./script .
RUN pip install -r requirements.txt
CMD [“python”, “./script.py”] 
