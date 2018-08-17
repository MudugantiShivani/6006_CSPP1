'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILENAME = "stopwords.txt"

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    tempdict1 = {}
    tempdict2 = {}
    sum_in_numerator = 0
    sumofdict1 = 0
    sumofdict2 = 0
    for word in dict1:
        if word in tempdict1:
            tempdict1[word] += 1
        else:
            tempdict1[word] = 1
    for word in dict2:
        if word in tempdict2:
            tempdict2[word] += 1
        else:
            tempdict2[word] = 1
    frequencyof_words = {}
    keyvalue = set(list(tempdict1.keys()) + list(tempdict2.keys()))
    for key in keyvalue:
        frequencyof_words[key] = [0, 0]
    for key in tempdict1:
        frequencyof_words[key][0] = tempdict1[key]
    for key in tempdict2:
        frequencyof_words[key][1] = tempdict2[key]
    for key in frequencyof_words:
        sum_in_numerator = sum_in_numerator + (frequencyof_words[key][0] * frequencyof_words[key][1])
    numerator = sum_in_numerator
    for key in frequencyof_words:
        sumofdict1 = sumofdict1 + (frequencyof_words[key][0]**2)
        sumofdict2 = sumofdict2 + (frequencyof_words[key][1]**2)
    denominator = (math.sqrt(sumofdict1) * math.sqrt(sumofdict2))
    distance_indocument = numerator/ denominator
    return distance_indocument
def load_stopwords(file):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file, 'r') as file_name:
        for line in file_name:
            stopwords[line.strip()] = 0
    return stopwords
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input().lower()
    input2 = input().lower()
    character = "1234567890.,!?$%^&@#*'-()"
    for char in character:
        input1 = input1.replace(char, '')
        input2 = input2.replace(char, '')
    inputin_list1 = input1.split()
    inputin_list2 = input2.split()
    temporarylist_1 = list(inputin_list1)
    temporarylist_2 = list(inputin_list2)
    stop_words = load_stopwords(FILENAME)
    for word in temporarylist_1:
        if word in stop_words.keys():
            inputin_list1.remove(word)
    for word in temporarylist_2:
        if word in stop_words.keys():
            inputin_list2.remove(word)
    if '' in inputin_list1:
        inputin_list1.remove('')
    if '' in inputin_list2:
        inputin_list2.remove('')
    print(similarity(inputin_list1, inputin_list2))
if __name__ == '__main__':
    main()
    