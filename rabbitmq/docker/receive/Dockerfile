FROM python:3
RUN pip install pika
WORKDIR /usr/src/app
COPY . .
CMD ["receive.py"]
ENTRYPOINT ["python3"]
