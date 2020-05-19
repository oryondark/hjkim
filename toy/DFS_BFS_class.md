```python
from collections import defaultdict
class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addNode(self, nodes):
        #무향그래프
        self.graph[nodes[0]].append(nodes[1])
        self.graph[nodes[1]].append(nodes[0])
    
    def getGraph(self):
        return self.graph
    
    def bfs(self, st_node, n):
        visited = []
        queue = []
        table = [0] * (n+1)
        queue.append(st_node)
        visited.append(st_node)
        
        #table[st_node] = 0
        while queue:
            node = queue.pop(0)
            next_nodes = self.graph[node]
            
            for next_node in next_nodes:
                if (next_node in visited) != True:
                    table[next_node] = table[node] + 1
                    queue.append(next_node)
                    visited.append(next_node)
        print(visited)
        return table
    
    def _dfs(self, node, visited):
        visited.append(node)
        next_nodes = self.graph[node]
        
        for next_node in next_nodes:
            if (next_node in visited) != True:
                self._dfs(next_node, visited)
        
        
    def dfs(self, st_node):
        visited = []
        self._dfs(st_node, visited)
        print(visited)
        
                
def solution(n, edges):
    #if len(edges) == 2:
    #    return 1
    graph = Graph()
    answer = 0
    for node in edges:
        graph.addNode(node)
    #print(graph.getGraph())
    table = graph.bfs(1, n)
    max_value = max(table)
    #print(table)
    for maximum in table:
        if maximum == max_value:
            answer += 1
        
    return answer
```


```python
def demo(n, edges):
    graph = Graph()
    answer = 0
    for node in edges:
        graph.addNode(node)
    graph.bfs(1, n)
    graph.dfs(1)

edge_nodes = [
                [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]],
                [[1,3],[1,5]],
                [[3,2],[2,1],[2,5],[2,4],[1,4],[1,2]]
             ]
n = 6
demo(n, edge_nodes[0])
```

    [1, 3, 2, 6, 4, 5]
    [1, 3, 6, 4, 2, 5]



```python

```
