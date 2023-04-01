# Create Python Flask Image
FROM python:3.11.1
WORKDIR /app/backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Install ODBC Driver 17
RUN apt-get install curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN apt-get install -y unixodbc

EXPOSE 5000
CMD python3 -m flask --app server.py run --host=0.0.0.0 -p 5000
