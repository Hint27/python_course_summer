# Formating String

writer = "Marker"
board_type = "White Board"

#board_description = "We are using " + board_type + " and we write on it with " + writer

board_description = f"We are using {board_type} and we write on it with {writer}. There is {10 + 3}"

print(board_description)

# Modifier
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Character Escaping
message2 = '  Hello, I\'m good. \tFine.\nI am going to class.  '

print(message2)
print(message2.lstrip())
print(message2.rstrip())
print('Menu'.center(30, '='))
print('Food'.ljust(20, '='))
print('Fruit'.rjust(20, '='))
