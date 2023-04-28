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
            
    def get_position(self, element_val):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head 
        position = 1
        while current:
            if current.value == element_val:
                return position
            current = current.next 
            position += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head 
        if position == 1:
            new_element.next = current
            self.head = new_element
        else:
            for i in range (position-2):
                if current is None:
                    return
                else:   
                    current = current.next
            new_element.next = current.next       
            current.next = new_element
             
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current:  
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
                
    def get_value(self, position):
        current = self.head 
        pos = 1
        while current and pos<=position:
            if pos == position:
                return current.value
            current = current.next
            pos += 1
        return None
            
                                        
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position

print (ll.head.next.next.value)
position = ll.get_position(3)
if position:
    print(ll.get_value(position))

# Test insert
ll.insert(e4,4)
position = ll.get_position(4)
if position:
    print(ll.get_value(position))

# Test delete
ll.delete(1)
position = ll.get_position(2)
if position:
    print(ll.get_value(position))

#print (ll.get_position(1))
position = ll.get_position(4)
if position:
    print(ll.get_value(position))
#print (ll.get_position(2))
position = ll.get_position(3)
if position:
    print(ll.get_value(position))
#print (ll.get_position(3))