class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def print_linked_list(self):
        if not self.head:
            return False
    
        result = []
        current_node = self.head
        while current_node:
            result.append(str(current_node.data))
            current_node = current_node.next
    
        return " -> ".join(result)
    
    def remove_beginning(self):
        if self.head is None:
            return False 
        self.head = self.head.next
        if self.head is None:  
            self.tail = None
        return True
    
    def remove_at_end(self):
        if self.head is None:
            return False
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
        return True

    def remove_at(self, data):
        if self.head is None:
            return False
        elif self.head.data == data:
            self.remove_beginning()
            return True
        else:
            current_node = self.head
            while current_node.next and current_node.next.data != data:
                current_node = current_node.next
            if current_node.next is None:
                return False
            else:
                if current_node.next == self.tail:
                    self.tail = current_node
                current_node.next = current_node.next.next
                return True