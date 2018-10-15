FROM python:3.5
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
#RUN apt-get update
#RUN apt-get install python3.5-dev
RUN pip install Flask==0.10.1 uWSGI==2.0.15 requests==2.5.1 redis==2.10.3
WORKDIR /app
COPY app /app
COPY cmd.sh /
EXPOSE 9090 9191
USER uwsgi
CMD ["/cmd.sh"]
