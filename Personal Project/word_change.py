def word_changer(c, num):
    if c.isupper():
        alphabet_num = ord(c) - 65
        new_num = (num + alphabet_num) % 26
        return chr(new_num + 65)
    else:
        alphabet_num = ord(c) - 97
        new_num = (num + alphabet_num) % 26
        return chr(new_num + 97)


print(word_changer('l', 6))  # r
print(word_changer('L', 6))  # R

print(word_changer('a', 3))  # d
print(word_changer('A', 3))  # D

print(word_changer('m', 6))  # s
print(word_changer('M', 6))  # S

print(word_changer('p', -1))  # o
print(word_changer('P', -1))  # O

print(word_changer('a', -1))  # z
print(word_changer('A', -1))  # Z

print(word_changer('a', 0))  # a
print(word_changer('A', 0))  # A

print(word_changer('z', 1))  # a
print(word_changer('Z', 1))  # A

print(word_changer('z', -1))  # y
print(word_changer('Z', -1))  # Y

print(word_changer('h', 150))  # b
print(word_changer('H', 150))  # B
