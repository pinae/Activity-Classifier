#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import PIPE, Popen
import re
wlp = re.compile(b"^(0x[\da-f]+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.+)$")


def get_list_of_open_windows():
    win_list = []
    root = Popen(['wmctrl', '-p', '-G', '-l'], stdout=PIPE)
    stdout, stderr = root.communicate()
    lines = stdout.split(b"\n")
    for line in lines:
        matches = wlp.match(line)
        if matches:
            win_id, destop_no, pid, x, y, width, height, name = matches.groups()
            win_list.append({
                'name': name,
                'id': win_id,
                'x': int(x), 'y': int(y),
                'width': int(width), 'height': int(height),
                'destop_no': int(destop_no),
                'pid': int(pid)
            })
    return win_list


def position_window(win_id, x, y, width, height):
    Popen(['wmctrl', '-i', '-r', win_id,  '-e', ','.join([x, y, width, height])])


def focus_window(win_id):
    Popen(['wmctrl', '-i', '-a', win_id])


if __name__ == "__main__":
    for w in get_list_of_open_windows():
        print(w)
