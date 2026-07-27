class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def insert_after(self, prev_data, data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Value not found in the list")
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.insert(20)
print("Linked List Elements:")
ll.display()
ll.insert_after(10, 12)
print("\nUpdated Linked List Elements after inserting 12 after 10:")
ll.display()