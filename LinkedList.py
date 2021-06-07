# Edgar Castillo / Github: https://github.com/hellocastillo
# Copyright (c) 2021 Edgar Castillo

# Linked List is a form of a sequential collection and it does not have to be in order.
# A Linked List is made up of independent nodes that may contain any type of data and each node has a reference to the next node in the link.

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head = node()
        
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
        
