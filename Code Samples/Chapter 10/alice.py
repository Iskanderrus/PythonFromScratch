from pathlib import Path
import string


def custom_key(some_string: str):
    """
    A function to fill the key value while sorting a list first by length, then alphabetically.
    :param some_string: A string value of the list.
    :return: Tuple of the negative string length value and string itself in lower case.
    """
    return -len(some_string), some_string.lower()


signs = string.punctuation

path = Path('../../../../Downloads/alice_in_wonderland.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f'Sorry the file {str(path).split("/")[-1]} does not exist in this directory.')
else:
    # count the words in the file
    words = contents.split()
    num_words = len(words)
    num_unique_words = len(set(words))
    print(f'The file {str(path).split("/")[-1]} has about {num_words} words and {num_unique_words} of unique words.')

    # looking for the shortest and longest word in the text.
    unique_words_list = list(set(words))
    unique_words_list = [x.strip(signs + string.digits) for x in unique_words_list]
    while unique_words_list.count(''):
        unique_words_list.remove('')
    unique_words_list.remove('•')

    unique_words_list.sort(key=custom_key, reverse=True)

    print(f'The shortest word in the file {str(path).split("/")[-1]} is {unique_words_list[0]}\nThe longest word in '
          f'the file {str(path).split("/")[-1]} is {unique_words_list[-1]}')
