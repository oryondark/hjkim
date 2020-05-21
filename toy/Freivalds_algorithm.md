```python
#freivald's algorithm 
def vectorize(vectorize, mat, rv, k_len):
    for i in k_len:
        for j in k_len:
            vectorize[i] = vectorize[i] + (mat[i][j] * rv[j])
    return vectorize

def sub(Av, Cv, k):
    subtracted_vector = []
    for i in k:
        subtracted_vector.append(Av[i] - Cv[i])
    
    return subtracted_vector

def frvd(k, A, B, C):
    k_len = range(0, k)
    rv = [1] * k
    
    Bxr = [0] * k
    vectorize(Bxr, B, rv, k_len)
    print("B vectorized : ", Bxr)
    
    Cxr = [0] * k
    vectorize(Cxr, C, rv, k_len)
    print("C vectorized : ", Cxr)
    
    AxBxr = [0] * k
    vectorize(AxBxr, A, Bxr, k_len)
    print("A Vectorized : ", AxBxr)
    
    print(sub(AxBxr, Cxr, k_len))
    
```


```python
A = [[2,3], [3,4]]
B = [[1,0], [1,2]]
C = [[6, 5], [8, 7]]
k = 2
frvd(k, A,B,C)

A = [[2,5], [3,4]]
B = [[1,0], [1,2]]
C = [[6, 5], [8, 7]]
k = 2
frvd(k, A,B,C)
```

    B vectorized :  [1, 3]
    C vectorized :  [11, 15]
    A Vectorized :  [11, 15]
    [0, 0]
    B vectorized :  [1, 3]
    C vectorized :  [11, 15]
    A Vectorized :  [17, 15]
    [6, 0]



```python

```
