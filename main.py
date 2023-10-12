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
#input_text = "A robot may not injure a human being or, through inaction, allow a human being to come to harm. A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law. A robot must protect its own existence."

#binaryEncoded = text_to_binary(input_text)
#print(binaryEncoded)

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

#Task 5
#Leon Chen
#This function should new text file called “TextOutput.txt” that contains the characters that correspond to the given file.


def decode(fn="BinOutput.txt"):
    f = open(fn, "r")
    s = f.read()
    f.close()

    #print(s)
    i = s.index(".")
    s = s[i+1:]
    #print(s)

    charStr = binary_to_text(s)

    f = open("TextOutput.txt", "w+")
    f.write(charStr)
    #print(charStr)
    f.close()


# Sahaj Soni Task 4:
# Opens a file, reads the entire contents into a string, and closes the file
def read_text_file(fn): 
    f = open(fn) # open the text file for reading
    s = f.read() # read the contents of the text file into a string variable 's'
    f.close() # close the text file


    binary = text_to_binary(s) # converts the text file into binary, and the binary result is stored in the variable 'binary'

    numBits = len(binary) # calculate the number of bits in the binary representation
    outputText = str(numBits) + "." + binary # the 'binary' data is converted to a string, followed by a period, and then followed by the binary value as a string
    f = open("BinOutput.txt", "w+") # open or create a new text file called "BinOutput.txt" for writing
    f.write(outputText) # write the concatenated binary data to the "BinOutput.txt" file
    f.close() # close the "BinOutput.txt" file



read_text_file("TextInput.txt") 

decode("BinOutput.txt")
