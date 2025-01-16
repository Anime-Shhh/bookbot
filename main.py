def main():
    bookPath = "books/frankenstein.txt"
    text = getBookText(bookPath)
    # print(text)
    print(countWords(text))


def getBookText(bookPath):
    with open(bookPath) as file:
        text = file.read()
    return text


def countWords(text):
    return len(text.split())


main()
