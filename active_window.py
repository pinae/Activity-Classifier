#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import PIPE, Popen
import re


def get_active_window_title():
    root = Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=PIPE)
    stdout, stderr = root.communicate()
    m = re.search(b"^_NET_ACTIVE_WINDOW.* ([\w]+)$", stdout)
    if m is not None:
        window_id = m.group(1)
        window = Popen(['xprop', '-id', window_id, 'WM_NAME'], stdout=PIPE)
        stdout, stderr = window.communicate()
    else:
        return None
    match = re.match(b"WM_NAME\(\w+\) = (?P<name>.+)$", stdout)
    if match is not None:
        return window_id, match.group("name").strip(b'"')
    return None


if __name__ == "__main__":
    import time
    time.sleep(5)
    print(get_active_window_title())
