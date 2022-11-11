def reversed_list( nodes ) :
	############# DO NOT CHANGE ANYTHING BELOW #############
	my_ll = MySpecialList(nodes)
	head = my_ll.root
	reversed_head = my_ll.reverseList(head)
	return my_ll.print_as_list(reversed_head)
	############# DO NOT CHANGE ANYTHING ABOVE #############



class Node:
	def __init__(self, data):
		self.value = data
		self.next = None



class MySpecialList:
	def __init__(self, arr):
		# Given an array, initialize it into a Linked List
		# The head of the Linked List should be saved as self.head
		
		self.arr = arr
		self.head = None
        for item in arr:
            self.insert(Node(item))
            


	def insert(self, root, item):
	# Given the root/head of a Linked List, appened the item to the end of the Linked List
	# Function should return the root/head of the Linked List
           
            Thenode = Node(item)
            current = Node(item)
            root = Node(root)
            while current.next != None:
                current = current.next
            current.next = Thenode

            return root


        def reverseList(self, head):
            # Given the head of a Linked List, reverse it and return the head of the newly reversed Linked List
            node = Node(head)
            current = node
            while current.next != None:
                current = current.next

            reversed_list_head = current
            
            return reversed_list_head

        def print_as_list(self, head):
            # Given the head of Linked List, this function will convert it to a list while preserving the order of the Linked List
            # Return the list
            linked_list_as_list = []
            current = Node(head)
            while current.next != None:
                linked_list_as_list.append(current)

            return linked_list_as_list
