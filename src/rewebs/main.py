""" Setup a web dev server, start a browser and refresh when a file is saved.

Inspired by
https://sakthipriyan.com/2016/02/15/auto-refresh-chrome-when-files-modified.html

Licence: AGPL-3.0
"""

import os
import time
from rewebs.webserver import start_server
from rewebs.browser import refresh_browser, start_browser
from rewebs.monitor import monitor


def cb(port=8000):
    """ Callback function. """
    refresh_browser(port)


def main():
    my_directory = os.getcwd()

    port = start_server(my_directory)
    start_browser(port)
    time.sleep(2)
    monitor(my_directory, lambda : cb(port=port))


if __name__ == "__main__":
    main()
