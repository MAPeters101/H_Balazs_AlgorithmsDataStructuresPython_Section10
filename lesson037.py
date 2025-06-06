# FIFO First item we Insert is the First one to take Out

class Queue:
    def __init__(self):
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return self.queue == []

    # O(1) running time
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1

    # O(1) running time
    def peek(self):
        return self.queue[0]

    # O(1) running time
    def size_queue(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue)
print("Size: %d" % queue.size_queue())
print("Dequeue: %d" % queue.dequeue())
print("Size: %d" % queue.size_queue())
print("Dequeue: %d" % queue.dequeue())
print("Size: %d" % queue.size_queue())
print("Dequeue: %d" % queue.dequeue())
print("Size: %d" % queue.size_queue())
print("Dequeue: %d" % queue.dequeue())
print("Size: %d" % queue.size_queue())
print("Dequeue: %d" % queue.dequeue())




