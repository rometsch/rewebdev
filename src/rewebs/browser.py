""" Start and communicate with a chromium browser instance.

Taken from 
https://sakthipriyan.com/2016/02/15/auto-refresh-chrome-when-files-modified.html
and modified to use chromium-browser.

Licence: APACHE LICENSE, VERSION 2.0
"""

import json
import os
import sys
import subprocess
import threading
import multiprocessing
import tempfile

import requests
from websocket import create_connection

from .ports import get_next_free_port


chrome_port = get_next_free_port(9222)
chrome_json_url = 'http://localhost:%s/json' % (chrome_port)
refresh_json = json.dumps({
    "id": 0,
    "method": "Page.reload",
    "params": {"ignoreCache": True}
})


def open_browser(url):
    # directory is used by chromium browser to store profile for this remote user.
    tempdir = tempfile.TemporaryDirectory()
    directory = os.path.join(tempdir.name, 'chrome-remote-debuggin-profile')
    command = 'chromium --new-window --remote-debugging-port={} --user-data-dir={} {}'.format(chrome_port, directory, url)
    subprocess.call(command, shell=True)


def get_page_opened(port):
    rv = None
    # get response for the GET request.
    try:
        response = requests.get(chrome_json_url, timeout=0.1)
    except Exception as e:
        return None
    # Process each item in the response.
    for page in response.json():
        # only if it is a page and interested urls.
        if page['type'] == 'page' and f"localhost:{port}" in page['url']:
            rv = page
            break
    return rv

def refresh_browser(port):
    # get response for the GET request.
    page = get_page_opened(port)
    if page is not None:
        # Open websocket connection, send json and close it.
        # This will refresh this specific tab.
        ws = create_connection(page['webSocketDebuggerUrl'])
        ws.send(refresh_json)
        ws.close()


def start_browser(port):
    # Browser is launched via a daemon thread.
    # It will terminate the browser when you close the python script.
    try:
        p = multiprocessing.Process(target=open_browser, kwargs={
            "url": f"http://localhost:{port}"})
        p.start()
    except OSError:
        print("caught the error")
        sys.exit(1)
    return p

