user_input = str(input("Введите слово:"))
letter_1 = ord(user_input[0])
if 97 <= letter_1 <= 122:
    letter_1 -=32
capitalized = chr(letter_1) + user_input[1:]
print("Результат:", capitalized)