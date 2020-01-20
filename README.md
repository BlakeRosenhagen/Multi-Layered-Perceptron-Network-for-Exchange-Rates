# Multi-layer-Perception-Network-for-Exchange-Rates
Using an Artificial Neural Network to process, train, and predict future exchange rates based on historical data.


## Attention
**This is a work in progress and will be updated.**

Must have matplotlib 2.2.3 installed to work correctly
"!pip install matplotlib 2.2.3" in command prompt

This version is meant to run in a jupyter notebook




## Description
A multilayer perceptron (MLP) is a fully connected neural network, i.e., all the nodes from the current layer are connected to the next layer. A MLP consisting in 3 or more layers: an input layer, an output layer and one or more hidden layers. Note that the activation function for the nodes in all the layers (except the input layer) is a non-linear function.


<img src="mlp.png" width="40%">

**ASSUMPTION** : The main assumption of this model is assuming that the price of a the previous time is a significant predictor of the present price. Functionally this can be visualized as two array, x and y like what is shown below.

x_column . . . . . . . . . . . . . . . . . . y_column

price at time 1  ------->     price at time 2

price at time 2  ------->     price at time 3

price at time 3  ------->     price at time 4

## Methodology
The functional input of this model is any time series data, so it could therotically work with other price type data such as stock prices, future prices, etc. But the predicting capabilities are really only designed for exchange rate data.

prep.py first prepares the data so that it may be compadible with the neural network.

train.py trains the model with the inputs of model selection, epoch count, and batch size. The model's cost/loss function is to minimize mean square error (MSE). Mean absolute percentage error (MAPE) is also shown and logged. Each epoch the loss function attempts to reduce the MSE. Successful simulations will showcase a decreasing MSE until the last one or two points.

train.py will aslo split the data into two sets, training and test sets. The default split ratio is 80/20 training. This can be altered, see customizable simmulation tab.

predict.py will use the trained model that was created in train.py and predict the future exchange rates. A visualization will appear to show this.

baseline.py, cond.py, plot, tools.py function as supportive file that allow the core files to run.

## Instructions
1. Place time series data file into data folder replacing ce.csv

2. Rename your csv file as ce.csv, save

3. Launch jupyter notebook

4. Run all cells

5. Visualization is outputted on notebook, and more information is saved to **models** and **__pycache__** folders.

## Visualization examples




## Customizable simulation
### Alter epoch and batch variables
___________________________________
This is how to change *epoch count* and *batch size*

Follow these instuctions after step 2 of "instructions header"

1. Open tools.py in editor, go to line 22, replace the two int values in the list that equals to batches with your own numbers within given ranges. 10-100,30-55

2. Save file

3. Go to step 3 of "Instructions header"


### Alter train-test split

--------------------------

This is how to change the segmentation of the data into training and testing sets.

Follow these instuctions after step 2 of "instructions header"

1. Open tools.py in editor, go to line 41 and 42, replace the two decimal values with your own numbers. MUST BE EQUAL TO 1.00.

2. Save file

3. Go to step 3 of "Instructions header"

## Technologies used
jupyter notebook

keras

tensorflow

pandas

numpy

scikit-learn

matplotlib
