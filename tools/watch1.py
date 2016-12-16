#!env python
import evdev
import sys

try:
    location = sys.argv[1]
except IndexError:
    print "Missing Input Location"
    print "Usage:"
    print "  "+sys.argv[0]+" </dev/input/event?>"
    exit(1)
print location

device = evdev.InputDevice(location)
print(device)
Theevent = device.read_loop()
event = Theevent.next()
print(evdev.ecodes.EV[event.type], evdev.ecodes.KEY[event.code])
