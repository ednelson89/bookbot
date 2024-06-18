def main():
    book_path = "books/frankenstein.txt"
    book_text = getBookText(book_path)
    word_count = wordCount(book_text)
    char_count = countChars(book_text)

    printReport(book_path, word_count, char_count)


def getBookText(inString):
    with open(inString) as f:
        return f.read()


def wordCount(file_text):
    return len(file_text.split())


def countChars(inString):
    tempString = inString.lower()
    countDict = {}

    for char in tempString:
        # not normally a fan of nested ifs, but this is easy
        if char.isalpha():
            if char in countDict:
                countDict[char] += 1
            else:
                countDict[char] = 1

    # Return the dict, sorted by from highest to lowest
    return dict(sorted(countDict.items(), key=lambda key_val: key_val[1], reverse=True))


def printReport(book_path, word_count, char_count):
    print(f"--- Begin Report of: {book_path} ---")
    print(f"Word Count: {word_count} words found in document")
    print()
    for char in char_count:
        print(f"The '{char}' character appeared {char_count[char]} times.")
    print("--- End Report ---")


main()
