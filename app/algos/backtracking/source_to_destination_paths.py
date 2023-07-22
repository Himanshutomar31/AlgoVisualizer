from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):
        visited[u] = True
        path.append(u)

        if u == d:
            print(path)
        else:
            for i in self.graph[u]:
                if not visited[i]:
                    self.printAllPathsUtil(i, d, visited, path)

        path.pop()
        visited[u] = False

    def printAllPaths(self, s, d):
        visited = [False] * self.V
        path = []
        self.printAllPathsUtil(s, d, visited, path)

def main():
    # Create a graph with 4 vertices
    g = Graph(4)

    # Add edges to the graph
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    # Define the source and destination vertices for finding paths
    s = 2 ; d = 3

    # Print all different paths from the source to the destination
    print("Following are all different paths from %d to %d:" % (s, d))
    g.printAllPaths(s, d)

if __name__ == "__main__":
    main()
