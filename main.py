"""Runnable for the mushroom perceptron"""

import Parsers
from Perceptron import *

def run():
    """Uses a trained perceptron model to predict the selected data."""

    file = ""
    case = 0
    run = True

    while run:
        print("What file would you like to predict for? Entering \"100\" predicts the mushrooms in"
              "MushroomData_Unknwon_100.txt, \nentering \"1600\" predicts the mushrooms in "
              "MushroomTestData_1600.txt.\n>")
        file = input()
        if file == "100":
            run = False
            case = 1
            file = "MushroomData_Unknwon_100.txt"

        elif file == "1600":
            run = False
            case = 0
            file = "MushroomTestData_1600.txt"

        else:
            print("invalid file, please enter either \"100\" or \"1600\".\n")

    mushrooms = Parsers.file_read(file)

    weights = []


    if case == 1:
        for attribute in mushrooms[0]:
            weights.append(0)

        mushroom_perceptron = Perceptron(weights, 0, 0, mushrooms, 0, 0, 0)
        mushroom_perceptron.load("Perceptron_info.json")
        mushroom_perceptron.predict_unknown_data()
    else:
        for attribute in mushrooms[0][slice(1, len(mushrooms[0]))]:
            weights.append(0)

        mushroom_perceptron = Perceptron(weights, 0, 0, mushrooms, 0, 0, 0)
        mushroom_perceptron.load("Perceptron_info.json")
        mushroom_perceptron.predict_test_data()

def test():
    """Testing function, also used to train perceptrons"""

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

run()
