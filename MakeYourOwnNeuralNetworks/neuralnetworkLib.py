import numpy as np 

class NeuralNetwork:
   
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = np.array(input_nodes)
        self.hidden_nodes = np.array(hidden_nodes)
        self.output_nodes= np.array(output_nodes)
        
        self.weights_ih = np.random.random((self.hidden_nodes.size(),self.input_nodes.size()))
        self.weights_ih *= 2
        self.weights_ih -= 1

        self.weights_ho = np.random.random((self.output_nodes.size(),self.hidden_nodes.size()))
        self.weights_ho *= 2
        self.weights_ho -= 1

        self.bias_h = np.random.random((self.hidden_nodes.size(), 1))
        self.bias_h *= 2
        self.bias_h -= 1
    
        self.bias_o = np.random.random((self.output_nodes.size(), 1))
        self.bias_o *= 2
        self.bias_o -= 1
    
