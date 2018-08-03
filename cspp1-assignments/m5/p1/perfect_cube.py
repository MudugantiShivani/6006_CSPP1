# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    # input is captured in s
    cube_num=int(input())
    epsilon = 0.01
    inc = 1
    guess = 0

    while guess <= cube_num:
        if abs(guess**3 -cube_num) < epsilon:
            break
        else:
            guess += inc

    if abs(guess**3 - cube_num) >= epsilon:
        print('failed')
    else:
        print(cube_num)
    # watch out for the data type of value stored in s
    # your code starts here

if __name__ == "__main__":
    main()
