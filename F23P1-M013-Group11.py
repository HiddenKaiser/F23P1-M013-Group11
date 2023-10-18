# To Run: python main.py

# Jack Keuler Tasks:
# 1. Read characters and binary values from an Excel file
# 2. Function to return binary value for a given string
# 3. Function to return text string for a binary value

import pandas as pd

# Read Excel file
df = pd.read_excel('BinaryDefinitions.xlsx')
sf = pd.read_excel('ShortcutDefinitions.xlsx')

# print out all the contents of the excel file
print(df)

# Read characters from Excel file (column "Characters")
# Read binary values from Excel file (column "Binary")
# store character = binary value in a dictionary
# store and read binary value as a string

def read_shortcut_table():
    char_bin = {}
    for i in range(len(sf)):
        char = str(sf['Character'][i])
        repString = sf['String'][i]

        repString = " " + repString + " "
        if repString[len(repString)-2] == "/":
            repString = repString.replace("/ ", "")

        char_bin[char] = repString
        
    return char_bin


shortcuts = read_shortcut_table()

# idea, use shortcut character (::shortcut) and then a lower/uppercase letter to indicate the word it indicates
def encode_text(text):
    for key in shortcuts:
        repString = shortcuts[key]
        shortcutStr = "::shortcut" + str(key)
        text = text.replace(repString, shortcutStr)

    f = open("EncodedText.txt", "w+") # open or create a new text file called "BinOutput.txt" for writing
    f.write(text) # write the concatenated binary data to the "BinOutput.txt" file
    f.close() # close the "BinOutput.txt" file

    return text

def decode_text(text):
    for key in shortcuts:
        repString = shortcuts[key]
        shortcutStr = "::shortcut" + str(key)
        text = text.replace(shortcutStr, repString)
    return text
    

# Jack Keuler Task 1:
# expand_binary takes a number, we store the characters as either a short 5 bit binary or a long 7 bit binary
# if the number is below 5 digits, we add 0s to the front of the number until it is 5 digits long
def expand_binary(binary):
    binary = str(binary)
    if len(binary) < 5:
        while len(binary) < 5:
            binary = '0' + binary
    return binary

# Jack Keuler Task 1:
# Read characters and binary values from Excel
def read_excel():
    char_bin = {}
    for i in range(len(df)):
        char = str(df['Characters'][i])
        if char == '<space>':
            char = ' '

        binary = expand_binary(df['Binary'][i]) # expand binary, because pandas reads the binary values as a number and gets rid of the trailing values
        char_bin[char] = binary
        #print(char, binary)
    return char_bin


# read the table and put it in a dictionary. (Also prints out the values)
char_table = read_excel()

def isApartOfCharTable(unfinishedKey):
    if unfinishedKey in char_table:
        return True
    
    for charKey in char_table:
        if charKey.find(unfinishedKey) >= 0:
            return True
    return False

# Jack Keuler Task 2:
# Function to return binary value for a given string
# convert a string to an encoded binary string

def text_to_binary(text):
    text = encode_text(text)

    binary = ""
    i = 0

    shortcutNum = 0

    while i < (len(text)):
        key = text[i]
        highestLength = 0
        for charKey in char_table:
            length = len(charKey)
            if length > highestLength and text.find(charKey, i, i+length) >= 0:
                highestLength = length
                key = charKey
                i = i + length - 1

        if key == "\n":
            key = "\\n"

        if key == "::shortcut":
            shortcutNum += 1
            #print("Shortcut found")

        binary += char_table[key]
        i += 1
    
    print(str(shortcutNum) + " shortcuts found!")

    return binary

# Jack Keuler Task 3:
# Function to return text string for a binary value
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

    text = text.replace("\\n", "\n")
    text = decode_text(text)

    return text


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

    print("Took " + str(numBits) + " bits to represent the text file")


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

# task 6
# testing to see if the input text and output text are the same
def compare_results(TextInput: str = "TextInput.txt", TextOutput: str = "TextOutput.txt") -> bool:
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


read_text_file("TextInput.txt") 

decode("BinOutput.txt")

print( "Strings Match: " + str(compare_results()) )