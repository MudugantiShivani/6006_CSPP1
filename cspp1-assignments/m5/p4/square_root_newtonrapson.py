# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    x = int(input())
    epsilon = 0.01
    guess = x/2.0
    while abs(guess*guess - x) >= epsilon:
        guess = guess - (((guess**2) - x)/(2*guess))
    print(str(guess))   
    # epsilon and step are initialized
    # don't change these values
    # your code starts here
if __name__== "__main__":
    main()
