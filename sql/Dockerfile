FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE intelligence

RUN apt-get update
RUN apt-get install vim -y

COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

COPY ./data/ /tmp/
