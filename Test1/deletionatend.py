#deletion at end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    # Insert at End
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    # Delete from End
    def delete_end(self):
        #  list is empty
        if self.head is None:
            print("List is empty")
            return
        # If there is only one node
        if self.head.next is None:
            self.head = None
            return       
        temp = self.head
        # Move to the second last node
        while temp.next.next:
            temp = temp.next
        # Delete last node
        temp.next = None
    # Display Linked List
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
# Create Linked List
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
print("Before Deletion:")
ll.display()
# Delete Last Node
ll.delete_end()
print("After Deletion:")
ll.display()