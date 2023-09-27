def count_words_ending_with_e(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            words = text.split()
            count = 0
            for word in words:
                if word.endswith('e') or word.endswith('E'):
                    count += 1
            return count
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found")
    except Exception as e:
        print(f"An error occured: {str(e)}")

file_name = "words.txt"

word_count = count_words_ending_with_e(file_name)
if word_count is not None:
    print(f"Number of words ending with 'e': {word_count}")