from http.server import BaseHTTPRequestHandler, HTTPServer
from Test_Api import API
class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self,response=""):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print(response)
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data_str = post_data.decode('utf-8')


        start_index = post_data_str.find(':"') + 2
        end_index = post_data_str.rfind('"')


        value = post_data_str[start_index:end_index]

        Test = API(value)
        self.do_GET(Test.talk())


httpd = HTTPServer(('localhost', 1000), RequestHandler)
print("Serving at port", 1000)
httpd.serve_forever()
