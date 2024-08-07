from keras.models import Sequential
from keras.layers import Dense,Activation,Conv2D,MaxPooling2D,Flatten,Dropout,BatchNormalization
from keras.datasets import mnist
from keras.utils import np_utils
from keras.optimizers import Adam

def AlexNet(input_shape=(224,224,3), output_shape=2):
    model = Sequential() # 空的
    # 48个卷积核 尺寸11x11 步长4x4 不填充
    model.add(Conv2D(filters=48, kernel_size=(11, 11), strides=(4, 4), padding='valid',
                     input_shape=input_shape, activation='relu'))
    model.add(BatchNormalization())
    # 最大池化
    model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='valid'))

    model.add(Conv2D(filters=128, kernel_size=(5, 5), strides=(1, 1), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='valid'))
    model.add(Conv2D(filters=192, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
    model.add(Conv2D(filters=192, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
    model.add(Conv2D(filters=192, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='valid'))
    # 展开成一维
    model.add(Flatten())

    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(output_shape, activation='softmax'))

    return model

