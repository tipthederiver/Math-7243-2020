#!/usr/bin/env python
# coding: utf-8

# # Data Handling Common Imports


import os 
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt 
from tensorflow import keras
import matplotlib.image as mpimg

# # Data Generator
# 
# Code from https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly.
# 
# Usage: 
# 
# files = ['ID_0a336e630', 'ID_0ba79c0ef', 'ID_0bc7199c6']
# path = '../Example Bucket'
# data_gen = DataGenerator(folder=path,batch_size=1, file_list=files, shuffle=False)


class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self, folder, file_list, batch_size=128, dim=(512, 512), shuffle=True):
        'Initialization'
        self.dim = dim
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.folder = folder + "/"
        
        ## Get list of applicable filenames:
        self.files = file_list
        self.list_IDs = list(range(len(self.files)))
        
        self.on_epoch_end()

    def __len__(self):
        'Denotes the number of batches per epoch'
        return int(np.floor(len(self.list_IDs) / self.batch_size))

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]

        # Find list of IDs
        list_IDs_temp = [self.list_IDs[k] for k in indexes]

        # Generate data
        X, y = self.__data_generation(list_IDs_temp)

        return X, y

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, list_IDs_temp):
        'Generates data containing batch_size samples' # X : (n_samples, *dim, n_channels)
        # Initialization
        X = np.empty(((self.batch_size)*2, *self.dim,4))
        y = np.empty(((self.batch_size)*2, *self.dim,1))
        L = self.batch_size
        
        # Folders:
        Fd = ['brain_bone_window/',
              'brain_window/',
              'max_contrast_window/',
              'subdural_window/']

        # Generate data
        for i, ID in enumerate(list_IDs_temp):
            for j in range(4):
                # Store images and horizontal flip
                img = mpimg.imread(self.folder + Fd[j] + self.files[ID] + '.jpg')[:,:,0]
                X[i,:,:,j] = img
                X[L + i,:,:,j] = np.flip(img,1)

            # Store segment and horizontal flip
            seg = np.load(self.folder + "segs/seg_" + self.files[ID] + '.npz')['arr_0']
            y[i,:,:,0] = seg
            y[L + i,:,:,0] = np.flip(seg,1)

        return X, y
