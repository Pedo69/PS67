# Node class
class Node:
# Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

        # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
        print("Delete node "+(str)(key))
        temp = head
        prev = None

    # Base case if linked list is empty
        if temp is None:
            return head

        # Case 1: Head is to be deleted
        if key == 1:
            head = temp.next
            return head

        # Case 2: Node to be deleted is in middle
        # Traverse till given position
        for i in range(1, key):
            prev = temp
            temp = temp.next
            if temp is None:
                print("Data not present")
                return head

        # If given position is found, delete node
        if temp is not None:
            prev.next = temp.next

        return head


    #write code here
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next
           
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    print ("Created Linked List: ")
    llist.printList()
    llist.deleteNode(1)
    print ("Linked List after Deletion of 1:")
    llist.printList()