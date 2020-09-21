FROM mysql:5.7
COPY ./Create.sql /docker-entrypoint-initdb.d
EXPOSE 3306
ENV MYSQL_ROOT_PASSWORD=password
