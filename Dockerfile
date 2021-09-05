FROM python:3.9-slim

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --ignore-pipfile --deploy

COPY src /app/src/

ENTRYPOINT ["python", "src/main.py"]
