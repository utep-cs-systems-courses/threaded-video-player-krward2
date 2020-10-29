
class FrameQueue:
    __init__(self, lock):
        self.list = []
        self.lock = lock

    def push(frame, thread):
        lock.acquire()
        self.list.insert(frame, 0)
        lock.release()

    def pop(thread):
        lock.acquire()
        frame = self.list.pop(len(self.list))
        lock.release()
        return frame
