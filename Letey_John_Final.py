### Title
print('Final Exam, John Letey, john.letey@colorado.edu')
### Imports
import math
import random as rand
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
### Problem 1 Code
print()
print('Problem #1')
print('--------------------')
## Implementation of Count
def Count(A, p, q, r):
	# Initialize the variable that will hold the number of reverses in the array A[p:r]
	count = 0
	# Define the size of the left half and right half of the array A[p:r]
	n1 = q - p + 1
	n2 = r - q
	# Calculate the left half and the right half of the array A[p:r]
	L = []
	R = []
	for i in range(n1):
		L.append(A[p + i])
	for j in range(n2):
		R.append(A[q + j + 1])
	# Define some indeces
	i, j, k = 0, 0, p
	# Calculate the number of reverses in the array A[p:r]
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
			count += (n1 - i)
		k += 1
	# But, we forgot the edge cases when n1 > n2 and n1 < n2
	while i < n1:
		A[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		A[k] = R[j]
		j += 1
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
# Randomly generate an array of numbers
numbers = []
for i in range(100):
	numbers.append(rand.randint(0,100))
# 
choice = str(input('Do you want to see the randomly generated list of numbers? [y/n] '))
if choice == 'y':
	print('Here is an array of randomly generated numbers:', numbers)
print('The number of reverses in the array is', CountReverses(numbers, 0, len(numbers)-1))
choice = str(input('Since I used the Merge-Sort algorithm, do you want to see the sorted array? [y/n] '))
if choice == 'y':
	print('The sorted array is', numbers)
### Problem 2 Code
print()
print('Problem #2')
print('--------------------')
# ## Implementation of path_exists_in_residual_net
# def path_exists_in_residual_net(Gf, s, t):
	
# ## Implementation of Ford-Fulkerson
# def FordFulkerson(G, s, t):
# 	# Define an array that will hold the flow
# 	flow = [0 for i in range(len(G.edges))]
# 	# Calculate the flow
# 	while path_exists_in_residual_net(Gf, s, t):

# 	# Return the flow
# 	return flow
## Implementation of calculateHatGraph
def calculateHatGraph(G, bptp, liui):
	# Define another graph to G
	GHat = G
	# Add a super source and a super sink to the graph
	GHat.add_nodes_from(['S', 'T'])
	# Define indeces
	personIndex, issueIndex = 0, 0
	# Add lower bounds
	for node in list(GHat.nodes()):
		if node[:5] == 'Issue':
			if issueIndex < len(liui):
				GHat.add_edge(node, 'T', lower=liui[issueIndex][0], capacity=liui[issueIndex][1])
				issueIndex += 1
		else:
			if personIndex < len(bptp):
				GHat.add_edge('S', node, lower=bptp[personIndex][0], capacity=bptp[personIndex][1])
				personIndex += 1
	# Return the new graph
	return GHat
## Run the program for problem 2
# Get how many issues there are
numOfIssues = int(input('How many issues are there? '))
# Set a list of issues, where the numbers correspond to specific issues
issues = [i+1 for i in range(numOfIssues)]
# Get how many people there are
numOfPeople = int(input('How many people are there? '))
# Randomly generate issues for each person
IssuesAndPeople = []
for i in range(numOfPeople):
	for j in range(numOfIssues):
		isIssue = bool(rand.randint(0, 1))
		if isIssue:
			IssuesAndPeople.append(('Person '+str(i+1), 'Issue '+str(issues[j])))
# Print the randomly generated list of issues and corresponding people
choice = str(input('Do you want to see the randomly generated list of issues and corresponding issues? [y/n] '))
if choice == 'y':
	print('Here are the edges between people and issues:', IssuesAndPeople)
# 
bptp = []
for i in range(numOfPeople):
	tp = 0
	for j in range(len(IssuesAndPeople)):
		if IssuesAndPeople[j][0] == 'Person '+str(i+1):
			tp += 1
	bp = tp//2
	bptp.append((bp, tp))
#
liui = []
for i in range(numOfIssues):
	li = rand.randint(300, 400)
	ui = rand.randint(500, 700)
	liui.append((li, ui))
# Create a directed graph containing the issues and people
G = nx.DiGraph()
G.add_edges_from(IssuesAndPeople, lower=0, capacity=1)
# Calculate G^ (GHat)
GHat = calculateHatGraph(G, bptp, liui)
inputFlow, flow = nx.maximum_flow(GHat, 'S', 'T')
#
print('The input flow to the graph is:', inputFlow)
#
choice = str(input('Do you want to see the flow for each person? [y/n] '))
if choice == 'y':
	print(flow)
### Problem 3 Code
print()
print('Problem #3')
print('--------------------')
##

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
## Implementation of whoWasHit
def whoWasHit(distances):
	hits = [[] for i in range(len(distances))]
	for i in range(len(distances)):
		Min = float('inf')
		index = 0
		for j in range(len(distances)):
			if distances[i][j] < Min and i != j:
				Min = distances[i][j]
				index = j
		hits[index].append(i+1)
	return hits
## Run the program for problem 5
# Set a list of people on the field
n = [3, 5, 7, 9, 11, 13, 15, 17, 19]
# Get the number of tests the user wants to run on the program
numOfTests = int(input('How many tests do you want to run on my program? '))
# Randomly generate distances 
distances = []
for i in range(numOfTests):
	ni = n[rand.randint(0, len(n))-1]
	distance = [[-1 for i in range(ni)] for j in range(ni)]
	dists = np.random.choice([i for i in range(1, 51)], size=50, replace=False)
	for j in range(ni):
		distance[j][j] = float('inf')
	for j in range(ni):
		for k in range(ni):
			if j != k and distance[j][k] == -1:
				distance[j][k] = dists[k]
				distance[k][j] = dists[k]
	distances.append(distance)
# Get the choice from the user of if the user wants to see the output of each test
choice = str(input('Do you want to see the ouput of each test? [y/n] '))
# Calculate who gets hit, and who doesn't with all of the test cases
numOfTrues = 0
for i in range(numOfTests):
	# Tell the user what test this is
	if choice == 'y':
		print('==========Test ', i+1, '==========',sep='')
	# Calculate who gets hit, and who doesn't
	listOfHits = whoWasHit(distances[i])
	# Print to the user how many people are on the field
	if choice == 'y':
		print('There are', len(distances[i]), 'people on the field')
	# Print all the people that didn't get hit
	didntGetHit = False
	for j in range(len(distances[i])):
		if listOfHits[j] == []:
			if choice == 'y':
				print('Person', j+1, 'never gets hit')
			didntGetHit = True
	if not didntGetHit:
		if choice == 'y':
			print('Everybody got hit')
	else:
		numOfTrues += 1
# Tell the user how many of the tests were true
if choice == 'y':
	print()
print('Out of', numOfTests, 'there were', numOfTrues, 'tests that one or more people were not hit in')