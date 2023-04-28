class Queue:
    def __init__(self, head=None):
        #self.ll = LinkedList(top)
        self.storage = [head]
        self.head = head

       
    def enqueue(self, new_element):
        self.storage.append(new_element)
        

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            removed_element = self.storage.pop(0)
            self.head +=1
            return removed_element
        
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print (q.peek())

# Test dequeue
# Should be 1
print (q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print (q.dequeue())
# Should be 3
print (q.dequeue())
# Should be 4
print (q.dequeue())
q.enqueue(5)
# Should be 5
print (q.peek())