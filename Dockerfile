FROM python:3.6-jessie

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd -r uwsgi && useradd -r -u 1000 -g uwsgi uwsgi
RUN chown -R uwsgi .
USER uwsgi

EXPOSE 8080 8888

CMD ["uwsgi", "-L", "--socket", "0.0.0.0:8080", "--module", "QnA.wsgi", "--master", "--processes", "2", "--threads", "2", "--max-requests", "250"]