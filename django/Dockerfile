FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /django
WORKDIR /django
ADD ../requirements.txt /django/


RUN pip install --upgrade pip && pip install -r requirements.txt && apt-get update && apt-get install -y gettext
WORKDIR /django/weird/
ENTRYPOINT ["/django/weird/entrypoint.sh", ""]