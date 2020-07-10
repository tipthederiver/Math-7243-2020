import dataWrangler as dw
import models as md
import pickle

import os
import argparse

parser = argparse.ArgumentParser(
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# Data and model checkpoints directories					
parser.add_argument('--model_dir', type=str, default='/opt/ml/model',
                    help='Directory to store checkpointed models')

# Data and model checkpoints directories					
parser.add_argument('--final_model', type=str, default='/opt/ml/model',
                    help='Directory to store final models')
                    
# Data and model checkpoints directories
parser.add_argument('--data_dir', type=str, default='',
                    help='Data directory containing input.txt with training examples') 

# Data and model checkpoints directories
parser.add_argument('--train_file', type=str, default='',
                    help='File containing list of training names')   

# Data and model checkpoints directories
parser.add_argument('--test_file', type=str, default='',
                    help='File containing list of validating names')  

# Data and model checkpoints directories
parser.add_argument('--weights', type=str, default='',
                    help='File containing weights') 

# Data and model checkpoints directories
parser.add_argument('--epochs', type=str, default='1',
                    help='File containing weights') 

                    
args = parser.parse_args()
files = os.listdir(args.data_dir)
print(files)

##
# Need to save model weights, history to S3
##
# Save final model out to opt.
##

#files = ['ID_0a336e630', 'ID_0ba79c0ef', 'ID_0bc7199c6']
#path = '../Example Bucket'

train_list = []
test_list = []

if not os.path.exists(args.final_model):
    os.makedirs(args.final_model)

if len(args.train_file) is 0:
    train_file = args.data_dir + '/train.txt'
else:
    train_file = args.train_file
    
  
if len(args.test_file) is 0:
    test_file = args.data_dir + '/test.txt'
else:
    test_file = args.test_file
          
          
# open file and read the content in a list
with open(train_file, 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1] # remove linebreak which is the last character of the string
        train_list.append(currentPlace) # add item to the list
          
# open file and read the content in a list
with open(test_file, 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1] # remove linebreak which is the last character of the string
        test_list.append(currentPlace) # add item to the list
        


train_gen = dw.DataGenerator(folder=args.data_dir,batch_size=1, file_list=train_list, shuffle=False)
test_gen = dw.DataGenerator(folder=args.data_dir,batch_size=1, file_list=test_list, shuffle=False)

model = md.unet2D(input_size = (512,512,4))

if len(args.weights) > 0:
    model.load_weights(args.weights)
    print("Weights Successfully Loaded")

history = md.train_model(model, train_gen, test_gen, name="model", checkpoint_dir=args.final_model, epochs=int(args.epochs))

print(args.final_model)

#model.save(args.final_model + '/trainedmodel.h5') # saving the model
model.save_weights(filepath=args.final_model + '/final_weight.h5')

with open(args.final_model + '/trainHistoryOld', 'wb') as handle: # saving the history of the model
    pickle.dump(history.history, handle)
