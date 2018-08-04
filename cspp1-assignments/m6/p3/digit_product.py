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
    a = int_input
    rem = 0
    final = 1
    if int_input < 0:
        int_input = s-(int_input)
    while int_input > 1:
        rem = int_input%10
        int_input = int_input//10
        final = final*rem
    if a>0:
        print(final)
    if a==0:
        print(rem)
    if a<0:
        print(-final)
if __name__ == "__main__":
    main()
