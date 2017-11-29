### Title
print('Final Exam, John Letey, john.letey@colorado.edu')
### Imports
import math
import random as rand
import networkx as nx
import matplotlib.pyplot as plt
### Problem 1 Code
print()
print('Problem #1')
print('--------------------')
## Implementation of Count
def Count(A, p, q, r):
	count = 0
	n1 = q - p + 1
	n2 = r - q
	L = []
	R = []
	for i in range(n1):
		L.append(A[p + i])
	for j in range(n2):
		R.append(A[q + j + 1])
	i, j, k = 0, 0, p
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
			count += (n1 - i)
		k += 1
	# Return the number of reverses in the array A[p:r]
	return count
## Implementation of CountReverses
def CountReverses(A, p, r):
	# Initialize the variable that will hold the number of reverses in the array A[p:r]
	count = 0
	# Calculate the number of reverses in the array A[p:r]
	if p < r:
		q = math.floor((p + r)/2)
		count += CountReverses(A, p, q)
		count += CountReverses(A, q+1, r)
		count += Count(A, p, q, r)
	# Return the count of reverses in the array A[p:r]
	return count
## Run the program for Problem 1
numbers = []
for i in range(100):
	numbers.append(rand.randint(0,100))
# numbers = [0, 2, 3, 1, 5, 4, 2, 7] # 6
print('Here is an array of randomly generated numbers:', numbers)
print('The number of reverses in the array is', CountReverses(numbers, 0, len(numbers)-1))
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
def countPaths(G, s, t):
	# Get the predecessors of the target t
	predecessors = list(G.predecessors(t))
	# Search the list of predecessors for the source s
	for predecessor in predecessors:
		if predecessor == s:
			return 1
	# Define a variable that will hold the count of how many paths there are from s to t
	count = 0
	# Go to each of the predecessors and calculate the number of paths
	for predecessor in predecessors:
		count += countPaths(G, s, predecessor)
	# Return the number of paths
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
target = input('What is the target in your graph? ')
# Get the number of paths from the source to the target
numOfPaths = countPaths(G, source, target)
# Tell the user how many paths there are from the source to the target
print('The number of paths from the source', source, 'to the target', target, 'is', numOfPaths, 'paths.')
### Problem 5 Code
print()
print('Problem #5')
print('--------------------')
##

## Run the program for problem 5
