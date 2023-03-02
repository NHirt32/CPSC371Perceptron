
class Perceptron:
    """Core object of the perceptron."""
    def __init__(self, weights, bias, lrate, data, iterations):
        self.weights = weights
        self.bias = bias
        self.lrate = lrate
        self.data = data
        self.iterations = iterations

    def sign(self, val):
        """Optimistically says that the 0 value will map to 1."""
        if val < 0:
            return -1
        else:
            return 1

    def predict(self, attributes):
        """Takes a list of numeric attributes representing a mushroom, returns whether they are poisonous or not.
            Does not take the output value, so remember to pass in appropriate slices."""
        result = 0
        for index, attribute in enumerate(attributes):
            result = result + ((self.weights[index] * attribute) + self.bias)

        return self.sign(result)

    def train_datapoint(self, datapoint):
        """Takes in a datapoint, adjusts weights accordingly."""
        attributes = datapoint[slice(1, len(datapoint))]
        tested_result = self.predict(attributes)

        true_result = 1

        # if is poisonous
        if datapoint[0] == 15:
            true_result = -1

        err = true_result - tested_result

        if err != 0:
            for index, weight in enumerate(self.weights):
                self.weights[index] = weight + (self.lrate * (true_result - tested_result) * attributes[index])

            self.bias = self.bias + (self.lrate * (true_result - tested_result))
            return 1
        else:
            return 0

    def train(self):
        """Takes in a bunch of datapoints, and adjusts the weights accordingly. Iterates
            for as many times as is set in the iterations field."""
        counter = 0
        global_errors = 0

        while counter < self.iterations:
            errors = 0
            for datapoint in self.data:
                err = self.train_datapoint(datapoint)
                errors = errors + err
                global_errors = global_errors + err

            print(self.to_string() +"\nNumber of errors globally: " + str(global_errors) +
                  "\nNumber of errors this epoch: " + str(errors) + "\n")
            counter = counter + 1



    def to_string(self):
        String = "weights: "
        for weight in self.weights:
            String = String + str(weight) + " "

        String = String + "\nbias: " + str(self.bias)

        String = String + "\nlearning rate: " + str(self.lrate)

        return String