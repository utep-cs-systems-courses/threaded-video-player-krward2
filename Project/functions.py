#!/usr/bin/env python3

import cv2, os, sys, time

def extractFrames(clipFileName, outQueue):
    print('Extract Frames starting.')
    count = 0
    # open the video clip
    vidcap = cv2.VideoCapture(clipFileName)
    # read one frame
    success,image = vidcap.read()

    while success and count < 72:
      outQueue.enqueue(image)
      success,image = vidcap.read()
      count += 1

    #End of stream signal for all 3 threads
    outQueue.enqueue(None)
    print('Extractor EXITING')
    sys.exit()

def convertToGrayscale(inQueue, outQueue):
    print('ConvertToGrayscale starting')
    count=0
    inputFrame = inQueue.dequeue()
    while inputFrame is not None and count < 72:
        grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)
        outQueue.enqueue(grayscaleFrame)
        inputFrame = inQueue.dequeue()

    outQueue.enqueue(None)
    print(' Converter EXITING')
    sys.exit()

def displayFrames(inQueue, frameDelay):
    #Console message
    print('Display frames starting.')
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
