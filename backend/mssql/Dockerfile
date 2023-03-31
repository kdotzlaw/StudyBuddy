# Create MSSQL Image and Initialize Data
FROM mcr.microsoft.com/mssql/server:2022-latest
EXPOSE 1433
ENV ACCEPT_EULA=Y
ENV MSSQL_SA_PASSWORD=dbtools.IO

COPY ./StudyBuddy_create.sql /docker-entrypoint-initdb.d/
COPY ./setup_database.sh /docker-entrypoint-initdb.d/
COPY ./entrypoint.sh /docker-entrypoint-initdb.d/
RUN ./opt/mssql/bin/sqlservr & ./docker-entrypoint-initdb.d/setup_database.sh