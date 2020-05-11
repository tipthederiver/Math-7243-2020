#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[6]:


import pandas as pd
from ipywidgets import IntProgress
from ipywidgets import HBox
from ipywidgets import Label
from IPython.display import display

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ipyvolume as ipv

import models


# # Plot difference between 3d Segmentations using MPL
# 
# Do not use this unless you really like the aesthetics of matplotlib. 

# In[7]:


def plt_differences_MPL(y_pred,y):
    y_p = np.round(y_pred[:,:,:,0])

    m = np.multiply(y_p,1-y);
    n = np.multiply(1-y_p,y);
    q = np.multiply(y_p,y);

    fig = plt.figure(figsize=(10,10))
    ax = fig.gca(projection='3d')
    print("Ploting", int(np.sum(q)) ,"True Positives")
    ax.voxels(q, alpha=.2,facecolor='C0');
    print("Ploting", int(np.sum(m)) ," False Positives")
    ax.voxels(m, alpha=.2,facecolor='C1');
    print("Ploting", int(np.sum(n)) ," False Negatives")
    ax.voxels(n, alpha=.2,facecolor='C2');
    
    return {"tp": int(np.sum(q)), "fp": int(np.sum(m)), "fn":int(np.sum(n))}


# # Compare segments and models

# In[8]:


def compared_segments(y_true,y_pred):
    y_true = y_true.astype('float32')
    y_pred = y_pred.astype('float32')
    loss_summary = {
        'IoU Coefficient': iou_coeff(y_true,y_pred).numpy(),
        'IoU Loss': iou_loss(y_true,y_pred).numpy(),
        'Binary Crossentropy IoU': bce_iou_loss(y_true,y_pred).numpy(),
        'DICE Coefficient': dice_coeff(y_true,y_pred).numpy(),
        'DICE Loss': dice_loss(y_true,y_pred).numpy(),
        'Binary Crossentropy DICE': bce_dice_loss(y_true,y_pred).numpy()
    }
    return loss_summary

def compare_models(data_gen, model_2d, model_3d=None):
    f = IntProgress(min=0, max=data_gen.epochs)
    l = Label("0/" + str(data_gen.epochs))
    H = HBox([f, l])
    display(H) # display the bar and label
    
    output = pd.DataFrame()

    for i in range(data_gen.epochs):
        X,y = data_gen.__getitem__(i)
        y_pred = model_2d.predict(X[0].reshape(80,120,120,1))
        output = output.append(compared_segments(y_pred,y[0]), ignore_index=True)
        
        # Update Progress Bar
        f.value += 1
        l.value = str(f.value) + "/" + str(data_gen.epochs)
        
    return output

