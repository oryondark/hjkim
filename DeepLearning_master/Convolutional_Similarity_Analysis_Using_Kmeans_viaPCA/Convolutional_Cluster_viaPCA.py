'''
Implemented by Oak Ridge National Laboratory.
The resemble code create by hjkim on Bigdata Laboratory in Kookmin Univ.

Using Scikit-learn and Torch-framework
'''
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data
import cv2 as cv
import numpy as np


'''
Please, note that You have to implement the convolution network model or resemble that code

1) Instance to kmeans_via_pca class
2) Generates to input data set and into the model
3) Generating Convolutional features over model inputs to learn method
4) then, you can call predict method which is that can get a result clustering label for test data.
5) If you like to do using kmeans instance of scikit-learn, just call refer_to_kmeans method.
'''
class kmeans_via_pca():
    '''
    The class has to denoting, comp is to reduce components, cluster is the number of k.
    '''
    def __init__(self, comp=256, cluster=20):
        super(kmeans_via_pca, self).__init__()

        #K means Cluster Algorithm
        self._kmeans = KMeans(init="k-means++", n_clusters=cluster, n_init=10)
        #Principal Component Analysis
        self._pca = PCA(n_components=comp)


    def _transform_(self, reductions):
        transform = self._kmeans.fit_transform(reductions)

    '''
    Training method that is start Cluster with PCA
    Kemans needs 1D, then generates flattened list.
    '''
    def learn(self, trained_dataset):
        reducted_list = []
        for i in range(0,len(trained_dataset)):
            reductions = self._pca.fit_transform(trained_dataset[i])
            reducted_list.append(np.array(reductions).flatten())

        # You can get a cluster result
        self._transform_(reducted_list)

    '''
    It's prediction method

    If you directly have a got image frame over opencv image reader,
    follow method can be convert to tensor.
    '''
    def predict(self, img):
        if str(type(img)).find("torch.Tensor") < 1:
            #print("Not torch Tensor")
            img = cv.resize(img, (64, 64), interpolation = cv.INTER_AREA)
            img = img.astype(np.float32)
            cv.normalize(img, img, 0, 1, cv.NORM_MINMAX)
            img = np.transpose(img, [2,0,1])
            img = torch.Tensor(img)

        _, _, conv1 = model(torch.unsqueeze(img,0).cuda())
        conv1 = conv1.cpu().detach().numpy().squeeze(0)

        reshape = []
        for i in range(0, len(conv1)):
            reshape.append(conv1[i].flatten())

        reduction = self._pca.fit_transform(np.array(reshape))

        #start predict.
        #print(np.array([np.array(reduction).flatten()]).shape)
        return self._kmeans.predict([np.array(reduction).flatten()])

    """
    In this method call, You can that the method is kmeans inference model.
    """
    def refer_to_kmeans(self):
        return self._kmeans
