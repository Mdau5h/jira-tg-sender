FROM nexus-docker-hub.south.rt.ru/library/python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY Pipfile.lock Pipfile ./
RUN pip install -U pip -i https://nexus-pypi.south.rt.ru/repository/pypi-all/simple setuptools pipenv && pipenv install

COPY . .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]