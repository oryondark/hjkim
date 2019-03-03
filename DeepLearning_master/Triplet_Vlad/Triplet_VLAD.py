import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data
import cv2 as cv
import numpy as np

# Include that I was download Embedding Net of VLAD to server.
# If you want to see the original source code, please that let you go to link below.
# https://arxiv.org/pdf/1511.07247 : NetVLAD paper link
# https://github.com/lyakaap/NetVLAD-pytorch : original source code
from netvlad import NetVLAD
from netvlad import EmbedNet
from netvlad import TripletNet

# cusotm dataloader
from customDataLoader3 import DataLoader

'''
Dirty code but you can understood the generator way.
'''
def data_generator(T=True, shf=True):
    '''
    Python Generator
    *  if you do run this line, you can get a data like the example
    example:
    gen = data_generator(True, 10, True)
    
    print(next(gen)) # get data index number 1
    print(next(gen)) # get data index number 2
    
    * as well as, you can uses with loop by enumerate
    for i, data in enumerate(gen, 0):
        print(data)
    '''

    train_loader = torch.utils.data.DataLoader( DataLoader(T, default_image_loader), batch_size = 1, shuffle = shf)
    pos_loader = torch.utils.data.DataLoader( DataLoader(T, default_image_loader), batch_size= 1, shuffle = shf)
    neg_loader = torch.utils.data.DataLoader( DataLoader(T, default_image_loader), batch_size= 1, shuffle= shf)

    count = 0
    for anc_data, anc_label in train_loader:
        for pos_data, pos_label in pos_loader:
            if anc_label == pos_label:
                p = pos_data
                pl = pos_label
                for neg_data, neg_label in neg_loader:
                    if anc_label != neg_label:
                        nl = neg_label
                        n = neg_data
                        break
                break
                count += 1

        # return anchor, anchor label, positive, negative, positive and negative label
        yield anc_data, anc_label, p, n, pl, nl


"""
AlexNet
Pytorch basic alexnet, but i did fine-tune for classification layer, just for testing.
"""
class AlexNet(nn.Module):

    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=4, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.batchnorm = nn.BatchNorm2d(128)
        self.classifier = nn.Sequential(
            #nn.Dropout(),
            #nn.Linear(128 * 6 * 6, 2048),
            #nn.ReLU(inplace=True),
            #nn.Dropout(),
            #nn.Linear(2048, 1024),
            #nn.ReLU(inplace=True),
            #nn.Linear(1024, num_classes),
            nn.Linear(128*6*6,2048),
            nn.ReLU(inplace=True),
            nn.Linear(2048,1024),
            nn.ReLU(inplace=True),
            nn.Linear(1024,num_classes),
        )

    def forward(self, x):
        features = self.features(x)
        x = self.avgpool(features)
        #features = self.batchnorm(x)
        x = x.view(x.size(0), 256 * 6 * 6)
        x = self.classifier(x)
        return x, features

#instance pre-trained model.
model = AlexNet(128)
PATH = "./checkpoint_newSave/99_20190224_alexnet.pt"
model = torch.load(PATH)
model.cuda() # GPU mode 



# Define model for embedding
net_vlad = NetVLAD(num_clusters=21, dim=256, alpha=1.0)
embednet = EmbedNet(model, net_vlad).cuda()
triplet = TripletNet(embednet).cuda()

print(triplet)
'''
TripletNet(
  (embed_net): EmbedNet(
    (base_model): AlexNet(
      (features): Sequential(
        (0): Conv2d(3, 64, kernel_size=(4, 4), stride=(4, 4), padding=(2, 2))
        (1): ReLU(inplace)
        (2): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
        (3): Conv2d(64, 192, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
        (4): ReLU(inplace)
        (5): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
        (6): Conv2d(192, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (7): ReLU(inplace)
        (8): Conv2d(384, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (9): ReLU(inplace)
        (10): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (11): ReLU(inplace)
        (12): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
      )
      (avgpool): AdaptiveAvgPool2d(output_size=(6, 6))
      (classifier): Sequential(
        (0): Dropout(p=0.5)
        (1): Linear(in_features=9216, out_features=2048, bias=True)
        (2): ReLU(inplace)
        (3): Dropout(p=0.5)
        (4): Linear(in_features=2048, out_features=2048, bias=True)
        (5): ReLU(inplace)
        (6): Linear(in_features=2048, out_features=21, bias=True)
      )
    )
    (net_vlad): NetVLAD(
      (conv): Conv2d(256, 21, kernel_size=(1, 1), stride=(1, 1))
    )
  )
)
'''

#pytorch triplet_margin_loss function
#https://pytorch.org/docs/stable/_modules/torch/nn/modules/loss.html#TripletMarginLoss
criterion = nn.TripletMarginLoss(margin=0.1, p=2)
def vlad_train(epochs, learning_rate):
	'''
	It is PIPLEIE function
	- vlad_train 
		- train_epoch
			- embedding network
			- vlad network
		- test_peoch
			same
	'''

	#optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.95)
	optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(0,epochs):
        train_epochs(epoch, optimizer)
        test_epochs(epoch)

def train_epochs(epoch, optimizer):

    if (epoch % 100) == 99:
        print(epoch, " : model save!")
        #torch.save(model, "./checkpoint_newSave/" + str(epoch) + "_" + "20190224_alexnet.pt")
    running_loss = 0.0

    # data generator
    gen = data_generator(True)

    for i, data in enumerate(gen, 0):
        targets = []
        images, labels, pos, neg, pos_label, neg_label = data
        features, pos_fit, neg_fit = triplet(images.cuda(), pos.cuda(), neg.cuda())

        targets = onehot[labels]
        targets = targets.argmax(dim=1) # Uses of crossEntropy
        loss = criterion(features, pos_fit, neg_fit)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        #print(loss.item())
        running_loss += loss.item()
    print("Training running loss : {}".format(running_loss / (i + 1)))
    

def test_epochs(epoch):

    if (epoch % 100) == 99:
        print(epoch, " : model save!")
        #torch.save(model, "./checkpoint_newSave/" + str(epoch) + "_" + "20190224_alexnet.pt")
    running_loss = 0.0

    # data generator
    gen = data_generator(False)


    for i, data in enumerate(gen, 0):
        targets = []
        images, labels, pos, neg, pos_label, neg_label = data

        #print(labels, pos_label, neg_label)
        # prediction
        #features = embednet(images.cuda())
        #pos_fit = embednet(pos.cuda())
        #neg_fit = embednet(neg.cuda())
        features, pos_fit, neg_fit = triplet(images.cuda(), pos.cuda(), neg.cuda())
        loss = criterion(features, pos_fit, neg_fit)
        running_loss += loss.item()
    print("Testing running loss : {}".format(running_loss / (i + 1))) 



lr = 1e-3 # 1 * 0.0001
for i in range(1,5): # 100 * 5 = 500 iteration
    #lr = lr / 10 # hard train
    if i == 3:
        vlad_train(100, lr, getting_fisher_vec=True)
