#!/usr/bin/env python

import sys

def main(argv):
    ver = sys.version_info
    print("Program '%s' argc = %d Python %d.%d" %
            (argv[0], len(argv), ver[0], ver[1]))

    for i in range(0, len(argv)):
        print("argv[%d] = '%s'" % (i, argv[i]))
    return 0

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
else:
    # Don't import the file
    exit(1)
