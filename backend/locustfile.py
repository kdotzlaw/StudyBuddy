from locust import HttpUser, task, between
'''
1. pip install locust
2. run flask server:  python3 -m flask --app server.py run
3. In backend directory: python -m locust
4. Visit: http://localhost:8089/
'''
class WebsiteTestUser(HttpUser):
    wait_time = between(0.5,3)
    creds = {'username': 'ryan2023', 'password': 'password'}

    def on_start(self):
        #authentication done here -- login
        creds = {'username': 'ryan2023', 'password': 'password'}
        self.client.post("http://localhost:5000/api/login", json=creds)
        #pass
    def on_stop(self):
        #logout done here??
        self.client.post("http://localhost:5000/api/logout")
        #pass
    @task
    def getClasses(self):
        self.client.get("http://localhost:5000/api/class")

