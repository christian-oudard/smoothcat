import os
import sys
import time

# Adapted from slowcat.
# https://grox.net/software/mine/slowcat/slowcat.py

delay = .03
if len(sys.argv) > 1:
  arg = sys.argv[1]
  if arg != "-d":
    print("usage: %s [-d delay]" % (sys.argv[0]))
    print( "delay: delay in seconds")
    print("example: %s -d .02 < vtfile" % (sys.argv[0]))
    sys.exit()
  if len(sys.argv) > 2:
    delay = float(sys.argv[2])

columns = os.get_terminal_size().columns
buf = ''
time.sleep(delay)
while True:
    # Fill the buffer up to the column size.
    data = sys.stdin.read(columns - len(buf))
    if len(data) == 0:
        break
    buf += data
    assert len(buf) <= columns

    # Display each line in the buffer except the last one.
    # If it is all on a single line, just display it and clear the buffer.
    lines = buf.split('\n')
    if len(lines) > 1:
        buf = lines.pop()
    else:
        buf = ''
    for line in lines:
        print(line)
        time.sleep(delay)
