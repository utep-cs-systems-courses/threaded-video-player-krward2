#!/usr/bin/env python3

from FrameQueue import FrameQueue
from ExtractFrames import extractFrames
from ConvertToGrayscale import convertToGrayscale
from DisplayFrames import displayFrames
from threading import Thread, Lock, enumerate, Condition

colorQueueLock = Lock()
grayscaleQueueLock = Lock()

endOfVideo = False

colorQueue = FrameQueue(colorQueueLock, ('Extracting','Converting'), endOfVideo)
grayscaleQueue = FrameQueue(grayscaleQueueLock, ('Converting', 'Displaying'), endOfVideo)

threads = [Thread(target = extractFrames, args = (colorQueue,)),
           Thread(target = convertToGrayscale, args = (colorQueue, grayscaleQueue)),
           Thread(target = displayFrames, args = (grayscaleQueue,))]

for i in range(len(threads)):
    threads[i].start()

'''
while enumerate() == 0:
    sys.sleep(250)

print('Video complete')
'''
