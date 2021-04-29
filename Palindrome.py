from itertools import combinations

def is_palindrome(word):
    if not isinstance(word, str):
        raise TypeError

    # remove non alphanumeric characters
    word = "".join(c for c in word if c.isalnum())

    if len(word) <= 0:
        return False

    # reverse the word
    word_rev = "".join(reversed(word))

    return word.lower() == word_rev.lower()


def get_longest_palindromic_substr(word):
    if not isinstance(word, str):
        raise TypeError

    # remove non alphanumeric characters
    word = "".join(c for c in word if c.isalnum())

    if len(word) <= 0:
        return ""

    # create a list of all substrings
    substr_list = [word[i:j] for i, j in combinations(
        range(len(word) + 1), r=2)]
    # sort in descending order based on string length
    substr_list.sort(key=len, reverse=True)
    # remove original word from the list
    substr_list.remove(word)

    # check if any of the substring is palindromic
    for substr in substr_list:
        if is_palindrome(substr):
            return substr.strip()

    return ""


def get_min_palindromic_split(word):
    if not isinstance(word, str):
        raise TypeError

    # remove non alphanumeric characters
    word = "".join(c for c in word if c.isalnum())

    if len(word) <= 1:
        return 0

    '''
    Assumption: word has to be split into palindromic subststrings
    if is_palindrome(word):
        return 0
    '''

    substr_list = []

    while True:
        substr = get_longest_palindromic_substr(word)

        if len(substr) <= 0:
            return 0

        substr_list.append(substr)
        # remove palindromic substring from the word
        word = word.replace(substr, "", 1)

        if is_palindrome(word):
            substr_list.append(word)
            break

    print(substr_list)

    return len(substr_list) - 1

