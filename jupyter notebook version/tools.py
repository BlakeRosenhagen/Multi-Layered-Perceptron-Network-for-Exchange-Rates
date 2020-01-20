import numpy as np
from pprint import pprint
import sys
from sys import exit


def get_params(script='train.py'):
    xa=''
    if script == 'train.py':
        xa='[plot|ploth]'
    try:
        #EDIT
            #global input_cycle_complete = 0
            #if input_cycle_complete > 0:
                #global input_1 = str(input("Mode?"))
                #global input_2 = input("Epoch?")
                #global input_3 = input("Batche Size?")
                #global batches_1 = [input_1,input_2,input_3]
                #global input_cycle_complete = input_cycle_complete + 1
            #else:
                #pass
                name, epochs, batches=['default',50,34]
        #EDIT
    except ValueError:
        print('Usage: %s model_name epochs batch_size %s' % (script, xa))
       #exit(1)
        sys.exit(1)
    try:

        #EDIT
        #plot=sys.argv[4]
        plot=['ploth']
        #EDIT

    except IndexError:
        plot=False

    return name, int(epochs), int(batches), plot

def train_test_split(rawx, xpo):
    train_size=int(len(rawx)*0.80)
    test_size=int(len(rawx)*0.20)
    print("Train size:", train_size, "Test size:", test_size, len(rawx))
    train_x, train_y = np.array(rawx[:train_size]), np.array(xpo[:train_size])
    test_x, test_y = np.array(rawx[train_size:]), np.array(xpo[train_size:])
    return train_x, train_y, test_x, test_y

def logme(msg):
    pprint(msg)
