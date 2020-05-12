""" Local development web server. """

import http.server
import os
import threading


def start_server_foreground(path, handler_class=http.server.SimpleHTTPRequestHandler):
    """ Start a simple http server restricted to local host.

    Parameter
    ---------
    path: str
        Path to the directory to be served.
    """
    os.chdir(path)

    port = 8000
    bind = "127.0.0.1"
    http.server.test(HandlerClass=handler_class, port=port, bind=bind)


def start_server(path):
    """ Start the simple http server in the background. 

    Parameter
    ---------
    path: str
        Path to the directory to be served.
    """
    server_thread = threading.Thread(
        target=start_server_foreground, args=[path])
    server_thread.start()


if __name__ == "__main__":
    start_server(os.getcwd())
