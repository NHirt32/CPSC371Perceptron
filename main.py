"""Runnable for the mushroom perceptron"""

import Parsers
from Perceptron import *

#file = "MushroomData_8000.txt"
file = "MushroomTrainingData_6400.txt"
#file = "MushroomTestData_1600.txt"

mushrooms = Parsers.file_read(file)

weights = []
for attribute in mushrooms[0][slice(1, len(mushrooms[0]))]:
    weights.append(0)

mushroom_perceptron = Perceptron(weights, 0, 0.005, mushrooms, 1000000, 0, 1)
mushroom_perceptron.load("Perceptron_init.json")
#mushroom_perceptron.predict_test_data()
#mushroom_perceptron.train()
#mushroom_perceptron.save("Perceptron_info.json")


