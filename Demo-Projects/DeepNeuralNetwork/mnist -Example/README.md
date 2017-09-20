# Deep Neural Network Example using MNIST Data set

We're going to be working first with the MNIST dataset, which is a dataset that contains 60,000 training samples and 10,000 testing samples of hand-written and labeled digits, 0 through 9, so ten total "classes.

The MNIST dataset has the images, which we'll be working with as purely black and white, thresholded, images, of size 28 x 28, or 784 pixels total

First, we take our input data, and we need to send it to hidden layer 1. Thus, we weight the input data, and send it to layer 1, where it will undergo the activation function, so the neuron can decide whether or not to fire and output some data to either the output layer, or another hidden layer. We will have three hidden layers in this example, making this a Deep Neural Network. From the output we get, we will compare that output to the intended output. We will use a cost function (alternatively called a loss function), to determine how wrong we are. Finally, we will use an optimizer function, Adam Optimizer in this case, to minimize the cost (how wrong we are). The way cost is minimized is by tinkering with the weights, with the goal of hopefully lowering the cost. How quickly we want to lower the cost is determined by the learning rate. The lower the value for learning rate, the slower we will learn, and the more likely we'll get better results. 

