#!/usr/bin/env python
# coding: utf-8

# # Losses

# In[3]:


from tensorflow.keras import backend as K
from tensorflow.keras.losses import binary_crossentropy

# Dice Coefficient
def dice_coeff(y_true, y_pred):
    smooth = 1.
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    score = (2. * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)
    return score

# Dice Loss
def dice_loss(y_true, y_pred):
    loss = 1 - dice_coeff(y_true, y_pred)
    return loss

# Binary Cross Entropy plus Dice Loss
def bce_dice_loss(y_true, y_pred):
    loss = binary_crossentropy(K.flatten(y_true),K.flatten(y_pred)) + dice_loss(y_true, y_pred)
    return loss

# Intersection Over Union Coefficeint
def iou_coeff(y_true, y_pred):
    smooth = 1.
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(K.abs(y_true_f*y_pred_f))
    union = K.sum(y_true_f)+K.sum(y_pred_f) - intersection
    score = (intersection + smooth)/(union + smooth)
    return score

# Intersection Over Union Loss
def iou_loss(y_true,y_pred):
    loss = 1- iou_coeff(y_true,y_pred)
    return loss

# Binary Cross Entropy plus IoU
def bce_iou_loss(y_true,y_pred):
    loss = binary_crossentropy(K.flatten(y_true),K.flatten(y_pred)) + iou_loss(y_true,y_pred)
    return loss


# # Construct 2D Unet Model
# 
# Usage:
# 
#     model = unet2D(input_size = (120,120,1))

# In[16]:


from tensorflow.keras.layers import Conv2D,Conv3D,Conv2DTranspose,MaxPooling2D,UpSampling2D,ZeroPadding2D
from tensorflow.keras.layers import Input, Dense, Activation,Dropout, BatchNormalization
from tensorflow.keras.layers import concatenate 
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import binary_crossentropy

def unet2D(pretrained_weights = None,input_size = (512,512,1),lr=1e-4):
    inputs = Input(input_size)
    conv1 = Conv2D(32, 3, padding = 'same')(inputs)
    conv1 = BatchNormalization()(conv1)
    conv1 = Activation('relu')(conv1)
    conv1 = Conv2D(32, 3, padding = 'same')(conv1)
    conv1 = BatchNormalization()(conv1)
    conv1 = Activation('relu')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    
    conv2 = Conv2D(64, 3, padding = 'same')(pool1)
    conv2 = BatchNormalization()(conv2)
    conv2 = Activation('relu')(conv2)
    conv2 = Conv2D(64, 3, padding = 'same')(conv2)
    conv2 = BatchNormalization()(conv2)
    conv2 = Activation('relu')(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    
    conv3 = Conv2D(128, 3, padding = 'same')(pool2)
    conv3 = BatchNormalization()(conv3)
    conv3 = Activation('relu')(conv3)
    conv3 = Conv2D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv3)
    conv3 = BatchNormalization()(conv3)
    conv3 = Activation('relu')(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    
    conv4 = Conv2D(256, 3, padding = 'same')(pool3)
    conv4 = BatchNormalization()(conv4)
    conv4 = Activation('relu')(conv4)
    conv4 = Conv2D(256, 3, padding = 'same')(conv4)
    conv4 = BatchNormalization()(conv4)
    conv4 = Activation('relu')(conv4)
    drop4 = Dropout(0.5)(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(drop4)

    conv5 = Conv2D(512, 3, padding = 'same')(pool4)
    conv5 = BatchNormalization()(conv5)
    conv5 = Activation('relu')(conv5)
    conv5 = Conv2D(512, 3, padding = 'same')(conv5)
    conv5 = BatchNormalization()(conv5)
    conv5 = Activation('relu')(conv5)
    drop5 = Dropout(0.5)(conv5)
    
#    padd = ZeroPadding2D(((0,1),(0,1)))(UpSampling2D(size = (2,2))(drop5))

    up6 = Conv2D(256, 2, padding = 'same')(UpSampling2D(size = (2,2))(drop5))
    up6 = BatchNormalization()(up6)
    up6 = Activation('relu')(up6)
    
    
    merge6 = concatenate([drop4,up6], axis = 3)
    conv6 = Conv2D(256, 3, padding = 'same')(merge6)
    conv6 = BatchNormalization()(conv6)
    conv6 = Activation('relu')(conv6)
    conv6 = Conv2D(256, 3, padding = 'same')(conv6)
    conv6 = BatchNormalization()(conv6)
    conv6 = Activation('relu')(conv6)

    up7 = Conv2D(128, 2, padding = 'same')(UpSampling2D(size = (2,2))(conv6))
    up7 = BatchNormalization()(up7)
    up7 = Activation('relu')(up7)
    
    merge7 = concatenate([conv3,up7], axis = 3)
    conv7 = Conv2D(128, 3, padding = 'same')(merge7)
    conv7 = BatchNormalization()(conv7)
    conv7 = Activation('relu')(conv7)
    conv7 = Conv2D(128, 3, padding = 'same')(conv7)
    conv7 = BatchNormalization()(conv7)
    conv7 = Activation('relu')(conv7)

    up8 = Conv2D(64, 2, padding = 'same')(UpSampling2D(size = (2,2))(conv7))
    up8 = BatchNormalization()(up8)
    up8 = Activation('relu')(up8)
    
    merge8 = concatenate([conv2,up8], axis = 3)
    conv8 = Conv2D(64, 3, padding = 'same')(merge8)
    conv8 = BatchNormalization()(conv8)
    conv8 = Activation('relu')(conv8)
    conv8 = Conv2D(64, 3, padding = 'same')(conv8)
    conv8 = BatchNormalization()(conv8)
    conv8 = Activation('relu')(conv8)

    up9 = Conv2D(32, 2, padding = 'same')(UpSampling2D(size = (2,2))(conv8))
    up9 = BatchNormalization()(up9)
    up9 = Activation('relu')(up9)
    
    merge9 = concatenate([conv1,up9], axis = 3)
    conv9 = Conv2D(32, 3, padding = 'same')(merge9)
    conv9 = BatchNormalization()(conv9)
    conv9 = Activation('relu')(conv9)

    conv9 = Conv2D(2, 3, padding = 'same')(conv9)
    conv9 = BatchNormalization()(conv9)
    conv9 = Activation('relu')(conv9)

    conv10 = Conv2D(1, 1, activation = 'sigmoid')(conv9)

    model = Model(inputs, conv10)

    model.compile(optimizer = Adam(lr = lr), loss = bce_dice_loss, metrics = ['accuracy'])
    
    model.summary()

    if(pretrained_weights):
        model.load_weights(pretrained_weights)

    return model



from tensorflow.keras.callbacks import CSVLogger

def train_model(model,training_generator,testing_generator, checkpoint_dir="", name="model", epochs=1):
    filepath = checkpoint_dir + name + "_{epoch:03d}-{loss:.4f}.h5"
    
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=False, mode='min')
    csv_logger = CSVLogger(checkpoint_dir + name + "_history_log.csv", append=True)

    history = model.fit(training_generator,
                        epochs=epochs, 
                        verbose=1,
                        validation_data=testing_generator,callbacks=[checkpoint, csv_logger])
    return history