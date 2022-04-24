alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
choice = 'yes'


def encrypt(text, shift):
  i = 0
  for letter in range(len(text)):
    text = list(text)
    ltr = text[i]
    if ltr in alphabet:
      position = alphabet.index(ltr)+shift
      if position > 25:
        position -= 26
      ltr = alphabet[position]
      text[i] = ltr
    i += 1
  text = "".join(text)
  print(text)

def decrypt(text, shift):
  i = 0
  for letter in range(len(text)):
    text = list(text)
    ltr = text[i]
    if ltr in alphabet:
      position = alphabet.index(ltr) - shift
      if position < 0:
        position += 26
      ltr = alphabet[position]
      text[i] = ltr
    i += 1
  text = "".join(text)
  print(text)

while choice == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 25:
    shift = shift % 26
  if direction == "encode":
    encrypt(text,shift)
  elif direction == "decode":
    decrypt(text,shift)
  else:
    choice = input('Will you like to do another cipher? ').lower
  choice = input('Will you like to do another cypher? "yes" or "no"')
if choice != 'yes':
  print("Goodbye!")