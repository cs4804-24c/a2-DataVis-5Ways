from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # send 200 response
        self.send_response(200)

        # send response headers
        self.send_header('Access-Control-Allow-Origin', '*')

        self.end_headers()

        if self.path == "/penglings.csv": # 
            # send the body of the response
            with open("penglings.csv", "rb") as f:
                self.wfile.write(f.read())

        self.wfile.write(bytes("It Works!", "utf-8"))





httpd = HTTPServer(('localhost', 8000), MyHandler)
httpd.serve_forever()