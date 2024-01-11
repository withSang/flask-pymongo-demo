FROM python:3.11.4-slim-bullseye as prod

# Copying requirements of a project
WORKDIR /app/src
COPY requirements.txt /app/src/

# Installing requirements
RUN pip install -r requirements.txt

# Copying actuall application
COPY . /app/src/

CMD ["gunicorn", "-b", "0.0.0.0:8080", "server:app", "-k", "gevent"]