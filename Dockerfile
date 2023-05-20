FROM python:3.8
WORKDIR /api
COPY . . 
RUN pip install -r requirements.txt
CMD ["python3", "run.py"]
