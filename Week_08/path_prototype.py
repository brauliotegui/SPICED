#
# prototype for movement paths
# that can be taken in single steps
#
# this is necessary so that multiple agents
# can move simultaneously
#
import time

LEFT = (-1, 0)
RIGHT = (+1, 0)
UP = (0, -1)
DOWN = (0, +1)

PATH1 = [LEFT] * 10 + [UP] * 10 + [RIGHT] * 20
PATH2 = [LEFT] * 20 + [DOWN] * 10 + [RIGHT] * 10


x, y = 100, 100  # starting position
path = PATH1[:]  # copy the path
target = 'one'   # name of the destination

def next_step():
    """walks one step only"""
    global x      # global variables are dirty programming
    global y      # but its a prototype
    global path
    global target
    dx, dy = path.pop(0)
    x += dx
    y += dy
    if len(path) == 0:
        # set new target
        if target == 'one':
            path = PATH2[:]
            target = 'two'
        else:
            path = PATH1[:]
            target = 'one'


while True:
    next_step()
    print(f"position {x:4}/{y:4}   steps until {target}: {len(path)})")
    time.sleep(0.1)
