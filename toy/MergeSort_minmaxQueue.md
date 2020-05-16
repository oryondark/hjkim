```python
import math
'''
Python에서 장렬 알고리즘이 제공되는
bisect를 사용하면 더욱 간편하게 할 수 있음
'''
class minmaxSortQueue(object):
    def __init__(self):
        self.nodes = list()
    
    #Merge sort        
    def _bin_insert(self, nodes, number):
        
        #Divide
        nodes_len = len(nodes)
        if nodes_len == 0:
            nodes.append(number)
            return nodes
        
        if nodes_len == 1:
            right = max(nodes[0], number)
            left = min(nodes[0], number)
            nodes[0] = left
            nodes.append(right)
            return nodes
            
        M = math.ceil(len(nodes)) - 1
        bin1 = nodes[M:]
        bin2 = nodes[:M]
        
        
        #Conquer
        if nodes[M] <= number:
            bin1 = self._bin_insert(bin1, number)
        else:
            bin2 = self._bin_insert(bin2, number)
        
        #Merge
        bin2.extend(bin1)
        return bin2
        
    def insert(self, number):
        self.nodes = self._bin_insert(self.nodes, number)
    
    def delete(self, number):
        if len(self.nodes) != 0:
            if number == -1:
                self.nodes.pop(0)

            elif number == 1:
                self.nodes.pop()
        
        
    def getQueue(self):
        return self.nodes
    
    def empty(self):
        if len(self.nodes) == 0:
            return True
        return False
```


```python
sortQueue = minmaxSortQueue()
```


```python
sortQueue.insert(100)
sortQueue.insert(20)
sortQueue.insert(10)
sortQueue.insert(7)
sortQueue.insert(6)
sortQueue.insert(3)
```


```python
sortQueue.getQueue()
```




    [3, 6, 7, 10, 20, 100]




```python

```
