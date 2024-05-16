from cs50 import get_string


def main():
    text = get_string("Text: ")

    letters = numletters(text)
    words = numwords(text)
    sentences = numsentences(text)

    L = (letters / words) * 100.0
    S = (sentences / words) * 100.0
    formula = round(.0588 * L - .296 * S - 15.8)

    if formula < 1:
        print("Before Grade 1")
    elif formula > 16:
        print("Grade 16+")
    else:
        print(f"Grade {formula}")


def numletters(text):
    lettercount = 0

    for i in range(len(text)):
        if text[i].isalpha():
            lettercount += 1
    return lettercount


def numwords(text):
    wordcount = len(text.split())
    return wordcount


def numsentences(text):
    sentences = 0
    for i in range(len(text)):
        if text[i] == '.':
            sentences += 1
        elif text[i] == '!':
            sentences += 1
        elif text[i] == '?':
            sentences += 1
    return sentences


main()
