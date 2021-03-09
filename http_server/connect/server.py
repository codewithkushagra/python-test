from http.server import HTTPServer, BaseHTTPRequestHandler


class clientserver(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path =='/':
            self.path='/serverpage.html'
        try:
            file_to_open=open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open="File does not exist"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open,'utf-8'))
httpd=HTTPServer(('localhost', 5050),clientserver)
httpd.serve_forever()


