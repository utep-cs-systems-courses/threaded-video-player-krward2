#!/usr/bin/env python3

import cv2
import time
import sys

def displayFrames(inQueue):
    #Console message
    print('Display frames starting.')

    # globals
    outputDir    = 'frames'
    frameDelay   = 42       # the answer to everything

    # initialize frame count
    count = 0

    frame = inQueue.dequeue()
    while frame is not None:
        cv2.imshow('Video', frame)
        if cv2.waitKey(frameDelay) and 0xFF == ord("q"):
            break
        count += 1
        frame = inQueue.dequeue()

    # make sure we cleanup the windows, otherwise we might end up with a mess
    cv2.destroyAllWindows()
    print('Displayer EXITING')
    sys.exit()
