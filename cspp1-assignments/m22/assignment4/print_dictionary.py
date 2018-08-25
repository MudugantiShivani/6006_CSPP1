'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    In this function we read the given dictionary and sort it according to
    the keys and frequency and print the key and frequency
    '''
    newdict = sorted(dictionary.keys())
    for element in newdict:
        print(element, '-', dictionary[element])
def main():
    '''
    Thuis is the main function which we call to execute the progfram
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
