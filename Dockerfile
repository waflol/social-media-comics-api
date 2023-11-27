FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /api

RUN sed -i 's/\r$//g' /api/scriptfiles/entrypoint.sh
RUN chmod +x /api/scriptfiles/entrypoint.sh

RUN sed -i 's/\r$//g' /api/scriptfiles/staging/build.sh
RUN chmod +x /api/scriptfiles/staging/build.sh

RUN sed -i 's/\r$//g' /api/scriptfiles/dev/build.sh
RUN chmod +x /api/scriptfiles/dev/build.sh

WORKDIR /api
ENTRYPOINT ["/api/scriptfiles/entrypoint.sh"]
