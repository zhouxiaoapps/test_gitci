FROM python:3.7

ADD . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt

#EXPOSE 5000/tcp

ENV FLASK_APP="/app/run.py"

CMD ["flask", "run", "--host=0.0.0.0"]