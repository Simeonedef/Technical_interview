import numpy
from collections import defaultdict

# compare if element happens before or at given index
def cmp(c, index):
    notSeen = True
    for y in range(0, len(hint_list)):
        if c in hint_list[y]:
            notSeen = False
            temp_index = hint_list[y].index(c)
            if temp_index > index:
                return False
    if notSeen is False:
        return True
    else:
        return False

# dict of every element appearing in hints
def create_dict(hint):
    # create dict
    temp = []
    for i in range(0, hint.shape[0]):
        for x in range(0, hint[i].size):
            temp.append(hint[i][x]);
    temp_dict = dict((temps, number) for number, temps in enumerate(temp))
    print("Dictionary length: %f" % len(temp_dict))
    return temp_dict

# turn hints into lists for easier removal
def create_list(hint):
    hint_list = []
    for x in range(0, hint.shape[0]):
        hint_list.append(hint[x].tolist())
    return hint_list

# main loop to find alphabet
def find_alphabet(temp_dict, hint_list):
    # create alphabet
    alphabet = []
    # find the current first element after previous first element has been removed
    for i in range (0, len(temp_dict)):
        for temps in temp_dict:
            if cmp(temps, 0):
                alphabet.append(temps)
                break

        for y in range(0, len(hint_list)):
            if temps in hint_list[y]:
                hint_list[y].remove(temps)

    return alphabet


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A recursive function used by topologicalSort

    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

                # Push current vertex to stack which stores result
        stack.insert(0, v)

        # The function to do Topological Sort. It uses recursive

    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

                # Print contents of the stack

        topo_alphabet = []
        for search_index in stack:
            for temps, index in topo_dict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                if index == search_index:
                    topo_alphabet.append(temps)
        return topo_alphabet


def createTopoDict(temp_dict):
    i = 0
    topo_dict = {}
    for temps in temp_dict:
        topo_dict[temps] = i
        i += 1
    return topo_dict


if __name__ == '__main__':
    hint = numpy.array([['t', 'c', 'k', 's', 'x', 'f', 'b', 'r', 'a', 'v', 'h', 'i', 'g',
                         'p', 'o'],
                        ['t', 'c', 'l', 'u', 's', 'z', 'f', 'r', 'a', 'h', 'e', 'i', 'j',
                         'q', 'g'],
                        ['w', 't', 'l', 'u', 'k', 's', 'n', 'f', 'm', 'a', 'v', 'h', 'i',
                         'g', 'p'],
                        ['t', 'c', 'u', 's', 'z', 'm', 'r', 'a', 'y', 'v', 'h', 'e', 'q',
                         'g', 'p'],
                        ['w', 'c', 'l', 'u', 's', 'f', 'b', 'm', 'y', 'v', 'h', 'i', 'q',
                         'g', 'o'],
                        ['w', 't', 'c', 'k', 'f', 'b', 'm', 'r', 'h', 'e', 'i', 'j', 'q',
                         'g', 'o'],
                        ['w', 't', 'c', 'u', 'k', 's', 'z', 'x', 'b', 'm', 'h', 'e', 'i',
                         'g', 'p'],
                        ['w', 't', 'c', 'k', 's', 'n', 'b', 'm', 'r', 'v', 'h', 'j', 'q',
                         'p', 'o'],
                        ['w', 't', 'c', 'u', 's', 'z', 'f', 'b', 'm', 'a', 'y', 'e', 'q',
                         'g', 'o'],
                        ['c', 'l', 'u', 'k', 's', 'z', 'n', 'f', 'b', 'r', 'a', 'y', 'v',
                         'e', 'i'],
                        ['t', 'c', 'l', 'k', 's', 'z', 'f', 'b', 'm', 'r', 'a', 'e', 'i',
                         'g', 'p'],
                        ['w', 'c', 'l', 'u', 'k', 's', 'x', 'n', 'f', 'b', 'a', 'y', 'i',
                         'j', 'q'],
                        ['w', 't', 'u', 'z', 'x', 'n', 'f', 'a', 'y', 'e', 'i', 'q', 'g',
                         'p', 'o'],
                        ['w', 't', 'u', 'k', 'z', 'x', 'n', 'b', 'r', 'y', 'h', 'j', 'q',
                         'g', 'o'],
                        ['w', 't', 'c', 'l', 'u', 'k', 'n', 'a', 'y', 'h', 'e', 'j', 'q',
                         'p', 'o']])

    hint2 = numpy.array([['a', 'b'], ['b', 'c'], ['c', 'd']])

    temp_dict = create_dict(hint)
    hint_list = create_list(hint)
    alphabet = find_alphabet(temp_dict, hint_list)
    print("Using iterative method: ")
    print(alphabet)
    print(len(alphabet))
    print("Complexity O(n^2 * e)")

    # Topological sorting
    topo_dict = createTopoDict(temp_dict)
    hint_list = create_list(hint)
    g = Graph(len(topo_dict))
    for x in range (0, len(hint_list)):
        for y in range (0, len(hint_list[x])-1):
            g.addEdge(topo_dict.get(hint_list[x][y]), topo_dict.get(hint_list[x][y+1]))

    print("Following is a Topological Sort of the given graph:")
    print(g.topologicalSort())
    print("Topological sort is complexity O(V+E)")
