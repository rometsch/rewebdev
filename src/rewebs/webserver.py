""" Local development web server. """

import http.server
import os
import threading
import socket
import errno

def is_port_free(port):
    """ Check whether the port is free to use on localhost.

    Parameters
    ----------
    port: int
        Port number to check.

    Returns
    -------
    bool:
        True if free, false if already in use.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind(("127.0.0.1", port))
        rv = True
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            rv = False
        else:
            # something else raised the socket.error exception
            raise

    s.close()

    return rv

def get_next_free_port(port):
    """ Find the next free port on localhost.
    
    Recursively test all port numbers with increments of 1 
    starting from number 'port'.
    
    Parameters
    ----------
    port: int
        Start looking from this port number upwards.
        
    Returns
    -------
    int
        Next free port number.
    """
    if is_port_free(port):
        return port
    else:
        return get_next_free_port(port + 1)

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


def start_server(path):
    """ Start the simple http server in the background. 

    Parameter
    ---------
    path: str
        Path to the directory to be served.
    """
    port = get_next_free_port(8000)
    server_thread = threading.Thread(
        target=start_server_foreground, args=[path, port])
    server_thread.start()
    return port


if __name__ == "__main__":
    start_server(os.getcwd())
