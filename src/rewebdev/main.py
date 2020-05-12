""" Setup a web dev server, start a browser and refresh when a file is saved.

Inspired by
https://sakthipriyan.com/2016/02/15/auto-refresh-chrome-when-files-modified.html

Licence: AGPL-3.0
"""

import os
from rewebdev.webserver import start_server
from rewebdev.browser import refresh_browser, start_browser
from rewebdev.monitor import monitor


def cb():
    """ Callback function. """
    refresh_browser()

def main():
    my_directory = os.getcwd()

    start_server(my_directory)
    start_browser()
    monitor(my_directory, cb)


if __name__ == "__main__":
    main()
