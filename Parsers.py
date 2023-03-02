
def file_read(requested_file):
    """Grabs data from input file and returns a 2d array of numbers representing attribute cases."""
    sample_data_file = open(requested_file, "r") # Opens known mushroom file in read mode
    sample_data_list = sample_data_file.readlines() # Reads each line into an array element

    for index, data in enumerate(sample_data_list):
        data = data.strip("\n") # Trims new line from each index
        sample_data_list[index] = data.split(',')   # Splits elements by ',' creating a 2d array

        for jindex, attribute in enumerate(sample_data_list[index]):
            sample_data_list[index][jindex] = map_input(attribute)

    return sample_data_list

def map_input(attr):
    """Maps a character attribute to an integer value."""
    switch = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25,
        '?': 26
    }

    return switch[attr]


