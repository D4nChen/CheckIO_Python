import operator
def checkio(text: str) -> str:
    list_of_words = [i for i in text.lower() if i.isalpha()]
    dictionary = {key: list_of_words.count(key) for key in list_of_words}
    result = max(dictionary.items(), key=operator.itemgetter(1))[0]
    for element in dictionary:
       if dictionary[element] == dictionary[result] and element < result:
            result = element
    return result