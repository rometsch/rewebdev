""" Setup a web dev server, start a browser and refresh when a file is saved.

Inspired by
https://sakthipriyan.com/2016/02/15/auto-refresh-chrome-when-files-modified.html

Licence: AGPL-3.0
"""

import os
import sys
import time
from rewebs.webserver import start_server
from rewebs.browser import refresh_browser, start_browser, get_page_opened
from rewebs.monitor import start_monitor

from .ports import get_next_free_port

def main():
    my_directory = os.getcwd()

    html_port = get_next_free_port(8000)
    server_process = start_server(my_directory, html_port)
    
    browser_process = start_browser(html_port)
    time.sleep(2)

    def cb():
        refresh_browser(html_port)

    monitor_process = start_monitor(my_directory, cb)

    while True:
        time.sleep(1)
        while True:
            if get_page_opened(html_port) is not None:
                time.sleep(0.5)
            else:
                browser_process.terminate()
                server_process.terminate()
                monitor_process.terminate()
                sys.exit(0)

if __name__ == "__main__":
    main()
