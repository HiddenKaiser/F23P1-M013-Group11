# To Run: python main.py

# Jack Keuler Tasks:
# 1. Read characters and binary values from an Excel file
# 2. Function to return binary value for a given string
# 3. Function to return text string for a binary value

import pandas as pd

# Read Excel file
df = pd.read_excel('BinaryDefinitions.xlsx')

# print out all the contents of the excel file
print(df)

# Read characters from Excel file (column "Characters")
# Read binary values from Excel file (column "Binary")
# store character = binary value in a dictionary
# store and read binary value as a string


# expand_binary takes a number, we store the characters as either a short 5 bit binary or a long 7 bit binary
# if the number is below 5 digits, we add 0s to the front of the number until it is 5 digits long
def expand_binary(binary):
    binary = str(binary)
    if len(binary) < 5:
        while len(binary) < 5:
            binary = '0' + binary
    return binary

def read_excel():
    char_bin = {}
    for i in range(len(df)):
        char = str(df['Characters'][i])
        if char == '<space>':
            char = ' '

        binary = expand_binary(df['Binary'][i]) # expand binary, because pandas reads the binary values as a number and gets rid of the trailing values
        char_bin[char] = binary
        print(char, binary)
    return char_bin


# read the table and put it in a dictionary. (Also prints out the values)
print("\n{")
char_table = read_excel()
print("}\n")

# convert a string to an encoded binary string
def text_to_binary(text):
    binary = ""
    i = 0
    while i < (len(text)):
        key = text[i]
        while True:
            # confirm that we can advance the index and that the key + the next character is in the table
            if i+1 < len(text) and (key + text[i+1]) in char_table:
                i += 1
                key = key + text[i]
            else:
                break
        # add the corresponding binary string to the encoded string
        binary += char_table[key]
        i += 1
    return binary

#input_text = "the quick brown fox jumps over the lazy dog."
input_text = "A robot may not injure a human being or, through inaction, allow a human being to come to harm. A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law. A robot must protect its own existence."

binaryEncoded = text_to_binary(input_text)
print(binaryEncoded)

# shorts are 5 bits long, longs are 7 bits long, convert binary to text
def binary_to_text(binary):
    text = ""
    i = 0
    keysList = list(char_table.keys()) # create a list of the keys
    valList = list(char_table.values()) # create a list of the values

    # loop through the entire string of binary numbers
    while i < len(binary):
        if binary[i] == '0':
            text += keysList[valList.index(binary[i:i+5])] # find the character that corresponds to the selected binary value
            i += 5
        else:
            text += keysList[valList.index(binary[i:i+7])] # find the character that corresponds to the selected binary value
            i += 7
    return text

print(binary_to_text(binaryEncoded))

# task 6
# testing to see if the input text and output text are the same
def task6(TextInput: str = "TextInput.txt", TextOutput: str = "TextOutput.txt") -> bool:
    # opens both txt files
    f1 = open("TextInput.txt", "r")
    f2 = open("TextOutput.txt", "r")
    # giving variables to the read files
    text1 = f1.read()
    text2 = f2.read()

    # checks to see if both texts are equal in length
    if len(text1) != len(text2):
        return False
    else:
        # loops over char in each string to check if they are the same
        for index, char in enumerate(text1):
            if text1[index] == text2[index]:
                return True
            else:
                return False
    
    f1.close()
    f2.close()
