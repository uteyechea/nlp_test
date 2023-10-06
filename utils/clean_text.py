import string

def remove_non_alphabetic(input_string):
    return ''.join([char for char in input_string if char.isalpha() or char.isspace()])

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

def run(input_text:str):
    text = remove_non_alphabetic(input_text)
    return text

