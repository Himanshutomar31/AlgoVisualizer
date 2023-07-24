def wordBreak(word):
    """
    Function to determine if the given word can be segmented into space-separated words
    such that each word is present in the dictionary.

    Args:
        word (str): The input word to be segmented.

    Returns:
        bool: True if the word can be segmented into valid words from the dictionary, False otherwise.
    """

    global dictionary

    size = len(word)

    # Base Case: If the word is empty, it can be segmented.
    if (size == 0):
        return True

    # Try all possible prefixes of the word and check if they are present in the dictionary.
    for i in range(1, size + 1):
        if (word[0:i] in dictionary and wordBreak(word[i: size])):
            return True

    # If no segmentation is possible, return False.
    return False


# Dictionary to store valid words
dictionary = set()

# Temporary list of valid words
temp_dictionary = ["mobile", "samsung", "sam", "sung", "man",
                   "mango", "icecream", "and", "go", "i", "like", "ice", "cream"]

# Add valid words to the dictionary
for temp in temp_dictionary:
    dictionary.add(temp)


def main():
    """
    Main function to check if the word "ilikesamsung" can be segmented into valid words.

    Returns:
        str: "Yes" if the word can be segmented, "No" otherwise.
    """
    return "Yes" if wordBreak("ilikesamsung") else "No"
