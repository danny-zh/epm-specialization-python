
def concat_list(words:list = []) -> str:
    """
    This function takes a list of words and returns a string formed by concatenating
    the characters at the same index from each word in the list.

    :param words: A list of strings. Defaults to an empty list.
    :return: A string formed by concatenating the characters at the same index from each word in the list.
    """
    new_word = [ word[num] for num, word in enumerate(words) ] 
    new_word = "".join(new_word)
    return new_word

if __name__ == "__main__":
    """
    This is the main function that demonstrates the usage of the contact_list function.
    It creates a list of words and calls the contact_list function with that list.
    It then prints the result.
    """
    words = ["yoda", "best", "has"]
    print(concat_list(words))