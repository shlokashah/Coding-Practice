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

	def deletenode(self,second):
		temp = self.head
		if self.head.data == second:
			return
		else:
			while(temp):
				if(temp.data == second.data and temp.next!=None):
					flag.next = second.next
				flag = temp
				temp=temp.next



if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	llist.head.next = second
	second.next = third
	third.next = None
	llist.printList()
	llist.deletenode(1)
	llist.printList()