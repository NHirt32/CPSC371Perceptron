# CPSC371Perceptron

## Contributors
    Name: Andrew Hunter-Owega
    Email: ahunterow@unbc.ca
    Student Number: 230 147 039

    Name: Daniel Strickland
    Email: dstrickla@unbc.ca
    Student Number: 230 146 357

    Name: Nicholas Hirt
    Email: nhirt@unbc.ca
    Student Number: 230 127 295

## Report

# Data Division
    In training and testing the perceptron, an 80 - 20 split was used for the provided 8000 mushrooms. 
    The latter 1600 were used as test data and are in file "MushroomTestData_1600.txt", and the
    previous 6400 mushrooms were used for training and are in file "MushroomTrainingData_6400.txt".

# Final Settings
    The perceptron model that we are currently using is the "Perceptron_info (1mil, 0.005 lrate).json" model.
    This has a learning rate of 0.005, and ran for one million epochs. 

# Accuracy of the Application
    The following accuracies are relative to the test data, being the 1600 mushrooms.
    Each JSON file represents a trained perceptron file.
    
    Perceptron_info (1mil, 0.1 lrate).json: 65 errors, or 4.1% error
    Perceptron_info (1mil, 0.005 lrate).json: 56 errors, or 3.5% error
    Perceptron_info (100k, 0.01 lrate).json: 51 errors, or 3.2% error
    Perceptron_info (100k, 0.1 lrate).json: 59 errors, or 3.6% error
    Perceptron_info (100k, 0.5 lrate).json: 51 errors or 3.2% error
    
# How To Use

Open up the project in something that runs python files, like an IDE, run main.py.

You will be prompted in the console to input either "100" or "1600."
Entering in "100" will run the current perceptron model prediction on the 100 unknown mushrooms,
entering in "1600" will run the current perceptron model prediction on the 1600 mushrooms used as test data.
