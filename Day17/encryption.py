def letterScramble(word):
    word = word.lower()
    newWord = word.replace("b", "c")
    newWord = newWord.replace("d", "e")
    newWord = newWord.replace("f", "g")
    newWord = newWord.replace("h", "i")
    return newWord

def numberScramble(word):
    word = word.lower()
    newWord = word.replace("i", "1")
    newWord = newWord.replace("e", "3")
    newWord = newWord.replace("a", "4")
    newWord = newWord.replace("o", "0")
    return newWord

def ceaserCipher(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encryptedWord = ""
    word = word.lower()
    for letter in word:
        letterIndex = alphabet.find(letter)
        if (letterIndex + 3) > len(alphabet):
            encryptedWord += alphabet[letterIndex - 26 + 3]
        else:
            encryptedWord += alphabet[letterIndex + 3]
    return encryptedWord

mysteryWord = "Thursday"
mysteryWord = letterScramble(mysteryWord)
print(mysteryWord)
mysteryWord = numberScramble(mysteryWord)

print(mysteryWord)
mysteryWord = ceaserCipher("hello")
print(mysteryWord)

