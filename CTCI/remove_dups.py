class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	def dups(self):
		temp = self.head
		while(temp):
			flag = temp.data
			forward = temp.next
			prev = temp
			while(forward):
				if(forward.data == flag):
					prev.next =  forward.next
				prev = forward
				forward = forward.next
			temp = temp.next
if __name__ == '__main__':

	llist = LinkedList()
	llist.head = Node("F")
	second = Node("O")
	third = Node("L")
	fourth = Node("L")
	fifth = Node("O")
	sixth = Node("W")
	llist.head.next = second
	second.next = third
	third.next = fourth
	fourth.next = fifth
	fifth.next = sixth
	sixth.next = None
	llist.printList()
	llist.dups()
	llist.printList()