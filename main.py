def getBookText(bookPath):
    with open(bookPath) as file:
        text = file.read()
    return text


def countWords(text):
    return len(text.split())


def countCharacters(text):
    seen = set()
    countLib = {}
    loweredText = text.lower()
    for character in loweredText:
        if character.isalpha():
            if character not in seen:
                seen.add(character)
                countLib[character] = 1
            else:
                countLib[character] += 1

    # now sort the dictionary
    countLib = dict(sorted(countLib.items(), key=lambda item: item[1], reverse=True))
    return countLib


def printCharacters(characterCounts):
    for character in characterCounts:
        print(
            f"The '{character}' character was found {characterCounts[character]} times in the text"
        )


def main():
    bookPath = "books/frankenstein.txt"
    text = getBookText(bookPath)
    print(f"--- Begin the report of {bookPath} ---")
    print(f"{countWords(text)} words were found in the document\n")
    printCharacters(countCharacters(text))
    print("--- End report ---")


main()
