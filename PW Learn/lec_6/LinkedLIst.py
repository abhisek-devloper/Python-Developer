class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Insert at a specific position (0-based index)
    def insert_at_position(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 0
        while temp is not None and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Index out of range.")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print("Value not found in the list.")

    # Delete at a specific position (0-based index)
    def delete_at_position(self, index):
        if self.head is None:
            print("List is empty.")
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0
        while temp.next is not None and count < index - 1:
            temp = temp.next
            count += 1

        if temp.next is None:
            print("Index out of range.")
            return

        temp.next = temp.next.next

    # Traverse the list
    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------------------
# Test the LinkedList
# -------------------
ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
ll.insert_at_position(2, 15)

print("Linked List after insertions:")
ll.traverse()

ll.delete_by_value(15)
print("After deleting value 15:")
ll.traverse()

ll.delete_at_position(1)
print("After deleting at position 1:")
ll.traverse()

