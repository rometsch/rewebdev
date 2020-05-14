""" Monitor a directory and call a callback function on save events.

Taken from 
https://sakthipriyan.com/2016/02/15/auto-refresh-chrome-when-files-modified.html.

Licence: APACHE LICENSE, VERSION 2.0
"""

import asyncore

import pyinotify

mask = pyinotify.IN_DELETE | pyinotify.IN_CLOSE_WRITE


class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, fn, *args, **kwargs):
        super(EventHandler, self).__init__(*args, **kwargs)
        self.function = fn

    def process_IN_DELETE(self, event):
        self.function()

    def process_IN_CLOSE_WRITE(self, event):
        self.function()


def monitor(directory, callback):
    """ Monitor a directory and call callback on selected events. """
    wm = pyinotify.WatchManager()
    # rec=True, to monitor all sub directories recursively.
    # auto_add=True, to monitor added new sub directories.
    wm.add_watch(directory, mask, rec=True, auto_add=True)
    # specify the event handler to process the events.
    pyinotify.AsyncNotifier(wm, EventHandler(callback))
    # start the asyncore loop to monitor and process events.
    asyncore.loop()
