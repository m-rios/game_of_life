from world import *
from time import sleep
import sys

if len(sys.argv) > 1:
    size = int(sys.argv[1])
else:
    size = 15
print 'size: %d' %size

world = World(size)
world.draw()
sleep(1)

while 1:
    world.calc()
    world.update()
    world.draw()
    sleep(0.2)