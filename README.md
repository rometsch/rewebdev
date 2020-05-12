# rewebdev

A simple python webdev server which also starts chromium and reloads the page on file change.

## Rational

[reveal.js](https://github.com/hakimel/reveal.js/) is awesome! While using it, I really like to see changes as I go.
So I need the webpage to automatically reload when I hit ctrl + s.
This package solves exactly this problem.

## How to run

Run `rewebdev` inside a directory containing an `index.html`.
Chromium should launch in debug mode and your index page should be served.

## How to install

Run `python3 setup.py install --user` to install the package and all its dependencies on your system.

You'll then have access to the python library (check out the 3 files for browser, webserver and file monitor support) and, most importantly, the `rewebdev` command.

## Limitations

This package was tested on Ubuntu 18.04 in May 2020.
No guarantee that it works anywhere else.

## LICENSE

This work is licensed under AGPL-3.0.
Some file are under the Apache v2.0 license, if indicated in the header of the file.
