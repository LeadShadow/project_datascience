FROM python:3.9

WORKDIR  /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
RUN chmod +x run.sh
CMD ["./run.sh"]