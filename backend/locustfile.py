from locust import HttpUser, task, between
'''
1. pip install locust
2. run flask server:  python3 -m flask --app server.py run
3. In backend directory: python -m locust
4. Visit: http://localhost:8089/
'''

'''
Perfoms a load test for login user, get all classes, logout user
'''
class WebsiteTestUser(HttpUser):
    wait_time = between(0.5,3)
    creds = {'username': 'ryan2023', 'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'}

    def on_start(self):
        creds = {'username': 'ryan2023', 'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'}
        self.client.post("http://localhost:5000/api/login", json=creds)
    def on_stop(self):
        self.client.post("http://localhost:5000/api/logout")
    @task
    def getClasses(self):
        self.client.get("http://localhost:5000/api/class")

