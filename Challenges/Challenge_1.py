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

# The messages says that the function "maketrans()" is recommended to do this kind of transformation and told you that you need to do this at the URL

# http://www.pythonchallenge.com/pc/def/ocr.html is the answer