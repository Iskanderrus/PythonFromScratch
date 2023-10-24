from pathlib import Path


def count_words(path_variable: Path) -> None:
    """
    Count the approximate number of words in a file
    :return: None
    """
    try:
        contents = path_variable.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'Sorry, the file {str(path_variable).split("/")[-1]} does not exist.')

    else:
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f'The file {str(path_variable).split("/")[-1]} has about {num_words} words.')


filenames = ['the_time_machine.txt', 'siddhartha.txt', 'alice_in_wonderland.txt']

for file in filenames:
    path = Path(f'../../../../Downloads/{file}')
    count_words(path)
