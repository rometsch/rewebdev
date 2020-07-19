""" Monitor a directory and call a callback function on save events.

Taken from 
https://sakthipriyan.com/2016/02/15/auto-refresh-chrome-when-files-modified.html.

Licence: APACHE LICENSE, VERSION 2.0
"""

import asyncore

import pyinotify

import os

mask = pyinotify.IN_DELETE | pyinotify.IN_CLOSE_WRITE


class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, fn, *args, **kwargs):
        super(EventHandler, self).__init__(*args, **kwargs)
        self.function = fn

    def process_IN_DELETE(self, event):
        self.function()

    def process_IN_CLOSE_WRITE(self, event):
        self.function()

def exclude_filter(x):
    """ A filter to exclude hidden directories. """
    parts = os.path.normpath(x).lstrip(os.path.sep).split(os.path.sep)
    rv = any((s[0] == "." for s in parts))
    return rv

def monitor(directory, callback):
    """ Monitor a directory and call callback on selected events. """
    wm = pyinotify.WatchManager()
    # rec=True, to monitor all sub directories recursively.
    # auto_add=True, to monitor added new sub directories.        
    wm.add_watch(directory, mask, rec=True, auto_add=True, exclude_filter=exclude_filter)
    # specify the event handler to process the events.
    pyinotify.AsyncNotifier(wm, EventHandler(callback))
    # start the asyncore loop to monitor and process events.
    asyncore.loop()
