import numpy as np
import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser(
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
                    
# Data and model checkpoints directories
parser.add_argument('--data_dir', type=str, default='data/tinyshakespeare',
                    help='data directory containing input.txt with training examples')     
                    
