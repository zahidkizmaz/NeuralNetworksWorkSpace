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
        
        self.learning_rate = 0.1

    # y = (1 / 1 + (e ^ -x))
    def sigmoid(self, x):0
        return (1 /(1 + np.exp(-x))) 

    def relu(self, x):
        return np.max([0 ,x])

    def predict(self, input_array):
        # generating hidden outputs
        inputs = np.array(input_array)
        hidden = np.array(np.dot(self.weights_ho, inputs))
        hidden += self.bias_h
        
        # activation function!
        hidden = np.map(sigmoid, hidden)
        
        output = np.dot(self.weights_ho, hidden)
        output += self.bias_o
        output = np.map(sigmoid, output)

        return np.ravel(output)

    def train(self, input_array, target_array):
        inputs = np.array(input_array)
        hidden = np.dot(self.weights_ih, inputs)
        hidden += self.bias_h
        hidden = np.map(sigmoid, hidden)

        outputs = np.dot(self.weights_ih, hidden)
        outputs += self.bias_o
        outputs = np.map(sigmoid, outputs)

        targets = np.array(target_array)
        
        output_errors = targets - outputs

        gradients = np.map(sigmoid, outputs)
        gradients = np.dot(gradients, output_errors)
        gradients *= self.learning_rate
        
        hidden_T = np.transpose(hidden)
        weight_ho_deltas = np.dot(gradients, hidden_T)

        self.weights_ho += weight_ho_deltas

        self.bias_o += gradients

        who_t = np.transpose(self.weights_ho)
        hidden_errors = np.dot(who_t, output_errors)

        hidden_gradient = np.map(sigmoid, output_errors)
        hidden_gradient = np.dot(hidden_gradient, hidden_errors)
        hidden_gradient *= self.learning_rate

        inputs_T = np.transpose(inputs)
        weight_ih_deltas = np.dot(hidden_gradient, inputs_T)

        self.weights_ih += weight_ih_deltas

        self.bias_h += hidden_gradient








