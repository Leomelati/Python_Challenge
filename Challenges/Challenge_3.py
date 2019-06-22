# We can found it at the source code

import requests

# Get the Source Code
http = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")

# Remove the line breaks of the text in the source code
source_code = http.text.replace("\n","")

# Separete the text by the comment mark
textos = source_code.split("<!--")

#Create a list that I will use to storage the letters
letters = []

# "posição" will be used to track the letter index
posição = 0
for letter in textos[1]:
    if letter.islower():
        # Get the four letter before and after
        seleção = textos[1][max(posição - 4,0): posição + 5]
        primeira = seleção[0]
        ultima = seleção[-1]
        # Check if the first and the last one letter in the selection is lowercase
        if primeira.islower() and ultima.islower():
                tres_primeiras = seleção[1:4]
                tres_ultimas = seleção[5:-1]
                #Check if the three letters before and after are uppercase
                if tres_primeiras.isupper() and tres_ultimas.isupper():
                        letters.append(letter)

    posição += 1    

# Join the letters of the list
print("".join(letters))

# http://www.pythonchallenge.com/pc/def/linkedlist.php is the answer
