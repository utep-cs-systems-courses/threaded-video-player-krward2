from threading import Condition
from threading import Semaphore
import sys, time


class FrameQueue:
    def __init__(self, lock, name, max = 5):
        self.list = []
        self.queueLock = lock
        self.emptyCheck = Semaphore(0)
        self.fullCheck = Semaphore(max)
        self.name = name
        self.maxQueueSize = max
        self.inCounter = 0
        self.outCounter = 0

    def enqueue(self, frame):
        self.fullCheck.acquire() #Blocks the producer thread if the queue is full
        self.inCounter += 1
        print(self.name, 'enqueuing frame', self.inCounter, '| Queue length:', len(self.list))

        self.queueLock.acquire() #Ensures only one thread has access to the queue.
        self.list.append(frame)
        self.queueLock.release()

        self.emptyCheck.release() #Will un-block the consumer thread if waiting on queue to fill

    def dequeue(self):
        self.emptyCheck.acquire() # Blocks the consumer thread if queue is empty
        self.outCounter += 1
        print(self.name, 'dequeuing frame', self.outCounter, '| Queue length:', len(self.list))

        self.queueLock.acquire() #Ensures only one thread has access to the queue.
        frame = self.list.pop(0)
        self.queueLock.release()

        self.fullCheck.release() #Will un-block the producer thread if waiting for space in the queue
        return frame

    def isEmpty(self):
        return (len(self.list) == 0)

    def isFull(self):
        return (len(self.list) >= self.maxQueueSize)
