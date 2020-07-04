import numpy as np
import pandas as pd
import os
import argparse

print("test")

parser = argparse.ArgumentParser(
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# Data and model checkpoints directories					
parser.add_argument('--model_dir', type=str, default='/opt/ml/model',
                    help='directory to store checkpointed models')

# Data and model checkpoints directories					
parser.add_argument('--final_model', type=str, default='/opt/ml/model',
                    help='directory to store checkpointed models')
                    
# Data and model checkpoints directories
parser.add_argument('--data_dir', type=str, default='data/tinyshakespeare',
                    help='data directory containing input.txt with training examples')     
                    
args = parser.parse_args()
files = os.listdir(args.data_dir)
print(files)


save_path = os.path.join(args.model_dir, "Output.txt")
with open(save_path, "w") as text_file:
    print(f"Purchase Amount: {files}", file=text_file)
