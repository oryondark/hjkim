```python
# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
    threshold = 0.6
    count = 0
    
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
  
    i = 0 # index for txt[] 
    while i < N: 
        matched_rank = ""
        if pat[j] == txt[i]: 
            i += 1
            j += 1
            count += 1
            
        if j == M: 
            matched_rank = "Found pattern at index " + str(i-j) + "\n"
            j = lps[j-1]

        # mismatch after j matches 
        if i < N and pat[j] != txt[i]:
            ## just added!!, so you can not consider for increased time-complexity.
            if (j/M) >= threshold:
                matched_rank = "Found Matched >=60 but <=100 at index " + str(i-j) + "\n"
                
            print(matched_rank, end='')                
            count = 0
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
```


```python
def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1
```

# Fundemantal KMP Algorithm


```python
txt = "ABCDEFGABCGGGGGABCDE"
pat = "ABCD"
KMPSearch(pat, txt) 
  
# This code is contributed by Bhavya Jain 
```

    Found pattern at index 0
    Found Matched >=60 but <=100 at index 7
    Found pattern at index 15


# Secondary proposed Algorithm for matched rank
KMP Algorithm can be proposed to compute a matched rank if you want rate of resamble pattern & original.


```python

```
