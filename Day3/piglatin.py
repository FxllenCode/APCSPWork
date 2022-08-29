import re

text: str = input("Input the text to convert to PigLatin... ")

textList: list = text.split(" ")
newTextList: list = []

for text in textList:
    text = text.lower()
    text = re.sub(r"\W", "", text)
    newText = ""

    if re.search(r"[aeiou]*[a-z]", text):
        newText = text + "yay"
    else:
        newText = text[1:] + text[:1] + "ay"

newTextList.append(newText)


print(" ".join(newTextList))
