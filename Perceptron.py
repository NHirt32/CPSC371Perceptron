
class Perceptron:
    """Core object of the perceptron, has one useful method predict()."""
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def sign(self, val):
        """Optimistically says that the 0 value will map to 1."""
        if val < 0:
            return -1
        else:
            return 1

    def predict(self, attributes):
        """Takes a list of numeric attributes representing a mushroom, returns whether they are poisonous or not."""
        result = 0
        for index, attribute in enumerate(attributes):
            result = result + ((self.weights[index] * attribute) + self.bias)

        return self.sign(result)