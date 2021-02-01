FROM python:3
RUN pip install pika
WORKDIR /usr/src/app
COPY . .
CMD ["send.py"]
ENTRYPOINT ["python3"]
