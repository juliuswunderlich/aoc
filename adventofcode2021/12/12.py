import copy

fname = "12/input.txt"
f = open(fname, 'r')
data = [l.strip().split('-') for l in f]

_adj = {}
_paths = []

# build adjacency list
for pair in data:
    k = pair[0] #key
    v = pair[1] #value
    if k not in _adj.keys(): _adj[k] = [] # add, if not there yet
    if v not in _adj.keys(): _adj[v] = [] # add, if not there yet
    _adj[k].append(v)
    _adj[v].append(k)

"""
PART 1
def printAllPathsUtil(u, d, visited, path):
        # Mark the current node visited if not uppercase
        if u.islower():
            visited[u]= True
        path.append(u)
 
        # If current vertex is same as destination, then add the found path
        if u == d:
            _paths.append(copy.deepcopy(path))
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in _adj[u]:
                if visited[i]== False:
                    printAllPathsUtil(i, d, visited, path)
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False

# print all paths from s to e
def printAllPaths(s, e):
    # Mark all the vertices as not visited
    visited = dict(_adj)
    for v in visited: visited[v] = False # set all of them to false
    visited["end"] = False # add an extra entry for end
    # Create an array to store paths
    path = []
    # Call the recursive helper function to print all paths
    printAllPathsUtil(s, e, visited, path)
"""

duplicate = False
def printAllPathsUtil(u, d, visited, path):
        # Mark the current node visited if not uppercase
        if u.islower():
            visited[u]= True
        if duplicate and u !="start" and u != end:
            path.append(u)
            path.append(u)
            duplicate = False
 
        # If current vertex is same as destination, then add the found path
        if u == d:
            _paths.append(copy.deepcopy(path))
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in _adj[u]:
                if visited[i]== False:
                    printAllPathsUtil(i, d, visited, path)
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False

# print all paths from s to e
def printAllPaths(s, e):
    # Mark all the vertices as not visited
    visited = dict(_adj)
    for v in visited: visited[v] = False # set all of them to false
    visited["end"] = False # add an extra entry for end
    # Create an array to store paths
    path = []
    # Call the recursive helper function to print all paths
    printAllPathsUtil(s, e, visited, path)

printAllPaths("start", "end")
print(len(_paths))