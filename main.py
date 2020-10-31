#!/usr/bin/env python3

from FrameQueue import FrameQueue
from ExtractFrames import extractFrames
from ConvertToGrayscale import convertToGrayscale
from DisplayFrames import displayFrames
from threading import Thread, Lock, enumerate, Condition

#Locks that will be used by each thread to safely access hte produce/consumer queues
colorQueueLock = Lock()
grayscaleQueueLock = Lock()

#The producer/consumer queues that each thread will use to pass data with.
colorQueue = FrameQueue(colorQueueLock, ('Extracting','Converting'), max = 10)
grayscaleQueue = FrameQueue(grayscaleQueueLock, ('Converting', 'Displaying'), max = 10)

#All three threads are defined and given the approprite function and queues
threads = [Thread(target = extractFrames, args = (colorQueue,)),
           Thread(target = convertToGrayscale, args = (colorQueue, grayscaleQueue)),
           Thread(target = displayFrames, args = (grayscaleQueue,))]

#All threads started.
for i in range(len(threads)):
    threads[i].start()
