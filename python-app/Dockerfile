FROM python:latest
RUN mkdir /app
WORKDIR /app

ADD . /app/
RUN pip install -r requerimets.txt
RUN export FLASK_APP=app.yp
EXPOSE 5000
CMD [ "python", "-m", "flask", "run", "--host", "0.0.0.0"]