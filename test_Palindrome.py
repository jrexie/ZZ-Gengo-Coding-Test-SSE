from unittest import TestCase
from Palindrome import *


class Test(TestCase):
    def test_is_palindrome(self):
        # ----- palindromes -----
        # single character
        self.assertEqual(True, is_palindrome("a"))
        # odd-length string
        self.assertEqual(True, is_palindrome("aba"))
        # even-length string
        self.assertEqual(True, is_palindrome("abba"))
        # string with spaces
        self.assertEqual(True, is_palindrome("nurses run"))
        # string with special characters
        self.assertEqual(True, is_palindrome('Al lets Della call Ed "Stella."'))
        # very long string
        self.assertEqual(True,
                         is_palindrome('Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, '
                                       'Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, '
                                       'Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, '
                                       'Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, '
                                       'Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, '
                                       'and Ellen sinned.'))

        # ----- not palindromes -----
        # empty string
        self.assertEqual(False, is_palindrome(""))
        # odd-length string
        self.assertEqual(False, is_palindrome("abc"))
        # even-length string
        self.assertEqual(False, is_palindrome("abcd"))
        # string with spaces
        self.assertEqual(False, is_palindrome("nurses run xxx"))
        # string with special characters
        self.assertEqual(False, is_palindrome('Al lets Della call Ed "Stella xxx."'))
        # very long string
        self.assertEqual(False,
                         is_palindrome('Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, '
                                       'Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, '
                                       'Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, '
                                       'Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, '
                                       'Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, '
                                       'and Ellen sinned xxx.'))
        # no alphanumeric characters
        self.assertEqual(False, is_palindrome("!#$%&@"))

        # ----- invalid inputs -----
        with self.assertRaises(TypeError):
            is_palindrome()

        with self.assertRaises(TypeError):
            is_palindrome(121)

    def test_get_longest_palindromic_substr(self):
        # ----- with palindromic substring -----
        # single character palindromic substring
        self.assertEqual("a", get_longest_palindromic_substr("abc"))
        # same letters
        self.assertEqual("aa", get_longest_palindromic_substr("aaa"))
        # right-side palindromic substring
        self.assertEqual("xyzzyx", get_longest_palindromic_substr("abaxyzzyxf"))
        # left-side palindromic substring
        self.assertEqual("nursesrun", get_longest_palindromic_substr("nurses run xxx"))
        # non palindromic string with middle palindromic substring
        self.assertEqual("nursesrun", get_longest_palindromic_substr("abc nurses run xxx"))
        # palindromic string
        self.assertEqual("ursesru", get_longest_palindromic_substr("nurses run"))
        # palindromic string with special characters
        self.assertEqual('lletsDellacallEdStell', get_longest_palindromic_substr('Al lets Della call Ed "Stella."'))

        # ----- without palindromic substring -----
        # empty string
        self.assertEqual("", get_longest_palindromic_substr(""))
        # single-character string
        self.assertEqual("", get_longest_palindromic_substr("a"))
        # non-alphanumeric string
        self.assertEqual("", get_longest_palindromic_substr("!#$%&@"))

        # ----- invalid inputs -----
        with self.assertRaises(TypeError):
            get_longest_palindromic_substr()

        with self.assertRaises(TypeError):
            get_longest_palindromic_substr(121)

    def test_get_min_palindromic_split(self):
        # ----- Can be divided where all substrings are palindromic -----
        # string is palindromic, single character
        self.assertEqual(0, get_min_palindromic_split("a"))
        # string is palindromic, multiple characters
        self.assertEqual(1, get_min_palindromic_split("aaa"))  # a/aa
        # string is not palindromic, multiple-character palindromic substrings
        self.assertEqual(1, get_min_palindromic_split("nurses run aba"))  # nursesrun/aba
        # string is not palindromic, single-character palindromic substrings
        self.assertEqual(2, get_min_palindromic_split("abc"))  # a/b/c
        # string is not palindromic, multiple palindromic substrings
        self.assertEqual(2, get_min_palindromic_split("noonabbad"))  # noon/abba/d
        self.assertEqual(3, get_min_palindromic_split("noonabbadaaaaaaa"))  # noon/abba/d/aaaaaaa
        self.assertEqual(6, get_min_palindromic_split("noonabcdef"))  # noon/a/b/c/d/e/f

        # ----- Cannot be divided where all substrings are palindromic -----
        # empty string
        self.assertEqual(0, get_min_palindromic_split(""))
        # string is not alphanumeric
        self.assertEqual(0, get_min_palindromic_split("!#$%&@"))

        # ----- invalid inputs -----
        with self.assertRaises(TypeError):
            get_min_palindromic_split()

        with self.assertRaises(TypeError):
            get_min_palindromic_split(121)
