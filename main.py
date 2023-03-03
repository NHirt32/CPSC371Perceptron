"""Runnable for the mushroom perceptron"""

import Parsers
from Perceptron import *

file = "MushroomTestData_1600.txt"

mushrooms = Parsers.file_read(file)

weights = []
for attribute in mushrooms[0][slice(1, len(mushrooms[0]))]:
    weights.append(0)

mushroom_perceptron = Perceptron(weights, 0, 0.5, mushrooms, 1000000, 0, 1)
mushroom_perceptron.load("Perceptron_info.json")
mushroom_perceptron.predict_test_data()


