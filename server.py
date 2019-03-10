from http.server import HTTPServer, BaseHTTPRequestHandler
import json

host = ('localhost', 2299)

class Resquest(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        datas = self.rfile.read(int(self.headers['content-length']))
        datas = datas.decode()
        sentence = json.loads(datas)['sentence']

        print(sentence)
        self.wfile.write(json.dumps(sentence, ensure_ascii=False).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()

