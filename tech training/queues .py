#linear queue
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, i):
        self.queue.append(i)
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return None
        return self.queue.pop(0)
    def peekfront(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[0]
    def peekrear(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[-1]
    def display(self):
        print("Queue:", self.queue)
    def isEmpty(self):
        return len(self.queue) == 0
    def clear(self):
        self.queue = []
        print("Queue cleared")
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
print(q.peekfront())
print(q.peekrear()) 
q.display()
q.clear()
q.display()

#circular queue
class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def isFull(self):
        return (self.rear+1)%self.size == self.front

    def isEmpty(self):
        return self.front ==-1

    def enqueue(self,value):
        if(self.isFull()):
            print("Queue Over Flow")
        if self.isEmpty():
            self.front=0
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=value
        print(f"Enqueued {value} at index {self.rear}")
    def dequeue(self):
        if self.isEmpty():
            return "Queue under flow!"
        val = self.queue[self.front]
        self.queue[self.front]=None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front=(self.front+1) % self.size
        return val

    def display(self):
        if self.isEmpty():
            print("Empty")
            return
        i,elems=self.front,[]
        while True:
            elems.append(self.queue[i])
            if i== self.rear:
                break
            i=(i+1)%self.size
        print("CircularQueue: ",elems)

c=CircularQueue(4)
c.enqueue(10)
c.enqueue(20)
c.enqueue(30)
c.enqueue(40)
c.display()
c.dequeue()
c.display()


