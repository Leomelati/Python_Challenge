from string import ascii_lowercase

msg = "map"

new_msg = []

for letter in msg:

    if letter in ascii_lowercase:

        position = ord(letter)+2

        if position >= 123:
            position = position - 26
            new_msg.append(chr(position))

        else:
            new_msg.append(chr(position))

    else:
        new_msg.append(letter)

print("".join(new_msg))

# A mensagem diz que a função "maketrans()" é recomendada para fazer esse tipo de transformarção e fala para vocÊ fazer isso no URL map fazendo ele virar OCR

# http://www.pythonchallenge.com/pc/def/ocr.html is the answer