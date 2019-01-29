# Usage:
1) opening the file "collection.py"
2) change variable "root" value to your images path.
3) Run
>>> get_all_dataset()

4) then import Convolution_Cluster_viaPCA
5) Run
>>> kmeans_pca = kmeans_via_pca()
>>> kmeans_pca.learn(dataset)

6) In this code help you flatten a features
7) start prediction
```python
for m in os.listdir(test_image_path):
    path = os.path.join(test_image_path, m)
    for k in os.listdir(path):
        img = cv.imread( os.path.join(path, k) )
        res = kmeans_pca.predict(img)
```

7) Thank you
