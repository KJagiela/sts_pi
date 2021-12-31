FROM python:3.9-buster

ARG USER_ID=1000

ENV USER_ID=${USER_ID} \
  HOME=/home/sts \
  PYTHONUNBUFFERED=1 \
  FLASK_ENV=development

RUN apt-get update -qq \
  && apt-get install -qq -y \
    vim \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean -qq -y \
  && pip install --upgrade pip \
  && pip install poetry


# create the user and group to run the application as
RUN addgroup --system --gid ${USER_ID} sts \
  && adduser --system --home ${HOME} --uid ${USER_ID} --ingroup sts sts

CMD ["flask", "run", "--host=0.0.0.0"]

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml /app/

# Force `virtualenvs.create false` in case user update it in `pyproject.toml`
RUN cd /app && poetry config virtualenvs.create false \
  && poetry install \
    --no-interaction \
    --no-ansi

RUN chown -R sts /app /home/sts
USER sts
