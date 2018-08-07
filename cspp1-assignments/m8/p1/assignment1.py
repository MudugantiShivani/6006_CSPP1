"""
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
#number and returns the factorial of given number.
# This function takes in one number and returns one number.
"""
def factorial(num_in):
    '''
    input:n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if num_in == 1 or num_in == 0:
        return 1
    else:
        return num_in * factorial(num_in-1)
def main():
    """
    here the input will be a number which is positive and returns the factorial
    of the given number
    """
    a = input()
    print(factorial(int(a)))
if __name__ == "__main__":
    main()
