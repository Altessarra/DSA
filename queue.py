class queue:
  def __init__(self, limit= 5):
    self.limit = limit
    self.array = [None] * limit
    self.rear = -1
    self.front = -1 
    
  def empty(self):
    if self.rear == -1 and self.front == -1:
      return True
    else:
      return False

  def full(self):
    if self.rear == self.limit - 1:
      return True
    else:
      return False
  
  def enqueue(self, data):
    if self.full():
      print("Queue is full")
      return
    elif self.empty():
      self.rear = 0
      self.front = 0
      self.array[self.rear] = data
      print(f"{data} is enqueued")
    else:
      self.rear += 1
      self.array[self.rear] = data
      print(f"{data} is enqueued")
  
  def dequeue(self):
    if self.empty():
        print("Queue is empty")
        return None

    elif self.array[self.front] is not None:
        removed = self.array[self.front]
        self.array[self.front] = None
        self.front += 1

    if self.front > self.rear:
        self.front = -1
        self.rear = -1

    print(f"{removed} is dequeued")
    return removed

  def peek(self):
    if self.empty():
      print("Queue is empty")
      return
    else:
      return self.array[self.front]

myQueue = queue()

print("========= Queue Operations =========")

print("1. Is the Queue Empty?: ", myQueue.empty())

print("\n2. Enqueuing Elements into Queue:")
myQueue.enqueue('c')
myQueue.enqueue('h')
myQueue.enqueue('r')
myQueue.enqueue('i')
myQueue.enqueue('s')

print("\n3. Is the Queue Full?: ", myQueue.full())

print("\n4. Current front element is (Peek Operation):", myQueue.peek())
print("Current Array: ", myQueue.array)

print("\n4. Dequeuing two elements from Queue:")
myQueue.dequeue()
myQueue.dequeue()

print("\n5. Is the Queue Full?: ", myQueue.full())
print("\nIs the Queue Empty?: ", myQueue.empty())

print("\nCurrent Array: ", myQueue.array)

print("\n6. Current front element is (Peek Operation):", myQueue.peek())
