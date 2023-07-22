def wordBreak(word):

    global dictionary

    size = len(word)

    if (size == 0):
        return True

    for i in range(1, size + 1):

        if (word[0:i] in dictionary and wordBreak(word[i: size])):
            return True

    return False


dictionary = set()


temp_dictionary = ["mobile", "samsung", "sam", "sung", "man",
                   "mango", "icecream", "and", "go", "i", "like", "ice", "cream"]


for temp in temp_dictionary:
    dictionary.add(temp)


def main():
    return "Yes" if wordBreak("ilikesamsung") else "No"
