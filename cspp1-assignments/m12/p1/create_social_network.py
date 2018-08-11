'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    cnt_string = 0
    for input_i in data:
        cnt_string += len(data[input_i])
    return data
def main():
    '''
    main function is written here
    '''
    n_input = input()
    data = {}
    for n_input in range(int(n_input)):
        s_string = input()
        l_len = s_string.split('follows')
        if l_len[0] not in data:
            data[l_len[0]] = [l_len[1]]
        else:
            data[l_len[0]].append(l_len[1])
    print(create_social_network(data))
if __name__ == "__main__":
    main()
