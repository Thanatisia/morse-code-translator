"""
Morse Code Translator
"""
import os
import sys

def merge_morse_symbols(morse_symbols=None):
    """
    Merge the individual morse symbols list for each alphanumerical character maps into a single word list
    - i.e. Hello World
        + Hello = ["....", ".", ".-..", ".-..", "---"]
        + World = [".--", "---", ".-.", ".-..", "-.."]

    :: Params
    - morse_symbols : List containing lists of all Morse symbols corresponding to each alphabet
        - Format: `HELLO = [ [".", ".", ".", "."], ["."], [".", "-", ".", "."], [".", "-", ".", "."], ["-", "-", "-"] ]`

    :: Returns
    - merged_morse_combination : List of the morse symbol's characters merged into individual strings
        + Type: List
        + Format: `HELLO = [ "....", ".", ".-..", ".-..", "---" ]`
    """
    # Initialize Variables
    merged_morse_combination = []

    # Join morse list together
    for i in range(len(morse_symbols)):
        # Get current morse combination
        curr_morse_combination = ''.join(morse_symbols[i])

        # Append the current morse combination into list for usage
        merged_morse_combination.append(curr_morse_combination)

    # Output
    return merged_morse_combination

def translate_string_to_morse(u_Msg, dataset=1):
    """
    Translate each word in a given string into a morse code, and return it in a list of morse symbols correlating to the individual words

    :: Params
    - u_Msg : The message string you wish to translate into morse
        + Type: String
    - dataset : Specify which morse code structure you want to use to translate
        + Type: Integer
        - Valid Values
            + 1 : The morse code symbols mapped to the characters are the strings
            + 2 : The morse code symbols are separated in a list

    :: Returns
    - translated_morse_code : The output list containing a dictionary (key-value) mapping of the word to its morse code symbols
        + Type: String
    """
    # Initialize Variables
    translated_morse_code = []
    morse_code_pronounciation = { "." : "dit", "-" : "dah" }
    match dataset:
        case 1: 
            morse_code = {
                # [character] : [code and durations]
                "A" : ".-",
                "B" : "-...",
                "C" : "-.-.",
                "D" : "-..",
                "E" : ".",
                "F" : "..-.",
                "G" : "--.",
                "H" : "....",
                "I" : "..",
                "J" : ".---",
                "K" : "-.-",
                "L" : ".-..",
                "M" : "--",
                "N" : "-.",
                "O" : "---",
                "P" : ".--.",
                "Q" : "--.-",
                "R" : ".-.",
                "S" : "...",
                "T" : "-",
                "U" : "..-",
                "V" : "...-",
                "W" : ".--",
                "X" : "-..-",
                "Y" : "-.--",
                "Z" : "--..",
                "0" : "-----",
                "1" : ".----",
                "2" : "..---",
                "3" : "...--",
                "4" : "....-",
                "5" : ".....",
                "6" : "-....",
                "7" : "--...",
                "8" : "---..",
                "9" : "----.",
            }
        case 2:
            morse_code = {
                # [character] : [code and durations]
                "A" : [".", "-"],
                "B" : ["-", ".", ".", "."],
                "C" : ["-", ".", "-", "."],
                "D" : ["-", ".", "."],
                "E" : ["."],
                "F" : [".", ".", "-", "."],
                "G" : ["-", "-", "."],
                "H" : [".", ".", ".", "."],
                "I" : [".", "."],
                "J" : [".", "-", "-", "-"],
                "K" : ["-", ".", "-"],
                "L" : [".", "-", ".", "."],
                "M" : ["-", "-"],
                "N" : ["-", "."],
                "O" : ["-", "-", "-"],
                "P" : [".", "-", "-", "."],
                "Q" : ["-", "-", ".", "-"],
                "R" : [".", "-", "."],
                "S" : [".", ".", "."],
                "T" : ["-"],
                "U" : [".", ".", "-"],
                "V" : [".", ".", ".", "-"],
                "W" : [".", "-", "-"],
                "X" : ["-", ".", ".", "-"],
                "Y" : ["-", ".", "-", "-"],
                "Z" : ["-", "-", ".", "."],
                "0" : ["-", "-", "-", "-", "-"],
                "1" : [".", "-", "-", "-", "-"],
                "2" : [".", ".", "-", "-", "-"],
                "3" : [".", ".", ".", "-", "-"],
                "4" : [".", ".", ".", ".", "-"],
                "5" : [".", ".", ".", ".", "."],
                "6" : ["-", ".", ".", ".", "."],
                "7" : ["-", "-", ".", ".", "."],
                "8" : ["-", "-", "-", ".", "."],
                "9" : ["-", "-", "-", "-", "."],
            }

    print("Morse Code: {}".format(morse_code))

    # Split user input into list
    u_msg_Split = u_Msg.split(" ")

    # Process user input into morse code
    # Iterate through the message list
    for i in range(len(u_msg_Split)):
        # Get current line
        curr_msg_str = u_msg_Split[i]

        # Split current line
        curr_msg_split = curr_msg_str.split(" ")

        # Iterate through all strings in the list
        for curr_str in curr_msg_split:
            # Initialize a new list to store string
            tmp_morse_code_storage = []

            # Iterate through characters in the current string
            for j in range(len(curr_str)):
                # Obtain current character
                curr_char = curr_str[j].upper()

                # Compare current character to the morse code chart/dictionary
                curr_char_morse_code = morse_code[curr_char]

                # Store current morse code into list
                tmp_morse_code_storage.append(curr_char_morse_code)

            # Map the current line to the morse code storage
            translated_morse_code.append({curr_str : tmp_morse_code_storage})

    # Output
    return translated_morse_code

def translate_dataset(u_Msg, dataset=1):
    """
    Translate the string into Morse using the provided dataset number

    :: Params
    - u_Msg : The message string you wish to translate into morse
        + Type: String
    - dataset : Specify which morse code structure you want to use to translate
        + Type: Integer
        - Valid Values
            + 1 : The morse code symbols mapped to the characters are the strings
            + 2 : The morse code symbols are separated in a list
    """
    # Initialize Variables
    results = []

    print("Message String: {}".format(u_Msg))

    # Translate String to Morse Code symbols
    translated_morse_code = translate_string_to_morse(u_Msg, dataset)

    print("Temporary: {}".format(translated_morse_code))

    # Output morse code
    for i in range(len(translated_morse_code)):
        # Get current word entry
        curr_entry = translated_morse_code[i]

        print("Current Entry: {}".format(curr_entry))

        # Iterate through current entry 
        for curr_word, curr_morse_list in curr_entry.items():
            # Join morse list together
            merged_morse_strings = merge_morse_symbols(curr_morse_list)

            # Print word to morse 
            results.append({curr_word : merged_morse_strings})

    # Return
    return results

def prepare_dataset(morse_symbols, delimiter="/"):
    """
    Print out the Morse Code

    :: Params
    - morse_symbols : List of dictionaries mapping a word to its corresponding morse symbol structure for indexing
        + Type: List
    - delimiter : Specify a separator/delimiter to place at the end of every word
        + Type: String
        + Default: "/"
    """
    # Initialize Variables
    result = ""

    # Output morse code
    for i in range(len(morse_symbols)):
        # Get current word entry
        curr_entry = morse_symbols[i]

        # Iterate through current entry 
        for curr_word, curr_morse_list in curr_entry.items():
            # Print word to morse 
            print("Translated Morse Code: {} = {} {}".format(curr_word, ' '.join(curr_morse_list), delimiter))
            result += " ".join(curr_morse_list)

            # End with the separator until there are no more words
            result += " {} ".format(delimiter)

    # Output
    return result

def main():
    # Initialize Variables

    # Obtain user input
    u_Msg = str(input("Please enter a message to convert into morse code: "))
    print("1 : The morse code symbols mapped to the characters are the strings\n2 : The morse code symbols are separated in a list")
    u_Dataset = int(input("Please enter which dataset to use? [1|2]: "))

    # Translate and obtain translation
    morse_symbols = translate_dataset(u_Msg, u_Dataset)

    print("Morse Symbols: {}".format(morse_symbols))

    # Print dataset
    result = prepare_dataset(morse_symbols)
    print(result)

if __name__ == "__main__":
    main()

