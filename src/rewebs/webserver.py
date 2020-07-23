""" Local development web server. """

import http.server
import os
import threading
import socket
import multiprocessing
from .ports import get_next_free_port

browser_port = get_next_free_port(8000)


def start_server_foreground(path, port, handler_class=http.server.SimpleHTTPRequestHandler):
    """ Start a simple http server restricted to local host.

    Parameter
    ---------
    path: str
        Path to the directory to be served.
    port: int
        Port number to serve on.
    """
    os.chdir(path)

    bind = "127.0.0.1"
    http.server.test(HandlerClass=handler_class, port=port, bind=bind)


def start_server(path, port):
    """ Start the simple http server in the background. 

    Parameter
    ---------
    path: str
        Path to the directory to be served.
    """
    p = multiprocessing.Process(
        target=start_server_foreground, args=[path, port])
    p.start()
    return p

if __name__ == "__main__":
    start_server(os.getcwd(), browser_port)
