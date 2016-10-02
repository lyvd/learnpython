'''
Using dictionaries, it is easy to implement the adjacency list in Python
We will create two classes , Graph, which holds the master of list of vertices,
and Vertex, which will represent each vertext in the graph.

Each Vertex uses a dictionary to keep track of the vertices to which is connected,
and the weight of each edge. 
'''

class Vertex:

	# constructor
	def __init__(self, key):

		# vertice id
		self.id = key

		# a dictionary to represent connected vertices
		self.connectedTo = {}

	# add a connection from this vertex to another
	def addNeighbor(self, nbr, weight = 0):
		self.connectedTo[nbr] = weight

	# display connected vertices
	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

	# get connections in the adjacent list
	def getConnections(self):
		return self.connectedTo.keys()

	# get id
	def getId(self):
		return self.id

	# get weight
	def getWeight(self):
		return self.weight


'''
The Graph class contains a dictionary that maps vertex names to vertex objects

'''

class Graph:

	# constructor
	def __init__(self):

		# list of vertices
		self.vertList = {}

		# number of vertices
		self.numVertices = 0

	# Add a vertex to the graph
	def addVertex(self, key):

		# increase number of verices
		self.numVertices = self.numVertices + 1

		# create a new vertext
		newVertex = Vertex(key)

		# add a vertice to the graph
		self.vertList[key] = newVertex

		# return the new vertex
		return newVertex

	# Get a vertex
	def getVertex(self, v):

		# check whether the vertex is in the list or not
		if v in self.vertList:

			# if so, return the vertex
			return self.vertList[v]

		else:
			return None

	# check a vertex is in the  graph
	def __contains__(self, v):
		return ( v in self.vertList )

	# Add an edge from a vertex to another
	def addEdge(self, f, t, cost = 0):

		# if the fist vertex is not in the graph
		if f not in self.vertList:
			nv = self.addVertex(f)

		# if the second vertex is not in the graph
		if t not in self.vertList:
			nv = self.addVertex(t)

		self.vertList[f].addNeighbor(self.vertList[t], cost)

	# get vertices
	def getVertices(self):
		return self.vertList.keys()

	# List vertex's value
	def __iter__(self):
		return iter(self.vertList.values())

# Create a Graph instance
g = Graph()

# Fill the graph with nodes 
for i in range(6):
	g.addVertex(i)

print(g.vertList)

# add connections between nodes
g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 5, 3)
g.addEdge(3, 4, 7)
g.addEdge(4, 0, 1)
g.addEdge(5, 2, 1)
g.addEdge(5, 4, 8)

for v in g:
	for w in v.getConnections():
		print("%s, %s" %(v.getId(), w.getId()))



