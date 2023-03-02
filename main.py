"""Runnable for the mushroom perceptron"""

import Parsers
from Perceptron import *

file = "MushroomData_8000.txt"

mushrooms = Parsers.file_read(file)

for mushroom in mushrooms:
    print(mushroom)

weights = []
for attribute in mushrooms[0][slice(1,len(mushrooms[0]))]:
    weights.append(0)

mushyfinder = Perceptron(weights, 1, 0.1, mushrooms, 1000)
mushyfinder.train()
