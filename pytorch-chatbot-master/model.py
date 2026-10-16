import torch
import torch.nn as nn
"""
This code defines a class called NeuralNet that represents a neural network model using PyTorch. 
The network has three fully connected layers: the first layer takes an input of size input_size, 
the second layer has hidden_size neurons, and the third layer outputs num_classes values. 
The non-linear activation function ReLU is applied after each hidden layer.

In the __init__ method, the network layers are defined using the nn.Linear class from PyTorch. 
The forward method specifies how input data should flow through the layers of the network, 
first through the first layer (self.l1), then through a ReLU activation function (self.relu), 
then through the second layer (self.l2), then through another ReLU activation function, 
and finally through the third layer (self.l3). 

The output of the network is returned without applying any activation or softmax function.
"""

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at the end
        return out