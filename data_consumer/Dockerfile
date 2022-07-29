FROM python:3.8-slim as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps

RUN apt-get update 
RUN apt-get -y upgrade 
RUN apt-get -y install --no-install-recommends gcc 
RUN pip install --upgrade pip 
RUN pip install pipenv

COPY data_consumer/Pipfile .
COPY data_consumer/Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

RUN useradd --create-home appuser
USER appuser

COPY data_consumer/app.py ./app.py
COPY data_consumer/example.log ./example.log
COPY data_consumer/.env ./example.log

CMD ["python3", "app.py"]