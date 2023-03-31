#!/usr/bin/env bash
# Wait for database to start up
sleep 20s
./opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P dbtools.IO -i ./docker-entrypoint-initdb.d/StudyBuddy_create.sql