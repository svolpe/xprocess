import socketserver
import sys
import time


class EchoTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        data = self.rfile.readline().strip().decode('UTF-8')
        print('[ECHO SERVER] Received data: {}'.format(data))
        self.wfile.write('Echo: {}'.format(data).encode('UTF-8'))


def print_err(s):
    sys.stderr.write(s)
    sys.stderr.flush()


if __name__ == '__main__':

    default_port = 9998
    host, port = 'localhost', int(sys.argv[1]) if len(sys.argv) > 1 else default_port

    server = socketserver.TCPServer((host, port), EchoTCPHandler)
    print_err('Server starting...')

    startup_time = 3
    time.sleep(startup_time)

    print_err('Server startup completed!')
    server.serve_forever()
