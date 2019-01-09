
# Data Augmentation

**Generating new training instances from exsiting ones**<br>
![image.png](https://github.com/oryondark/-/blob/master/DeepLearning_master/Augmentation_Tutorial/스크린샷%202019-01-09%20오후%201.26.13.png)


**Data augmentation is usually done as part of your input data pipeline that feeds your model while training. Randomly, instead of feeding an original training image, you will instead apply some augmentations to change it.<br>**

First, you have to understand data augmentation.<br>
Why use augmentation? that is one problem just.
<br>
Assume you have image-data but is small amount. you can't collect to any method.<br>
That's to solve, does proposal to you with using Data Augmentation Tech.<br>

At recently, GPU and Hardware for the save technologies extreamly growth up, Data augmentation has been important very.
So, we will learn to a number of way below.

- Resizing ( that is basic for Augmentation )
- Scaling ( same the resizing method )
- Translation
- Rotation
- Flipping
- Adding a noise

**Note that in this section we don't use Resizing Method. Because basically this method did when input uniform data to the model.**<br>


```python
# import modules for image preprocessing
import cv2 as cv
import matplotlib.pyplot as plt
import os, sys
```


```python
#image parse in directory

root_dir_path = './crop/' #target images directory
root_dir = os.listdir(root_dir_path)
print(root_dir)
```

    ['0019_Geometric', '0016_Leopard', '0007_Gingham', '0003_Regimental stripe', '0014_Paisely', '0005_Argyle', '0020_Honeycomb', '0015_Camoflage', '0017_Greek Key', '0010_Tartan', '0006_Dalmatians', '0001_Pinstripe', '0004_Barcode stripe', '0009_Windowpane', '0012_Houndstooth', '0002_Chevron', '0011_polka dot', '0008_Floral', '0013_Herringbone', '0018_Zebra']


# Create Save method by openCV
**You have to save in a storage if image precessing done.**


```python
def save(keyPath, file_name, cv_img, rate, type):
    
    '''
    save method need to save before image preprocessing.
    It has five arguments and requirement all.
    
    keyPath is root path of original image.
    file_name is original image file name
    cv_img is whole signal of the image
    rate is for scale value
    
    '''
    if os.path.isdir(keyPath) != True:
        os.mkdir(keyPath)
    
    saved_name = os.path.join(keyPath,"{}{}.{}".format(file_name.split('.')[0], type, 'jpg'))
    #print(saved_name)
    cv.imwrite(saved_name, cv_img)
```

# 1. Scaling
**Scaliling does not changed size, but that is zoom in or out on top of the image.**<br>
**Interpole method**<br>
*INTER_NEAREST* - a nearest-neighbor interpolation<br>
*INTER_LINEAR* - a bilinear interpolation (used by default)<br>
*INTER_AREA - resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.*<br>
*INTER_CUBIC* - a bicubic interpolation over 4x4 pixel neighborhood<br>
*INTER_LANCZOS4* - a Lanczos interpolation over 8x8 pixel neighborhood<br>


```python
def augmente(keyName, rate=None, if_scale=False):
    
    saved_dir = "./augmentation_images"
    keyPath = os.path.join(root_dir_path, keyName) # keypath direct to root path
    print(keyPath)
    datas = os.listdir(keyPath)
    data_total_num = len(datas)
    print("Overall data in {} Path :: {}".format(keyPath, data_total_num))
    
    
    try:
        for data in datas:
            type = "_scale_"
            data_path = os.path.join(keyPath, data)
            img = cv.imread(data_path)
            shape = img.shape
            ###### data rotate ######
            data_rotate(saved_dir, data, img, 20, "_rotate_", saving_enable=True)
            
            ###### data flip and save #####
            data_flip(saved_dir, data, img, rate, 1, False) # verical random flip
            data_flip(saved_dir, data, img, rate, 0, False) # horizen random flip
            data_flip(saved_dir, data, img, rate, -1, False) # both random flip
            
            ####### Image Scale #########
            if if_scale == True:
                print("Start Scale!")
                x = shape[0]
                y = shape[1]          
                f_x = x + (x * (rate / 100))
                f_y = y + (y * (rate / 100))
                cv.resize(img, None, fx=f_x, fy=f_y, interpolation = cv.INTER_CUBIC)

                img = img[0:y, 0:x]
                
                save(saved_dir, data, img, rate, type)
            ############################
                        
        #plt.imshow(img)
        #plt.show()
        return "success"
    
    except Exception as e:
        print(e)
        return "Failed"
```

# 2. Flip
**This method has two solution**<br>
1) Vertical flip<br>
2) horizen flip<br>


```python
def data_flip(saved_dir, data, img, rate, type, saving_enable=False):
    
    img = cv.flip(img, type)
    try:
        if type == 0:
            type = "_horizen_"
        elif type == 1:
            type = "_vertical_"
        elif type == -1:
            type = "_bothFlip_"
        
        if saving_enable == True:
            save(saved_dir, data, img, rate, type)
    
    except Exception as e:
        print(e)
        return "Failed"
```

# 3. Rotate
**Function can uses of getrotationmatrix2d() if you use opencv, Note that you have to follow the usage of parameter.**<br>
1) center – Center of the rotation in the source image.<br>
2) angle – Rotation angle in degrees. Positive values mean counter-clockwise rotation (the coordinate origin is assumed to be the top-left corner).<br>
3) scale – Isotropic scale factor.<br>
4) map_matrix – The output affine transformation, 2x3 floating-point matrix.<br><br>

![image.png](attachment:image.png)<br><br>


```python
def data_rotate(saved_dir, data, img, rate, type, saving_enable=False):
    
    xLength = img.shape[0]
    yLength = img.shape[1]
    
    try:
        rotation_matrix = cv.getRotationMatrix2D((xLength/2 , yLength/2), rate, 1)
        img = cv.warpAffine(img, rotation_matrix, (xLength, yLength))
        #print(img.shape)        
        if saving_enable == True:
            save(saved_dir, data, img, rate, type)
        
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"
        

```

# Create Entry Point function


```python
def main_TransformImage(keyNames):
    try:
        for keyname in keyNames:
            
            #print(keyname)
            augmente(keyname, 20) # scaling

        return "Augment Done!"
    except Exception as e:
        print(e)
        return "Augment Error!"
```


```python
main_TransformImage(root_dir)
```

    ./crop/0019_Geometric
    Overall data in ./crop/0019_Geometric Path :: 314
    ./crop/0016_Leopard
    Overall data in ./crop/0016_Leopard Path :: 770
    ./crop/0007_Gingham
    Overall data in ./crop/0007_Gingham Path :: 947
    ./crop/0003_Regimental stripe
    Overall data in ./crop/0003_Regimental stripe Path :: 434
    ./crop/0014_Paisely
    Overall data in ./crop/0014_Paisely Path :: 311
    ./crop/0005_Argyle
    Overall data in ./crop/0005_Argyle Path :: 659
    ./crop/0020_Honeycomb
    Overall data in ./crop/0020_Honeycomb Path :: 411
    ./crop/0015_Camoflage
    Overall data in ./crop/0015_Camoflage Path :: 432
    ./crop/0017_Greek Key
    Overall data in ./crop/0017_Greek Key Path :: 206
    ./crop/0010_Tartan
    Overall data in ./crop/0010_Tartan Path :: 345
    ./crop/0006_Dalmatians
    Overall data in ./crop/0006_Dalmatians Path :: 434
    ./crop/0001_Pinstripe
    Overall data in ./crop/0001_Pinstripe Path :: 456
    ./crop/0004_Barcode stripe
    Overall data in ./crop/0004_Barcode stripe Path :: 450
    ./crop/0009_Windowpane
    Overall data in ./crop/0009_Windowpane Path :: 513
    ./crop/0012_Houndstooth
    Overall data in ./crop/0012_Houndstooth Path :: 448
    ./crop/0002_Chevron
    Overall data in ./crop/0002_Chevron Path :: 676
    ./crop/0011_polka dot
    Overall data in ./crop/0011_polka dot Path :: 296
    ./crop/0008_Floral
    Overall data in ./crop/0008_Floral Path :: 945
    ./crop/0013_Herringbone
    Overall data in ./crop/0013_Herringbone Path :: 504
    ./crop/0018_Zebra
    Overall data in ./crop/0018_Zebra Path :: 467





    'Augment Done!'


