# Vigenere Cipher Dictionary Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish, pyperclip, vigenereCipher


def main():
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage = hackVigenere(ciphertext)

    if hackedMessage != None:
        print("Copying hacked message to clipboard:")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print("Failed to hack encryption.")


def hackVigenere(ciphertext):
    fo = open("dictionary.txt")
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip()  # remove the newline at the end
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)

        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            print()
            print("Possible encryption break:")
            print("Key " + str(word) + ": " + decryptedText[:100])
            print()
            print("Enter D for done, or just press Enter to continue breaking:")
            response = input("> ")
            if response.upper().startswith("D"):
                return decryptedText


if __name__ == "__main__":
    main()
