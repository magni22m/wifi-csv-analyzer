#Maryanne Magnier
#Lab 5
import csv
import re
import string

def wordFrequency(filename):
    '''This function should read the specified file and return a dictionary.
    Each word in the specified file should be a key in the dictionary.
    The values associated with the word should be the number of times that the
    word appeared in the text.'''

    my_dictionary = {}

    filename = open(filename, 'r')
    file_lines = filename.readlines()

    # for each line, split up the words and ignore punctuation and lowercase
    for line in file_lines:
        my_line = re.sub('[' + string.punctuation + ']', '', line)
        my_line = my_line.lower()
        each_word = line.split()

        # count the number of times each word is in the dictionary
        for word in each_word:
            if word in my_dictionary:
                my_dictionary[word] += 1

            else:
                my_dictionary[word] = 1

    return my_dictionary


def mergeFrequencies(ls):
    '''This function takes a list of dictionaries. It returns a new dictionary.
    The original dictionaries passed into the function should not be modified.'''

    result = {}
    # merge the two lists together
    # values and keys will be merged as needed
    for dictionary in ls:
        for key in dictionary:
            if key in result:
                result[key] += dictionary[key]
            else:
                result[key] = dictionary[key]
    return result


def parse(string):
    '''This function takes a single string as its only argument. If the string
    can cast to an integer, parse should return that integer. If it can be
    parsed to a float, then it should return that float. If it can do neither,
    it can return the original string.'''

    try:
        return int(string)
    except ValueError:
        pass

    try:
        return float(string)

    except ValueError:
        pass
    return string


def importCSV(filename):
    '''This takes a file name (a string) and returns a list of lists representing
    the data in the file. Each list in the lists is a row of the table.
    Each element of the row should be an integer if the element can be
    parsed as an integer, a float if the element can parse as a float, or
    a string if the element can't be parsed as either an integer or a float.
    Use the parse function above.'''

    second_list= []
    file = open(filename, 'r')

    line = file.readline()

    # break down each line into terms, put them into a new list
    for line in file:
        new_list = []

        line = line.rstrip("\n")
        terms = line.split(',')

        for term in terms:
            parsed_term = parse(term)
            new_list.append(parsed_term)

        second_list.append(new_list)

    file.close()
    return second_list

#Boston's Open Data Hub
def mostPopularNeighborhood(filename):
    '''This function will take a file and return the most popular
    neighborhood where popularity is measured by the total number of
    connections recorded in the dataset.'''

    # call importCSV on the file
    imported_file = importCSV(filename)
    # make an empty dictionary
    my_dictionary = {}

    # the neighborhood will be the key, the connections number will be the value
    # the first element of each list is the key
    for my_list in imported_file:
        my_dictionary[my_list[0]] = my_dictionary.get(my_list[0], 0) + my_list[2]

    return get_max(my_dictionary)

def mostPopularDate(filename):
    '''This function will take a file and return the most popular
    date where popularity is measured by the total number of
    connections recorded in the dataset.'''

    # call importCSV on the file
    imported_file = importCSV(filename)
    # make an empty dictionary
    my_dictionary = {}

    # get the data needed (in this case, date and time) using spits
    for my_list in imported_file:
        date_and_time = my_list[1]
        date = date_and_time[0:11]
        my_dictionary[date] = my_dictionary.get(date, 0) + my_list[2]

    return get_max(my_dictionary)


def mostPopularMonth(filename):
    '''This function will take a file and return the most popular
    month where popularity is measured by the total number of
    connections recorded in the dataset.'''

    # call importCSV on the file
    imported_file = importCSV(filename)
    # make an empty dictionary
    my_dictionary = {}

    # get relevant data, again using splits
    for my_list in imported_file:
        date_and_time = my_list[1]
        month = date_and_time[0:2]
        my_dictionary[month] = my_dictionary.get(month, 0) + my_list[2]

    return get_max(my_dictionary)


def get_max(dictionary):
    '''This function is a helper for all of the functions.'''

    # merges in the beginning to handle the summation problem
    new_dictionary = {}
    for key in dictionary:
        if key in new_dictionary:
            new_dictionary[key] += dictionary[key]
        else:
            new_dictionary[key] = dictionary[key]

    # finds the maximum value in a dictionary and returns its key
    temp_key = None
    temp_value = None
    for key, value in new_dictionary.items():
        if temp_value is None or value > temp_value:
            temp_value = value
            temp_key = key

    return temp_key
