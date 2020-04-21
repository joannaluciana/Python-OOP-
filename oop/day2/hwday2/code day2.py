"""
Please write your implementation in place of pass keyword.
After you will are ready to test your implementation run whole
file. There are 16 test cases all of them should Pass
"""


def identity(nums):
    """Identity:
    Given a list of numbers, write a list comprehension that produces a copy of the list.
        >>> identity([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]

        >>> identity([])
        []
    """
    # copy_list=[]
    # for x  in nums: copy_list.append(x)

    return [x for x in nums]


def doubled(nums):
    """Doubled:
    Given a list of numbers, write a list comprehension that produces a list of each number doubled.
        >>> doubled([1, 2, 3, 4, 5])
        [2, 4, 6, 8, 10]
        >>> doubled([-2, 2, -10, 10])
        [-4, 4, -20, 20]
    """

    return [2 * x for x in nums]


def squared(nums):
    """Squared:
    Given a list of numbers, write a list comprehension that produces a list of the squares of each number.
        >>> squared([1, 2, 3, 4, 5])
        [1, 4, 9, 16, 25]
        >>> squared([-2, 2, -10, 10])
        [4, 4, 100, 100]
    """
    return[x**2 for x in nums]


def evens(nums):
    """Evens:
    Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.
        >>> evens([1, 2, 3, 4, 5])
        [2, 4]
        >>> evens([1, 3, 5])
        []
        >>> evens([-2, -4, -7])
        [-2, -4]
    """
    return [x for x in nums if x%2==0 ]


def odds(nums):
    """Odds:
    Given a list of numbers, write a list comprehension that produces a list of only the odd numbers in that list.
        >>> odds([1, 2, 3, 4, 5])
        [1, 3, 5]
        >>> odds([2, 4, 6])
        []
        >>> odds([-2, -4, -7])
        [-7]
    """
    return[x for x in nums if x%2!=0]


def positives(nums):
    """Positives:
    Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
        >>> positives([-2, -1, 0, 1, 2])
        [1, 2]
    """

    return [ x for x in nums if x>0]


def selective_stringify_nums(nums):
    """Selectively stringify nums:
    Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.
        >>> selective_stringify_nums([25, 91, 22, -7, -20])
        ['25', '-20']
    """
    return [str(x) for x in nums if x%5==0]


def words_not_the(sentence):
    """Words not 'the'
    Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
        >>> words_not_the('the quick brown fox jumps over the lazy dog')
        [5, 5, 3, 5, 4, 4, 3]
    """
    split_sent=sentence.split()
    return[len(split_sent[x]) for x in range(0,len(split_sent)) if split_sent[x]!='the']


def vowels(word):
    """Vowels:
    Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word.
        >>> vowels('mathematics')
        ['a', 'e', 'a', 'i']
    """
    copy_list = []
    vowel_l = ["a", "o", "e", "i"]
    return[ word[x] for x in range(0,len(word)) if word[x] in vowel_l ]

def my_test(word2):
    """
    Given a string.
        >>> my_test("Addicted to code")
        4
    """

    return len(["♥" for x in word2 if x =="d"])





# STOP HERE! You solved everything!
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n*** ALL TESTS PASSED!\n')
