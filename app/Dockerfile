FROM python:latest

COPY . /clickstat

WORKDIR /clickstat

RUN pip install -r requirements.txt

CMD ["gunicorn","-w","4","-b","0.0.0.0:8000","app:app"]

EXPOSE 8000
