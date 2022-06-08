# coding: utf-8
import keras
from keras import backend as K

K.set_image_dim_ordering("tf")

import numpy as np

from keras.layers import (
    UpSampling1D,
    MaxPooling1D,
    BatchNormalization,
    Dense,
    MaxPooling1D,
    Conv1D,
)


def encoder(input_layer):
    conv1 = Conv1D(32, 2, activation="relu", padding="same")(
        input_layer
    )  # 28 x 28 x 32
    conv1 = BatchNormalization()(conv1)
    conv1 = Conv1D(32, 2, activation="relu", padding="same")(conv1)
    conv1 = BatchNormalization()(conv1)
    pool1 = MaxPooling1D(pool_size=1, strides=2)(conv1)  # 14 x 14 x 32
    conv2 = Conv1D(64, 2, activation="relu", padding="same")(pool1)  # 14 x 14 x 64
    conv2 = BatchNormalization()(conv2)
    conv2 = Conv1D(64, 2, activation="relu", padding="same")(conv2)
    conv2 = BatchNormalization()(conv2)
    """
    pool2 = MaxPooling1D(pool_size=1, strides=2)(conv2) #7 x 7 x 64
    conv3 = Conv1D(128, 2, activation='relu', padding='same')(pool2) #7 x 7 x 128 (small and thick)
    conv3 = BatchNormalization()(conv3)
    conv3 = Conv1D(128, 2, activation='relu', padding='same')(conv3)
    conv3 = BatchNormalization()(conv3)
    conv4 = Conv1D(256, 2, activation='relu', padding='same')(conv3) #7 x 7 x 256 (small and thick)
    conv4 = BatchNormalization()(conv4)
    conv4 = Conv1D(256, 2, activation='relu', padding='same')(conv4)
    conv4 = BatchNormalization()(conv4)
    """
    return conv2


def decoder(conv2):
    conv5 = Conv1D(128, 2, activation="relu", padding="same")(conv2)  # 7 x 7 x 128
    conv5 = BatchNormalization()(conv5)
    conv5 = Conv1D(128, 2, activation="relu", padding="same")(conv5)
    conv5 = BatchNormalization()(conv5)
    conv6 = Conv1D(64, 2, activation="relu", padding="same")(conv5)  # 7 x 7 x 64
    conv6 = BatchNormalization()(conv6)
    """
    conv6 = Conv1D(64, 2, activation='relu', padding='same')(conv6)
    conv6 = BatchNormalization()(conv6)
    up1 =   UpSampling1D(2)(conv6) #14 x 14 x 64
    conv7 = Conv1D(32, 2, activation='relu', padding='same')(up1) # 14 x 14 x 32
    conv7 = BatchNormalization()(conv7)
    conv7 = Conv1D(32, 2, activation='relu', padding='same')(conv7)
    conv7 = BatchNormalization()(conv7)
    """
    up2 = UpSampling1D(2)(conv6)  # 28 x 28 x 32
    decoded = Conv1D(1, 2, activation="sigmoid", padding="same")(up2)  # 28 x 28 x 1

    return decoded
