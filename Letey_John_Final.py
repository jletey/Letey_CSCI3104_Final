### Title
print('Final Exam, John Letey, john.letey@colorado.edu')
### Imports
import math
import random as rand
import networkx as nx
import matplotlib.pylab as plt
### Problem 1 Code
print()
print('Problem #1')
print('--------------------')
## Implementation of Count
def Count(A, p, q, r):
	count = 0
	if (r - q)%2 == 0:
		L = A[p:q]
		R = A[q:r]
	else:
		L = A[p:q+1]
		R = A[q+1:r]
	i, j = 0, 0
	for k in range(p ,r):
		if L[i] > R[j]:
			count += 1
			j += 1
		else:
			i += 1
		if i == len(L) or j == len(R):
			return count
	return count
## Implementation of CountReverses
def CountReverses(A, p, r):
	# Initialize the variable that will hold the number of reverses in the array A[p:r]
	count = 0
	# Calculate the number of reverses in the array A[p:r]
	if len(A[p:r]) > 2:
		q = math.floor((p + r)/2)
		count += CountReverses(A, p, q)
		count += CountReverses(A, q, r)
		count += Count(A, p, q, r)
		print('The count is', count)
	# Return the count of reverses in the array A[p:r]
	return count
## Run the program for Problem 1
# numbers = []
# for i in range(100):
# 	numbers.append(rand.randint(0,100))
numbers = [21, 11, 10, 16] # 1
print('Here is an array of randomly generated numbers:', numbers)
print('The number of reverses in the array is', CountReverses(numbers, 0, len(numbers)))
### Problem 2 Code
print()
print('Problem #2')
print('--------------------')
## Implementation of the Ford-Fulkerson Algorithm
def FordFulkerson(G, s, t):
	flow = [0 for i in range(len(G.edges))]
	# while
	return flow
## Run the program for problem 2

### Problem 3 Code
print()
print('Problem #3')
print('--------------------')

## Run the program for problem 3

### Problem 4 Code
print()
print('Problem #4')
print('--------------------')
## Implementation of countPaths
def countPaths(G, s, t, count=0):
	# Get the edges of the graph
	edges = list(G.edges())
	# Search the edges for the target t, and check to see if you're an edge away from the source
	positions = []
	isDone = False
	for i in range(len(edges)):
		start, end = edges[i]
		if end == t:
			positions.append(i)
			count += 1
			if start == s:
				isDone = True
	# Count the paths on each of the different paths
	if not isDone:
		for i in positions:
			start, end = edges[i]
			count = countPaths(G, s, start, count)
		return count
	else:
		return count
## Run the program for problem 4
# Initialize the directed graph G
G = nx.DiGraph()
# Add edges and nodes to the graph G
G.add_edge('Spider', 'A', weight=1.0)
G.add_edge('Spider', 'H', weight=1.0)
G.add_edge('Spider', 'J', weight=1.0)
G.add_edge('H', 'G', weight=1.0)
G.add_edge('H', 'K', weight=1.0)
G.add_edge('G', 'L', weight=1.0)
G.add_edge('G', 'F', weight=1.0)
G.add_edge('F', 'E', weight=1.0)
G.add_edge('E', 'Fly', weight=1.0)
G.add_edge('J', 'S', weight=1.0)
G.add_edge('J', 'K', weight=1.0)
G.add_edge('K', 'L', weight=1.0)
G.add_edge('L', 'M', weight=1.0)
G.add_edge('M', 'N', weight=1.0)
G.add_edge('M', 'F', weight=1.0)
G.add_edge('N', 'O', weight=1.0)
G.add_edge('N', 'E', weight=1.0)
G.add_edge('O', 'Fly', weight=1.0)
G.add_edge('A', 'S', weight=1.0)
G.add_edge('A', 'B', weight=1.0)
G.add_edge('B', 'R', weight=1.0)
G.add_edge('B', 'C', weight=1.0)
G.add_edge('S', 'R', weight=1.0)
G.add_edge('R', 'Q', weight=1.0)
G.add_edge('Q', 'C', weight=1.0)
G.add_edge('Q', 'P', weight=1.0)
G.add_edge('C', 'D', weight=1.0)
G.add_edge('D', 'Fly', weight=1.0)
G.add_edge('P', 'D', weight=1.0)
G.add_edge('P', 'O', weight=1.0)
G.add_edge('O', 'Fly', weight=1.0)
G.add_edge('T', 'Q', weight=1.0)
G.add_edge('T', 'P', weight=1.0)
G.add_edge('T', 'O', weight=1.0)
G.add_edge('T', 'N', weight=1.0)
G.add_edge('T', 'M', weight=1.0)
G.add_edge('R', 'T', weight=1.0)
G.add_edge('S', 'T', weight=1.0)
G.add_edge('J', 'T', weight=1.0)
G.add_edge('K', 'T', weight=1.0)
G.add_edge('L', 'T', weight=1.0)
# Print the list of nodes
print('The nodes that are in the graph are:', end=' ')
nodes = list(G.nodes())
nodes.sort()
for i in range(len(nodes)):
	print(nodes[i], end='')
	if i < len(nodes)-2:
		print(',', end=' ')
	else:
		if i == len(nodes)-2:
			print(', and', end=' ')
		else:
			print('.')
# Get the source and the target
source = input('What is the source in your graph? ')
target = input('What is the sink in your graph? ')
# Get the number of paths from the source to the target
numOfPaths = countPaths(G, source, target)
# Tell the user how many paths there are from the source to the target
print('The number of paths from the source', source, 'to the sink', target, 'is', numOfPaths, 'paths.')
### Problem 5 Code
print()
print('Problem #5')
print('--------------------')
##

## Run the program for problem 5
