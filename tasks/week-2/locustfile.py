import os
from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def get_time(self):
        self.client.get("/time")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  

# if __name__ == "__main__":
#     import os
#     os.system('locust -f locustfile.py --host=http://pytime.local:30371/')
