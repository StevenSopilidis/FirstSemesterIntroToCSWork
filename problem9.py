from ast import parse
from Utils import file_handler

# class for parsing the data and convert the chars into binary
class Parser:
    parsed_data = []
    def __init__(self, data) -> None:
        self.data = data
        self.__parse()

    # class method for converting every character to the 
    # binary form and saving them to a class field
    # will be called during class construction to parse data
    def __parse(self) -> None:
        # length of the binary
        l = 7
        for char in self.data:
            byte_array = char.encode()
            binary_int = int.from_bytes(byte_array, "big")
            binary_string = bin(binary_int)[2:].zfill(l)
            self.parsed_data.append(binary_string)
    # class method for printing the parsed data
    def printParsedData(self) -> None:
        i = 0
        for d in self.parsed_data:
            print(self.data[i], ":", d)
            i += 1

    # class method for finding the largest sequence of zeroes and ones
    def findMinMaxSequence(self) -> dict:
        max_one_sequence = 0
        max_zero_sequence = 0
        for d in self.parsed_data:
            current_one_sequence = 0
            current_zero_sequence = 0
            for bit in d:
                if bit == "1":
                    current_one_sequence += 1
                    current_zero_sequence = 0
                    if(current_one_sequence > max_one_sequence):
                        max_one_sequence = current_one_sequence
                else:
                    current_zero_sequence += 1
                    current_one_sequence = 0
                    if(current_zero_sequence > max_zero_sequence):
                        max_zero_sequence = current_zero_sequence
        return {"max_one_sequence": max_one_sequence, "max_zero_sequence": max_zero_sequence}


handler = file_handler.FileHandler("TestFiles/ascii_file.txt")
data = handler.readData()
parser = Parser(data)
# print the data as binary of length 7
parser.printParsedData()
# print the largest sequence of zeros and largest sequence of ones
max_sequences = parser.findMinMaxSequence()
print(max_sequences)