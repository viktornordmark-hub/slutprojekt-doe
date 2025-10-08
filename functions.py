'''Gemensamma funktioner'''
def print_heading(text):
    '''printar '===' ovan/under '''
    print("-"*len(text))
    print(text)
    print("-"*len(text))
#konvertera bytes till gb
def bytes_to_gb(bytes_size):
    return "{:.2f}".format(bytes_size / (1024 ** 3))
