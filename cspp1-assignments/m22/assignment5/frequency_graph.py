'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''
    In this program we read the dictionary and store the values
    of the word repetition and replace that with "#"
    '''

    newdict = sorted(dictionary.keys())
    for element in newdict:
        print(element, '-', "#" * dictionary[element])

def main():
    '''
    this is the main function of the program
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
