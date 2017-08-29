from Xlib import display


def get_mouse_position():
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]


if __name__ == "__main__":
    from time import sleep
    while True:
        print("{}        \r".format(get_mouse_position()), end="")
        sleep(0.05)

