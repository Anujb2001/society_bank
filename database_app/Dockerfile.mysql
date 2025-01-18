# Dockerfile for MySQL
FROM mysql:8.0

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=transactions_db

# Expose MySQL port
EXPOSE 3306

COPY init.sql /docker-entrypoint-initdb.d/

