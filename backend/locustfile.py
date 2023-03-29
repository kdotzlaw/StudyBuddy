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
    creds = {'username': 'andrea22', 'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'}

    def on_start(self):
        creds = {'username': 'andrea22', 'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'}
        self.client.post("http://localhost:5000/api/login", json=creds)
    def on_stop(self):
        self.client.post("http://localhost:5000/api/logout")
    @task
    def getClasses(self):
        self.client.get("http://localhost:5000/api/class")

    @task
    def getTasks(self):
        self.client.get("http://localhost:5000/api/COMP 2080/task")

    @task
    def updateMeta(self):
        self.client.post("http://localhost:5000/api/class/COMP 2080/update_meta", json={"sectionnum": 1203})
    @task
    def editTask(self):
        self.client.post("http://localhost:5000/api/class/COMP 2080/task/Exam/edit",json={"newname":"Exam"})
        #self.client.post("http://localhost:5000/api/class/COMP 2080/task/Midterm/edit", json={"newname": "Exam"})

    @task
    def editClass(self):
        self.client.post("http://localhost:5000/api/class/COMP 2080/edit",json={"newname":"COMP 2080"})
    @task
    def getCompleteTasks(self):
        self.client.get("http://localhost:5000/api/class/COMP 2080/done_tasks")