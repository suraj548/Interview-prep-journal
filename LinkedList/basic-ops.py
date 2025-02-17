class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
        
    def append(self, value): # O(1)
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        return True
    
    def pop(self): # O(n)
        if self.lenght == 0:
            return None
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.lenght -= 1
        if self.lenght == 0:
            self.head == None
            self.tail == None
        return temp
    
    def prepend(self, value): # O(1)
        new_value = Node(value)
        if self.lenght == 0:
            self.head = new_value
            self.tail = new_value
        else:
            new_value.next = self.head
            self.head = new_value
        self.lenght += 1
        return True
    
    def pop_first(self): # O(1)
        if self.lenght == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.lenght -= 1
        if self.lenght == 0:
            self.tail = None
        return temp

    def get(self, index): # O(n)
        if index > self.lenght or index < 0:
            return None
        temp = self.head
        for _ in range(0, index): #by default the start value i.e index will be 0
            temp = temp.next
        return temp
    
    def set(self, index, value): # O(n)
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def print(self): # O(n)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next                

    def insert(self, index, value): #O(1)
        if index > self.lenght or index < 0:
            return False
        if index == self.lenght:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.lenght += 1
        return True    
            
    def delete (self, index): # O(1)
        if index > self.lenght or index < 0:
            return False
        if index == self.lenght:
            return self.pop()
        elif index == 0:
            return self.pop_first()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.lenght -= 1
        return True
    
    def reverse(self): # O(n)
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.lenght):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True
        
        
a = LinkedList(5)
a.append(6)
a.pop()
a.prepend(6)
a.prepend(1)
a.append(4)
a.append(3)
a.set(2, 8)
a.insert(2, 9)
a.print()
print("-------------------------------")
a.delete(2)
a.print()
print("-------------------------------")
a.reverse()
a.print()
print(a.head.value, a.tail.value)

        
        