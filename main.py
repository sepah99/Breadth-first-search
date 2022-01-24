# This function finds a path from start to the end of the tree by checking if each node has been
# visited while going down each node
# AdjTable is a dictionary 
def computeBFStree(AdjTable, start):
    # define some variables etc.
    done = False
    tree = []

    i = 0

    if type(AdjTable) != dict:
        return 'AdjTable is invalid'

    if not(start in AdjTable.keys()):
        return 'No start node in the graph'

    # first node
    tree.append(start)
    head = start

    # trace each node until reach end node, from start node
    while not done:
        if i < len(AdjTable[head])  and AdjTable[head][i] in tree:
            i+=1
        elif i >= len(AdjTable[head]):
            done = True
        else:
            tree.append(AdjTable[head][i])
            head = AdjTable[head][i]
            i = 0

    return tree

# computeBFSpath finds the shortest path from start to goal by checking each child node and labeling its
# parent node, and backtracks its by going to each parent node until reached the start node
# AdjTable is a dictionary
def computeBFSpath(AdjTable, start, goal):
    if type(AdjTable) != dict:
        return 'AdjTable is invalid'

    if not (start in AdjTable.keys()):
        return 'No start node in the graph'

    if not (goal in AdjTable.keys()):
        return 'No goal node in the graph'


    # Turning dictionary keys into list, to interact with each indices as a node
    keys = list(AdjTable.keys())

    # created an array of parents to set the parent of each node based on its dictionary key index value
    parents = [None]*len(keys)


    # Setting start node parent to itself
    parents[keys.index(start)] = keys.index(start)

    # shortest path from start to goal
    path = []
    queue = []
    found = False
    queue.append(start)

    while len(queue) != 0:
        # parent node
        head = queue.pop(0)

        # nodes that are connected to the head
        sub_nodes = list(AdjTable[head])

        # go through all the child nodes initialize their parents and check if found
        for node in sub_nodes:
            if parents[keys.index(node)] == None:
                parents[keys.index(node)] = keys.index(head)
                queue.append(node)
            if node == goal:
                found = True
                break

    if not found:
        return 'No path'

    # if found we trace back to start from the end node using the parent array.
    # trace back to the parent until reached the start node, append each parent node to
    # path and reverse the array.

    i = keys.index(node)
    # Back track to start node
    while i < len(parents) and i != parents[i]:
        path.append(keys[i])
        i = parents[i]
    path.append(keys[i])
    path.reverse()

    return path


if __name__ == '__main__':
    # AdjTable defined as a dictionary 'Tom': ['Lee', 'Sam', 'Ben']

    AdjTable = {'Tom': ['Lee', 'Ben', 'Sam'],
                'Lee': ['Tom'],
                'Sam': ['Tom', 'Ben'],
                'Ben': ['Tom', 'Sam']}

    start = 'Lee'
    goal = 'Ben'

    myBFSTree = computeBFStree(AdjTable, start)
    print(myBFSTree)

    myBFSPath = computeBFSpath(AdjTable, start, goal)
    print(myBFSPath)
