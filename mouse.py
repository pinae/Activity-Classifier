from Xlib import display
from time import sleep
while True:
    data = display.Display().screen().root.query_pointer()._data
    print(str((data["root_x"], data["root_y"])) + "        \r", end="")
    sleep(0.05)

