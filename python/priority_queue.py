'''
Created on May 20, 2015

@author: tekrei
Priority Queue capable of storing with a priority
Source: http://stackoverflow.com/questions/9289614/how-to-put-items-into-priority-queues
'''
from queue import PriorityQueue

class PQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item