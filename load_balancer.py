from flask import Flask, request
import requests
import threading
import random
import time

app = Flask(__name__)

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.failed_servers = set()
        self.lock = threading.Lock()
        self.health_check_interval = 30  # Health check interval in seconds
        self.current_index = 0

        # Start health check background task
        health_check_thread = threading.Thread(target=self.health_check, daemon=True)
        health_check_thread.start()

    def send_request(self, path):
        server = self.select_server()
        if server is None:
            return "No healthy servers available"

        url = f"http://{server}{path}"
        try:
            response = requests.get(url)
            return response.text
        except requests.exceptions.RequestException as e:
            self.handle_failure(server)
            return f"Error occurred while sending request: {e}"

    def select_server(self):
        with self.lock:
            if not self.servers:
                return None

            # Simple round-robin load balancing
            server = self.servers[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.servers)
            return server

    def health_check(self):
        while True:
            time.sleep(self.health_check_interval)
            for server in self.servers.copy():
                url = f"http://{server}/health-check"
                try:
                    response = requests.get(url)
                    if response.status_code != 200:
                        self.handle_failure(server)
                    else:
                        self.handle_recovery(server)
                except requests.exceptions.RequestException:
                    self.handle_failure(server)

    def handle_failure(self, server):
        print(f"Server {server} is down. Marking as failed.")
        with self.lock:
            self.servers.remove(server)
            self.failed_servers.add(server)

    def handle_recovery(self, server):
        print(f"Server {server} is back online. Marking as healthy.")
        with self.lock:
            self.failed_servers.discard(server)
            if server not in self.servers:
                self.servers.append(server)

servers = ["server1.com", "server2.com", "server3.com"]
load_balancer = LoadBalancer(servers)

@app.route('/')
def index():
    return load_balancer.send_request(request.path)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
