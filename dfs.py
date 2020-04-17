from collections import defaultdict

class DepthFirstSearch():
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

	def dfs_search(self,node,visited):
		visited[node] = 1
		print(node,end = " ")
		for i in self.graph[node]:
			if(visited[i] ==0):
				self.dfs_search(i,visited)

	def dfs(self,node):
		visited = [0 for i in range(0,len(self.graph))]
		print(visited)
		self.dfs_search(node,visited)

if __name__ == '__main__':
	g = DepthFirstSearch()
	g.create_graph()
	print("Enter the node to start search from")
	node = int(input())
	g.dfs(node)