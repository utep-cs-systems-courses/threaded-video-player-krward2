#!/usr/bin/env python3

import cv2
import sys

def convertToGrayscale(inQueue, outQueue):

    # initialize frame count
    count = 0
    print('ConvertToGrayscale starting')

    inputFrame = inQueue.dequeue()
    while inputFrame is not None and count < 72:
        grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)
        outQueue.enqueue(grayscaleFrame)
        count += 1
        inputFrame = inQueue.dequeue()

    outQueue.enqueue(None)
    print(' Converter EXITING')
    sys.exit()
