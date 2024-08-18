
"""
This is a simple HTTP server that serves the current time in seconds since the epoch
Server:
    Host: localhost
    Port: 8080
Endpoint:
    GET /time
"""

import http
from http.server import HTTPServer, SimpleHTTPRequestHandler

from time import time
import json


def get_current_time():
    return {"time": time()}

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/time':
            self.send_response(http.HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(json.dumps(get_current_time()).encode())
        else:
            super().do_GET()


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), Handler)
    print("serving at 127.0.0.1:8080")
    server.serve_forever()

