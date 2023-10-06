import string

def remove_non_alphabetic(input_string:str):
    return ''.join([char for char in input_string if char.isalpha() or char.isspace()])

def other_pre_processing_methods():
    pass

def run(input_text:str):
    text = remove_non_alphabetic(input_text)
    return text

