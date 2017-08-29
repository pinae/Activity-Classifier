#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Xlib import display, X


def get_list_of_open_windows():
    x_win_list = display.Display().screen().root.query_tree().children
    window_list = []
    for win in x_win_list:
        try:
        #if win.get_attributes().map_state == X.IsViewable:
            name = win.get_wm_name()
            geometry = win.get_geometry()
            window_list.append((name, {'x': geometry.x, 'y': geometry.y,
                                       'width': geometry.width, 'height': geometry.height}))
        except TypeError:
            print(win.id)
    return window_list


if __name__ == "__main__":
    for w in get_list_of_open_windows():
        print(w)
