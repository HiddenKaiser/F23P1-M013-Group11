# To Run: python p1.py

# 1. Read characters and binary values from an Excel file
# 2. Function to read binary values file and write text file

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
        binary = expand_binary(df['Binary'][i])
        char_bin[char] = binary
        print(char, binary)
    return char_bin


# read the table and put it in a dictionary. (Also prints out the values)
print("\n{")
char_table = read_excel()
print("}\n")

# convert text to binary

def text_to_binary(text):
    binary = ""
    i = 0
    while i < (len(text)):
        key = text[i]
        while True:
            if i+1 < len(text) and (key + text[i+1]) in char_table:
                i += 1
                key = key + text[i]
            else:
                break
        binary += char_table[key]
        i += 1
    return binary

binaryEncoded = text_to_binary("the quick brown fox jumps over the lazy dog.")
print(binaryEncoded)

# shorts are 5 bits long, longs are 7 bits long, convert binary to text
def binary_to_text(binary):
    text = ""
    i = 0
    while i < len(binary):
        if binary[i] == '0':
            text += list(char_table.keys())[list(char_table.values()).index(binary[i:i+5])]
            i += 5
        else:
            text += list(char_table.keys())[list(char_table.values()).index(binary[i:i+7])]
            i += 7
    return text

print(binary_to_text(binaryEncoded))