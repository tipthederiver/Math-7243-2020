#!/usr/bin/env python
# coding: utf-8

# # Data Handling Common Imports

# In[22]:


import os 
import numpy as np
from ipywidgets import IntProgress
from ipywidgets import HBox
from ipywidgets import Label
from IPython.display import display
from matplotlib import pyplot as plt 
from tensorflow import keras


# # Display Train and Test Data

# In[19]:


def display_train_test(out_folder, dim="3D"):
    f, ax = plt.subplots(2,4,figsize=(10,5))
    ax = ax.ravel()

    train_files = [file for file in os.listdir(out_folder + "/train/imgs/") if file.endswith(".npz")]
    test_files = [file for file in os.listdir(out_folder + "/test/imgs/") if file.endswith(".npz")]

    tt = "/train"

    for i in range(8):
        if(i>5):
            tt = '/test'
            file = test_files[np.random.randint(len(test_files))]
        else:
            file = train_files[np.random.randint(len(train_files))]
        # Pick a random file

        print(out_folder + tt + "/imgs/" + file)
        img = np.load(out_folder + tt + "/imgs/" + file)['arr_0']
        seg = np.load(out_folder + tt + "/segs/" + file)['arr_0']
        
        if dim is "2D":
            #bounds = get_bounds(seg)
            #sl = int(np.round((bounds[0][0] + bounds[1][0])/2))

            masked = np.ma.masked_array(seg, seg==0.0)
            ax[i].imshow(img,cmap="Greys")
            ax[i].imshow(masked)
            ax[i].set_title(tt[1:])
            
        elif dim is "3D":
            bounds = get_bounds(seg)
            sl = int(np.round((bounds[0][0] + bounds[1][0])/2))
            
            masked = np.ma.masked_array(seg[sl,:], seg[sl,:]==0.0)
            ax[i].imshow(img[sl,:],cmap="Greys")
            ax[i].imshow(masked)
            ax[i].set_title(tt[1:])


# # Get Bounding Box from Segment

# In[17]:


# Get the bounding box for a segment

def get_bounds(seg):
    M = (np.max(np.where(seg)[0]),np.max(np.where(seg)[1]),np.max(np.where(seg)[2]))
    m = (np.min(np.where(seg)[0]),np.min(np.where(seg)[1]),np.min(np.where(seg)[2]))

    return[m,M]


# # Create New Directory if one does not exist

# In[18]:


def create_dir(new_dir):
    if not os.path.isdir(new_dir):
        try:
            os.mkdir(new_dir)
        except OSError:
            print ("Creation of the directory %s failed" % new_dir)
        else:
            print ("Successfully created the directory %s " % new_dir)
    else:
        print("Directory", new_dir, "already exists  exists")


# # Downsample Code
# 
# Usage: 
# 
#     (L,W,H) = downsample3D(img_folder, out_folder, crop = (42,122,41,161,24,144), downsample=2, dim="3D")
#     
# Note: `dim` must be set to `2D` or `3D`. Downsample is not used in this project, but we leave the code in. 

# In[20]:


def downsample(img_folder, out_folder, sample = True, split = .8, down_rate = 1, crop = None, dim="3D"):
    # Check if dim is properly defined
    if dim not in ["2D","3D"]:
        print("dim is not either 2D or 3D")
        return
    
    # Load all of the base filenames, ignoring all other files in directory
    base_files = [file for file in os.listdir(img_folder) if file.endswith("MR.npz")]
    
    # Check if the output directories exists. If not, create it. 
    
    create_dir(out_folder)
    create_dir(out_folder + "/train")
    create_dir(out_folder + "/test")
    create_dir(out_folder + "/train/imgs")
    create_dir(out_folder + "/train/segs")
    create_dir(out_folder + "/test/imgs")
    create_dir(out_folder + "/test/segs")
            
    # Set up progress bar.
    
    f = IntProgress(min=0, max=len(base_files))
    l = Label("Loading File")
    H = HBox([f, l])
    display(H) # display the bar and label
    
    # Set up the output folders
    
    out_fol_img = out_folder + "/train/imgs/"
    out_fol_seg = out_folder + "/train/segs/"
    tt = "Train: " # The label for the progress bar
    
    # If crop is not None, get the crop range:
    if not crop:
        a1 = b1 = c1 = 0
        (a2,b2,c2) = np.load(img_folder + "/" + base_files[0])['arr_0'].shape
    else:
        (a1,a2,b1,b2,c1,c2) = crop
        
    print("Cropping to ", a1,a2,b1,b2,c1,c2)
    
    # For each file, load both the file and segmentation in. Downsample both and output.
    
    ds = down_rate
    for n, file in enumerate(base_files):
        img = np.load(img_folder + "/" + file)['arr_0'][a1:a2,b1:b2,c1:c2]
        seg = np.load(img_folder + "/" + file[:-4] + "seg.npz")['arr_0'][a1:a2,b1:b2,c1:c2]
        

        if (n+1) > len(base_files)*split:
            out_fol_img = out_folder + "/test/imgs/"
            out_fol_seg = out_folder + "/test/segs/"
            tt = "Test: "
            
        for i in range(ds):
            for j in range(ds):
                for k in range(ds):
                    N = str(i + ds*j + (ds**2)*k)
                    ds_img = img[i::ds,j::ds,k::ds]
                    ds_seg = seg[i::ds,j::ds,k::ds]
                    
                    if dim is "3D":
                        np.savez_compressed(out_fol_img + file[:-4] + N + ".npz", ds_img)
                        np.savez_compressed(out_fol_seg + file[:-4] + N + ".npz", ds_seg)
                    elif dim is "2D":
                        for r in range(a2-a1):
                            np.savez_compressed(out_fol_img + file[:-4] + N + "_" + str(r) + ".npz", ds_img[r,:,:])
                            np.savez_compressed(out_fol_seg + file[:-4] + N + "_" + str(r) + ".npz", ds_seg[r,:,:])
                        
                    
        f.value += 1 # signal to increment the progress bar
        l.value = tt + file
        
      
    # Display a sample output if requested
    if sample:            
        display_train_test(out_folder,dim=dim)
                    
    ## Summerize preproccesing info
    
    f = ds**3
    
    print("Train Images:", int(f*np.floor(len(base_files)*split)))
    print("Test Images:", int(f*(len(base_files) - np.floor(len(base_files)*split))))
    print("Dimensions:", ds_img.shape)
    
    return ds_img.shape


# # Data Generator
# 
# Code from https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly.
# 
# Usage: 
# 
#     training_generator = DataGenerator(folder=out_folder,batch_size=1, tt = "train", dim=(120, 120))
#     testing_generator = DataGenerator(folder=out_folder,batch_size=1, tt = "test", dim=(120, 120), shuffle=False)
#     test_gen_3D = DataGenerator(folder=out_folder,batch_size=1, tt = "test", dim=(80,120, 120), shuffle=False)

# In[24]:


class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self, folder, batch_size=128, dim=(104, 88), shuffle=True, tt = "train"):
        'Initialization'
        self.dim = dim
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.tt = tt
        self.folder = folder + "/" + tt
        
        ## Get list of applicable filenames:
        self.files = [file for file in os.listdir(self.folder + "/segs") if file.endswith(".npz")]
        print(len(self.files), "Files Found.")
        self.list_IDs = list(range(len(self.files)))
        self.epochs = int(np.ceil(len(self.files)/batch_size))
        
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
        X = np.empty(((self.batch_size)*2, *self.dim,1))
        y = np.empty(((self.batch_size)*2, *self.dim,1))
        L = self.batch_size

        # Generate data
        for i, ID in enumerate(list_IDs_temp):
            # Store image and horizontal flip
            X[i,:,:,:,0] = np.load(self.folder + "/imgs/" + self.files[ID])['arr_0']
            X[L + i,:,:,:,0] = np.flip(np.load(self.folder + "/imgs/" + self.files[ID])['arr_0'],1)

            # Store segment and horizontal flip
            y[i,:,:,:,0] = np.load(self.folder + "/segs/" + self.files[ID])['arr_0']
            y[L + i,:,:,:,0] = np.flip(np.load(self.folder + "/segs/" + self.files[ID])['arr_0'],1)
            X.reshape(-1,*self.dim,1)
            y.reshape(-1,*self.dim,1)

        return X, y


# In[ ]:




