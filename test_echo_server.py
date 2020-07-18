import socket
import sys

import py
import pytest
from xprocess import ProcessStarter

server_name = 'echo-server'
hostname, port = 'localhost', 6777
#test

@pytest.fixture(autouse=True)
def start_server(xprocess):
    python_executable_full_path = sys.executable
    python_server_script_full_path = py.path.local(__file__).dirpath("echo_server.py")

    class Starter(ProcessStarter):
        pattern = 'completed'
        args = [python_executable_full_path, python_server_script_full_path, str(port)]

    xprocess.ensure(server_name, Starter)

    yield
    
    xprocess.getinfo(server_name).terminate()


def test_echo_server():
    buffer_size = 4096

    sock = socket.socket()
    sock.connect((hostname, port))
    sock.sendall('hello\n'.encode('utf8'))
    c = sock.recv(buffer_size)
    assert c == 'Echo: hello'.encode('utf8')
