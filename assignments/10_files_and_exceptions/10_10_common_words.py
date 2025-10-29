def count_word(filename, word):
    """Count how many times a word appears in a text file."""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")
    else:
        word_count = contents.lower().count(word)
        print(f"The word '{word}' appears about {word_count} times in {filename}.")


filenames = ['alice.txt', 'moby_dick.txt', 'sherlock.txt']

for filename in filenames:
    count_word(filename, 'the')

