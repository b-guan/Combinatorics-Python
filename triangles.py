#!/usr/bin/env python3
import random
import math
def countTriangles(n,p):
	#will become a list of n nodes, consecutively numbered  0..n-1
	#example: [0,1,2,3]
	nodes = []
	
	#edges list will keep track of each edge formed, as a tuple. 
	#Each tuple contains the two nodes that are connected with each other
	#the tuples are listed consecutively, according to the first element in each tuple
	#tuples with the same first element are also listed in increasing order,
	#according to the second element in each tuple
	#example: [(0,3), (0,4), (0,5), (1,2), (1,5), (3,5)]
	edges = []
	
	#connections is a list that will containin n nested lists
	#each nested list, with index i, will contain the second element of each tuple in
	#edges that contain i as the first element
	#example (using the edges example above): [[3,4,5], [2,5], [], [5], [], []]
	connections = []
	
	number_of_triangles = 0
	expected = ((p/100.0)**3.0) * ((n*(n-1)*(n-2))/6)
	
	for i in range(n):
		nodes.append(i)
		connections.append([])
	
	#randomly forms each edge and appends edge to edge list as a tuple
	for node1 in range(n-1):
		for node2 in nodes[node1+1:]:
			if (random.randint(1,100) <= p):
				edges.append((node1,node2))
	for i in edges:
		index = i[0]
		connections[index].append(i[1])
	
	#iterates through each list in connections. Within each list, checks if the
	#each possible pair of nodes is actually an edge contained within the edge list
	#if it is, then increase number_of_triangles by 1
	for list in connections:
		for connected_node in list:
			for i in list[list.index(connected_node)+1:]:
				#still works without conditional?
				if ((connected_node, i) in edges):
					number_of_triangles +=1
	# print "nodes: "
	# print nodes
	# print "edges: "
	# print edges
	# print "connections: "
	# print connections
	# print "number of triangles: " + str(number_of_triangles)
	# print "expected: " + str(expected)
	# print "difference: " + str(number_of_triangles-expected)
	# return abs(number_of_triangles - expected)
	return number_of_triangles
def trials(t,n,p):
	average=0
	for i in range(t):
		average += countTriangles(n,p)
	expected = ((p/100.0)**3.0) * ((n*(n-1)*(n-2))/6)
	print "expected: "
	print str(expected)
	print 'actual: '
	return float(average)/t