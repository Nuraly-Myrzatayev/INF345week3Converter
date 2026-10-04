import os
from http.server import BaseHTTPRequestHandler, HTTPServer

celsius = 10

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self._send(200, b"ok")
        elif self.path == "/":
            self._send(200, b"Celsius to Fahrenheit converter")
        elif self.path == "/converter":
            self._send(200, str(f"{celsius} celsius is {(celsius * 1.8) + 32} fahrenheit").encode())
        else:
            self._send(404, b"not found")

    def _send(self, code, body):
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass

def make_server(port):
    return HTTPServer(("0.0.0.0", port), Handler)

if __name__ == "__main__":
    make_server(int(os.environ.get("PORT", "8080"))).serve_forever()
