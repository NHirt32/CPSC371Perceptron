import json
class Perceptron:
    """Core object of the perceptron."""
    def __init__(self, weights, bias, lrate, data, iterations, global_error, epoch):
        self.weights = weights
        self.bias = bias
        self.lrate = lrate
        self.data = data
        self.iterations = iterations
        self.global_error = global_error
        self.epoch = epoch


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

        while counter < self.iterations:
            errors = 0
            for datapoint in self.data:
                err = self.train_datapoint(datapoint)
                errors = errors + err
                self.global_error = self.global_error + err

            print(self.to_string() + "\nNumber of errors this epoch: " + str(errors) + "\n")
            counter = counter + 1
            self.epoch = self.epoch + 1


    def to_string(self):
        """Returns a string representing the perceptron object."""
        String = "EPOCH " + str(self.epoch)
        String = String + "\nweights: "
        for weight in self.weights:
            String = String + str(weight) + " "

        String = String + "\nbias: " + str(self.bias)

        String = String + "\nlearning rate: " + str(self.lrate)
        String = String + "\nGlobal error: " + str(self.global_error)

        return String


    def save(self, filename):
        """Saves the state of a perceptron in a given json file."""
        mushroom_perceptron_dict = {
            "bias": self.bias,
            "lrate": self.lrate,
            "weights": self.weights,
            "global_error": self.global_error,
            "epoch": self.epoch
        }

        file = open(filename, "w")

        json.dump(mushroom_perceptron_dict, file)

        file.close()


    def load(self, filename):
        """Loads the state of a perceptron in a given json file."""
        file = open(filename, "r")

        mushroom_perceptron_dict = json.load(file)

        i = 0
        while(i < len(mushroom_perceptron_dict["weights"])):
            self.weights[i] = mushroom_perceptron_dict["weights"][i]
            i = i + 1

        self.bias = mushroom_perceptron_dict["bias"]
        self.lrate = mushroom_perceptron_dict["lrate"]
        self.global_error = mushroom_perceptron_dict["global_error"]
        self.epoch = mushroom_perceptron_dict["epoch"]

        file.close()