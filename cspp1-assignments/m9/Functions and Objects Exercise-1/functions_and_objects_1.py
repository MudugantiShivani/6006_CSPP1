'''
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]
'''

def apply_to_each(L, f):
    '''
    input:here the input is the list
    output:it gives the list as output after converting to abs value
    '''
    for i in range(len(L)):
        L[i] = f(L[i])
    return L


def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
