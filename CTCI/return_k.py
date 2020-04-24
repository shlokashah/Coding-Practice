##to be completed
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		count = 0
		while(temp):
			print(temp.data)
			temp = temp.next
			count = count+1
		return count

	def returnk(self,d,length):
		temp = self.head
		flag = 0
		prev = temp
		while(flag<d and temp is not None):
			prev = temp
			temp = temp.next
		return prev.data



if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	llist.head.next = second
	second.next = third
	third.next = None
	length = llist.printList()
	# print(length)
	number = llist.returnk(length-2+1,length)
	print(number)
	# llist.printList()