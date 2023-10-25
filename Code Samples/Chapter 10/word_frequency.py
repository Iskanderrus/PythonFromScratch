from pathlib import Path

PATH = Path(f'../../../../Downloads/')
FILENAMES = ['the_time_machine.txt', 'siddhartha.txt', 'alice_in_wonderland.txt']
WORD = input("Type the word, you would like to count: ")


def word_frequency(path_variable: Path, list_of_files: list, word: str) -> None:
    """
    Count how many times can be a word found in a .txt file
    :path_variable: A Path type object to open a file
    :word: A string object to find a word frequency
    :return: None
    """
    for file in list_of_files:
        full_path = path_variable.joinpath(file)
        try:
            contents = full_path.read_text(encoding='utf-8')

        except FileNotFoundError:
            print(f'\nSorry, the file {full_path.name} does not exist.')
            # pass

        else:
            # Count the approximate number of the word in the file
            print(f'\nWord frequency in {full_path.name} is: {contents.lower().count(word)}')
            print(f'Word frequency in {full_path.name} with last space is: {contents.lower().count(word + " ")}')


word_frequency(path_variable=PATH, list_of_files=FILENAMES, word=WORD)
