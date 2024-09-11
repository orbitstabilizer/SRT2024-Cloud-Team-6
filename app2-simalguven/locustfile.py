from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def load_frontend(self):
        self.client.get("/")

    @task
    def load_backend(self):
        self.client.get("/api/message")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)

