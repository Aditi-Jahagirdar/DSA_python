class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        current = self.head
        if current:
            new_element.next = current
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        current = self.head
        if current:
            if current.next:
                self.head = self.head.next
            else:
                self.head = None 
            return current
        else:
            return None
    
class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)
        self.maxSize = 8
        self.top = -1

    def push(self, new_element):
        if self.top >= self.maxSize:
            return None
        else:
            self.top += 1
            self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        if self.top < -1:
            return None
        else:
            self.top -= 1
            return self.ll.delete_first()
        
            
          
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)

# val = stack.pop()
# print(val.value)
print (stack.pop().value)  #3
print (stack.pop().value)  #2
print (stack.pop().value)  #1

print (stack.pop())  

stack.push(e4)             
print (stack.pop().value)  #4