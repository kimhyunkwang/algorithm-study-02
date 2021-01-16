n = int(input())
encoding_words = []

def encode(word):
    encoding_word = ''
    for char in word:
        if char == 'Z':
            encoding_word += chr(ord(char) - 25)
        else:
            encoding_word += chr(ord(char) + 1)
    return encoding_word

for i in range(n):
    word = input()
    encoding_words.append(encode(word))

for word in encoding_words:
    print(word)