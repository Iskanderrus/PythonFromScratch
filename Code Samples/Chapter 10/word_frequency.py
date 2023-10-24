from pathlib import Path


def word_frequency(path_variable: Path, word: str) -> None:
    """
    Count how many times can be a word found in a .txt file
    :path_variable: A Path type object to open a file
    :word: A string object to find a word frequency
    :return: None
    """
    try:
        contents = path_variable.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'\nSorry, the file {str(path_variable).split("/")[-1]} does not exist.')
        #pass

    else:
        # Count the approximate number of the word in the file
        print(f'\nWord frequency in {str(path_variable).split("/")[-1]} is: {contents.lower().count(word)}')
        print(f'Word frequency in {str(path_variable).split("/")[-1]} with last space is: {contents.lower().count(word+" ")}')


filenames = ['the_time_machine.txt', 'siddhartha.txt', 'alice_in_wonderland.txt']

for file in filenames:
    path = Path(f'../../../../Downloads/{file}')
    word_frequency(path, 'the')


