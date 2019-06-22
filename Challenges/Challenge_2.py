# We can found it at the source code

import requests

http = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
source_code = http.text

textos = source_code.split("<!--")
letters = []

for letter in textos[2]:

    count = textos[2].count(letter)

    if count <= 10 and letter not in letters:
        letters.append(letter)

print(letters)

# http://www.pythonchallenge.com/pc/def/equality.html is the answer
