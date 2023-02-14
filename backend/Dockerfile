# Create Python Image
FROM python:3.11.1
WORKDIR /app
COPY . ./
RUN pip install -r requirements.txt
# EXPOSE 3000
CMD python ./index.py
ADD main.py
