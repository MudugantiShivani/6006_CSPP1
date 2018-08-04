'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input and print the product of digits
    '''
    int_input = int(input())
    rem = 0
    final = 1
    if int_input == "0":
        print("0")
    elif int_input>0:
        while (int_input>0):
            rem = int_input%10
            int_input = int_input//10
            final = final*rem
    print(final)
if __name__ == "__main__":
    main()
