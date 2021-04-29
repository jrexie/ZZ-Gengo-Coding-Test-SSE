from itertools import combinations


def cleanup_string(word):
    """
        Removes all non-alphabet characters from the input string

        Parameters
        ----------
        word : str
            The string to check

        Returns
        -------
        string
            String with only alphabet characters

        Raises
        ------
        TypeError
            If input is not a string
        """
    if not isinstance(word, str):
        raise TypeError

    # remove non alphabet characters
    return "".join(c.lower() for c in word if c.isalpha())


def is_palindrome(word):
    """
    Checks if a given string is palindromic.

    Parameters
    ----------
    word : str
        The string to check

    Returns
    -------
    True
        Input string is palindromic

    False
        Input string is not palindromic

    Raises
    ------
    TypeError
        If input is not a string
    """

    word = cleanup_string(word)

    if len(word) <= 0:
        return False

    # reverse the word
    word_rev = word[::-1]

    return word == word_rev


def get_longest_palindromic_substr(word):
    """
    Gets the longest palindromic substring of the given string.
    Non-alphabet characters are ignored in the checking.

    Parameters
    ----------
    word : str
        The string to check

    Returns
    -------
    non-zero string
        The longest palindromic substring (without non-alphabet characters)

    empty string
        If there is no palindromic substring

    Raises
    ------
    TypeError
        If input is not a string
    """

    word = cleanup_string(word)

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
            return substr

    return ""


def get_min_palindromic_split(word):
    """
    Gets the minimum number of string split necessary so that all substrings are palindromic

    Parameters
    ----------
    word : str
        The string to check

    Returns
    -------
    non-zero integer
        The minimum number of necessary splits

    0
        If the string could not be split to meet palindromic substring requirements

    Raises
    ------
    TypeError
        If input is not a string
    """
    word = cleanup_string(word)

    if len(word) <= 1:
        return 0

    # list of palindromic substrings
    substr_list = []

    while True:
        substr = get_longest_palindromic_substr(word)

        if len(substr) <= 0:
            return 0

        substr_list.append(substr)
        # remove the first occurrence of the palindromic substring from the current string
        word = word.replace(substr, "", 1)

        if is_palindrome(word):
            substr_list.append(word)
            break

    return len(substr_list) - 1
