from threading import Condition
import sys, time

class FrameQueue:
    def __init__(self, lock, actions = ('enqueue', 'dequeue'), max = 5):
        self.list = []
        self.queueLock = lock
        self.emptyCondition = Condition(lock)
        self.fullCondition = Condition(lock)
        self.actions = actions
        self.maxQueueSize = max
        self.counter = 0

    def enqueue(self, frame):
        self.fullCondition.acquire()
        while self.isFull():
            print(self.actions[0], 'waiting for queue to empty.')
            self.fullCondition.wait()
        self.list.append(frame)
        self.counter += 1
        print(self.actions[0], 'frame', self.counter, '| Queue length:', len(self.list))
        self.emptyCondition.notify()
        self.fullCondition.release()

    def dequeue(self):
        self.emptyCondition.acquire()
        while self.isEmpty():
            print(self.actions[1], 'waiting for queue to populate')
            self.emptyCondition.wait()
        print(self.actions[1], 'frame', self.counter, '| Queue length:', len(self.list))
        frame = self.list.pop(0)
        self.fullCondition.notify()
        self.emptyCondition.release()
        return frame

    def isEmpty(self):
        return (len(self.list) == 0)

    def isFull(self):
        return (len(self.list) >= self.maxQueueSize)
