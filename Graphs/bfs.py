from collections import defaultdict

class BreadthFirstSearch():
	def __init__(self):
		self.graph = defaultdict(list)

	def create_graph(self):
		print("Enter the number of nodes")
		node = int(input())
		print("Press -1 to exit")
		choice = 0
		while(choice!=-1):
			print("Enter the edges,input node1 and node2")
			node1 = int(input())
			node2 = int(input())
			self.graph[node1].append(node2)
			choice = int(input())
		print(self.graph)

	def bfs(self,node):
		visited = [0 for i in range(0,len(self.graph))]
		queue = []
		queue.append(node)
		visited[node] = 1
		while(queue):
			s = queue.pop(0)
			print(s,end = " ")
			for i in self.graph[s]:
				if (visited[i] == 0):
					queue.append(i)
					visited[i] = 1


if __name__ == '__main__':
	g = BreadthFirstSearch()
	g.create_graph()
	print("Enter the node to start search from")
	node = int(input())
	g.bfs(node)