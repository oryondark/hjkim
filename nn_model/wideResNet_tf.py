import tensorflow
import tensorflow.keras
from tensorflow.keras.layers import Dense, Conv2D, BatchNormalization, Activation, Dropout
from tensorflow.keras.layers import AveragePooling2D, Input, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, LearningRateScheduler
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.regularizers import l2
from tensorflow.keras import backend as K
from tensorflow.keras.models import Model
print(tensorflow.__version__)

'''
layer  output  filter
conv1 32 x 32 3x3x16
conv2 32 x 32 3x3x16xfactor
conv3 16 x 16 3x3x32xfactor
conv4 8 x 8   3x3x64xfactor
avg   1 x 1   8x8
'''
def wideBlock(x, output_ch, dropout, stride):
    x = BatchNormalization()(x)
    x = Conv2D(output_ch, 3, padding="SAME", strides=1, activation="relu")(x)
    x = Dropout(dropout)(x)
    x = BatchNormalization()(x)
    x = Conv2D(output_ch, 3, padding="SAME", strides=stride, activation="relu")(x)
    return x

def wideLayer(x, output_ch, num_of_block, rate,stride):
    strides = [stride] + [1]*(num_of_block - 1)
    for i, s in enumerate(strides):
        y = wideBlock(x, output_ch, rate, s)
        if s != 1:
            o = Conv2D(output_ch, 1, padding="SAME", strides=stride)(x)
            y = tensorflow.keras.layers.add([o, y])
        y = Activation('relu')(y)
    return y


def ResNet(input_shape, depth, factor, num_classes):
    assert ((depth-4)%6 ==0), 'should be 6n+4'
    n = int((depth-4) / 6) # number of blocks
    outchannel_per_steps = [16*factor, 32*factor, 64*factor] # wide factors
    drop_rate = 0.3

    batch = Input(shape=input_shape) # inputs

    x = Conv2D(16, 3, strides=1, padding="SAME", input_shape=(None,32,32,3))(batch) # No use ReLU

    ##### Wide ResNet #####
    x = wideLayer(x, outchannel_per_steps[0], n, drop_rate, 1)
    x = wideLayer(x, outchannel_per_steps[1], n, drop_rate, 2)
    x = wideLayer(x, outchannel_per_steps[2], n, drop_rate, 2)
    #####     End     #####

    x = BatchNormalization()(x)
    x = AveragePooling2D(pool_size=8)(x)
    x = Flatten()(x)
    x = Dense(num_classes, activation='softmax')(x) # outputs
    model = Model(inputs=batch, outputs=x)

    return model
