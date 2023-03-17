# Create Python Flask Image
FROM python:3.11.1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD python ./server.py
