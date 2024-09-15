import random
from locust import HttpUser, task, between
url_prefix="http://192.168.0.32:30080"

class MessageAPIUser(HttpUser):
    # wait_time = between(2, 5)  # Longer wait time for low load --users 10 --spawn-rate 1
    # wait_time = between(0.5, 2)  # Moderate wait time for medium load--users 100 --spawn-rate 10
    wait_time = between(0.1, 0.5)  # Minimal wait time for high load  --users 500 --spawn-rate 50
    @task(1)
    def rapid_requests(self):
        self.client.get("frontend")
        a = self.client.get("backend/api/messages")
        id = len(a.text.split("},{"))
        new_message = {"text": f"Stress test message {id}"}
        self.client.post("backend/api/messages", json=new_message)
        self.client.get("backend/api/messages")
        self.client.delete(f"backend/api/messages/last")
        self.client.get("backend/api/messages")