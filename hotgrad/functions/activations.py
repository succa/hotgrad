# -*- coding: utf-8 -*-
""" Implementation of the activation functions. """

from torch import FloatTensor
import hotgrad
from hotgrad.module import Module2Operands, Module1Operand

class ReLU(Module1Operand):
    """
    Implements a rectified linear unit (ReLU) activation function.
    """
    
    def forward(self, input):
        """ Compute the forward pass. """
        
        super(ReLU, self).forward(input)
        
        input.data[self.input.data<0] = 0
        return hotgrad.variable.Variable(input.data, previous_op=self)

    def backward(self, grad):
        """ Propagate the gradient to the input Variable. """
        input_grad = (self.input.data>0).type(FloatTensor)
        self.input.backward(grad = input_grad*grad)
        
class Tanh(Module1Operand):
    """
    Implements Tanh activation function.
    """
    
    def forward(self, input):
        """ Compute the forward pass. """
        super(Tanh, self).forward(input)
        
        return hotgrad.variable.Variable(input.data.tanh(), previous_op=self)
   
    def backward(self, grad):
        """ Propagate the gradient to the input Variable. """
        input_grad = 1 - self.input.data.tanh()**2
        self.input.backward(grad = input_grad*grad)
    
