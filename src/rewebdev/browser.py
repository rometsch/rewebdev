""" Start and communicate with a chromium browser instance.

Taken from 
https://sakthipriyan.com/2016/02/15/auto-refresh-chrome-when-files-modified.html
and modified to use chromium-browser.

Licence: APACHE LICENSE, VERSION 2.0
"""

import json
import os
import subprocess
import threading

import requests
from websocket import create_connection

chrome_port = 9222
chrome_json_url = 'http://localhost:%s/json' % (chrome_port)
refresh_json = json.dumps({
    "id": 0,
    "method": "Page.reload",
    "params": {"ignoreCache": True}
})


def open_browser(url):
    # directory is used by chromium browser to store profile for this remote user.
    directory = os.path.expanduser('~/.chrome-remote-profile')
    command = 'chromium-browser --remote-debugging-port=%d --user-data-dir=%s %s' % \
        (chrome_port, directory, url)
    subprocess.call(command, shell=True)


def refresh_browser():
    # get response for the GET request.
    response = requests.get(chrome_json_url)
    # Process each item in the response.
    for page in response.json():
        # only if it is a page and interested urls.
        if page['type'] == 'page' and 'localhost:8000' in page['url']:
            # Open websocket connection, send json and close it.
            # This will refresh this specific tab.
            ws = create_connection(page['webSocketDebuggerUrl'])
            ws.send(refresh_json)
            ws.close()


def start_browser():
    # Browser is launched via a daemon thread.
    # It will terminate the browser when you close the python script.
    thread = threading.Thread(target=open_browser, kwargs={
                              'url': 'http://localhost:8000'})
    thread.daemon = True
    thread.start()
