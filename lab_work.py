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
        if self.head is None:
            #give our first node the head and tail pointer 
            self.head = new_node 
            self.tail = new_node 
            return 
        #make the new_node point to the old head 
        new_node.next = self.head 
        #you move the head pointer to the new node 
        self.head = new_node 

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            #give our first node the head and tail pointer 
            self.head = new_node 
            self.tail = new_node 
            return 
        #we reach here if we have an head already. we then make the new_node the next value 
        self.tail.next = new_node
        #Give the new_node the tail pointer. 
        self.tail = new_node 

    def delete_node(self, key):
        #if the key is located at the head, 
        if self.head.data == key:
            #make the next node the head 
            self.head = self.head.next 
            return 
        
        prev = None 
        current = self.head 
        #as long as we are within the linked list and we have not 
        # found the key  
        while current and current.data != key:
            prev = current 
            current = current.next 
            
            return 
        #we come out of the loop when the key is found 
        #and ignore the node containing the key by making 
        #it's previous node have a next pointer to it's next node
        prev.next = current.next

        
        if current == self.tail:
            self.tail = prev
        
    def display_list(self):
        temp = self.head
        #we print this as long as there is a next value 
        while temp:
            print(temp.data, end="->")
            temp = temp.next 
        print("None")

#test 
lst = LinkedList()
#lst.insert_at_beginning(10)
#lst.insert_at_beginning(20)
#lst.insert_at_beginning(30)
#lst.insert_at_beginning(40)
#lst.insert_at_beginning(50)


lst.insert_at_end(10)
lst.insert_at_end(20)
lst.insert_at_end(30)
lst.insert_at_end(40)
lst.insert_at_end(50)

lst.delete_node(20)
lst.display_list()
