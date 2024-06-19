import sys


def main():
    book_path = get_path()
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)

    print_report(book_path, word_count, char_count)


def get_path():
    print(
        "Please provide the relative path to your .txt file, or pass nothing to view a demo:"
    )
    temp_path = input()

    if not temp_path:
        print("You have not provided a path; a demo file will be used instead.")
        print("-----------------------------------------------")
        temp_path = "books/frankenstein.txt"

    return temp_path


def get_book_text(in_path):
    try:
        with open(in_path) as f:
            return f.read()
    except:
        print("Oops, the path you provided failed; the program will close.")
        sys.exit(0)


def count_words(file_text):
    return len(file_text.split())


def count_chars(inString):
    temp_string = inString.lower()
    count_dict = {}

    for char in temp_string:
        # not normally a fan of nested ifs, but this is easy
        if char.isalpha():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1

    # Return the dict, sorted by from highest to lowest
    return dict(
        sorted(count_dict.items(), key=lambda key_val: key_val[1], reverse=True)
    )


def print_report(book_path, word_count, char_count):
    print(f"--- Begin Report of: {book_path} ---")
    print(f"Word Count: {word_count} words found in document")
    print()
    for char in char_count:
        print(f"The '{char}' character appeared {char_count[char]} times.")
    print("--- End Report ---")


main()
