from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str("Hello from Python on Now 2.0!\n").encode())
        self.wfile.write(str("path: ").encode()+self.path.encode()+str("\n").encode())
        self.wfile.write(str("query string: ").encode()+urlparse(self.path).query.encode())
        return