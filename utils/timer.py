import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.duration = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.duration = round(time.time() - self.start_time, 3)
