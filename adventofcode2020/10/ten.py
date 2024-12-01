pathExists = False

def buildDict(data):
    graph = {}
    for i in data:
        graph[i] = []
    for i in data:
        if i+1 in data:
            graph[i].append(i+1)
        if i+2 in data:
            graph[i].append(i+2)
        if i+3 in data:
            graph[i].append(i+3)
    return graph


def bfs(visited, queue, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print(s)

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


"""
def dfs(visited, graph, node, max):
    if node not in visited:
        visited.add(node)
        print(visited)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, max)
"""
counter = 0
solutions = []


def dfs_util(visited, path, graph, node, max):
    global counter, solutions 
    visited[node] = True
    path.append(node)

    if node == max:
        #print(path)
        counter += 1
    else:
        for neighbour in graph[node]:
            if visited[neighbour] == False:
                dfs_util(visited, path, graph, neighbour, max)
    path.remove(node)
    visited[node] = False


if __name__ == "__main__":
    dfs_of = {}
    #input = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    #input = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
    input = open("input.txt")
    data = [int(l.strip("\n")) for l in input]
    #data = input
    data.append(0) # append 0 as start value
    data.append(max(data) + 3)
    s_data = sorted(data) # input sorted
    graph = buildDict(s_data)

    chunks = []
    gaps = [i for i in range(len(s_data)-1) if abs(s_data[i] - s_data[i+1]) == 3]
    temp = []
    for i in range(len(s_data)):
        temp.append(s_data[i])
        if i in gaps:
            chunks.append(temp)
            temp = []
    
    """
    r_list = []
    print(chunks)
    for i in range(len(chunks)):
        if len(chunks[i]) == 1:
            chunks[i-1] += chunks[i]
    for i in chunks:
        if len(i) == 1:
            chunks.remove(i)
    print(chunks)
    """

        


    combination_nums = []
    visited = {} # dict to keep track of visited nodes.
    print(chunks)
    for c in chunks:
        for i in c:
            visited[i] = False
        path = [] # Set to keep track of visited nodes.
        mi = min(c)
        ma = max(c)
        dfs_util(visited, path, graph, mi, ma)
        combination_nums.append(counter)
        counter = 0
        for i in c:
            visited[i] = False

    res = 1
    for num in combination_nums:
        res *= num
    print(res)




        
    



"""
    for i in range(1, len(way)):
        diff = way[i] - way[i-1]
        diff_dict[diff] += 1

    print(diff_dict[1])
    print(diff_dict[3])
    """

        



"""
    visited = [] # List to keep track of visited nodes.
    queue = []     #Initialize a queue
    bfs(visited, queue, graph, 0)
    """

