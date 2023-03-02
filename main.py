import Parsers

file = "MushroomData_8000.txt"

mushrooms = Parsers.file_read(file)

for mushroom in mushrooms:
    print(mushroom)