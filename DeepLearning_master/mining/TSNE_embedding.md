### Load deep learning model


```python
import numpy as np
from sklearn.manifold import TSNE
from dl_model import Net
from PIL import Image
from PIL import ImageFile
import torch
import pickle
```


```python
model = pickle.load(open('model.pkl','rb'))
model.double()
```

### Crawling of the feature vector from your deep learning model


```python
#Test
x = np.random.rand(3, 64, 64)
x = torch.tensor([x])
```


```python
a, b = model(x)
```


```python
import os, sys
def normalize_minmax(input_x):
    input_x = np.abs((input_x - np.min(input_x)) / (np.min(input_x) - np.max(input_x)))
    return input_x

feature_vectors = []
feature_labels = []
def feature_crawling(img_folder):
    global feature_vectors
    dirs = os.listdir(img_folder)
    while dirs:
        pattern = dirs.pop(0)
        join = os.path.join(img_folder, pattern)
        try:
            if os.path.isdir(join):
                feature_crawling(join)
            else:
                img = Image.open(join)
                img = img.resize((64, 64))
                img = np.array(img)
                img = normalize_minmax(img)
                img = np.transpose(img, (2,0,1))
                img = np.array([img[2],img[1],img[0]])

                torch_img = torch.tensor([img])
                detected_lable, feature_v = model(torch_img)
                feature_vectors.append(feature_v.detach().cpu().numpy()[0])
                feature_labels.append(detected_lable.argmax().detach().cpu().numpy())
        except:
            print("occurs error : ", join)
```


```python
feature_crawling('pattern_img/crop')
```

### projection using T-SNE


```python
tsne_op = TSNE(n_components=2, random_state=0, verbose=1, perplexity=40, n_iter=300)
```


```python
tsne_emd = tsne_op.fit_transform(feature_vectors)
```


```python
tsne_emd.shape
```


```python
import matplotlib.pyplot as plt
def plot_embedding(X, Y, title=None):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    
    plt.figure()
    #ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(Y[i]),
                 color=plt.cm.Set1(Y[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})
        
    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)
    
    plt.savefig('TSNE_Result.pdf',format='pdf')
    plt.show()
```


```python
plot_embedding(tsne_emd, feature_labels,"Evaluate using T-SNE embedding")
```
