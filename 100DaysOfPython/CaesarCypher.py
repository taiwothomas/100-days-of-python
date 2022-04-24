from caesar_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
choice = 'yes'
def caesar(text, shift, direction):
  i = 0
  if shift > 25:
    shift = shift % 26
  if direction == "decode":
    shift *= -1
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
  print(f"Here is the {direction}d result: {text}")
print(logo)
while choice == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encode" or direction == "decode":
    caesar(text,shift,direction)
  else:
    choice = input('Will you like to do another cipher? ').lower
  choice = input('Will you like to do another cypher? "yes" or "no" ')
if choice != 'yes':
  print("Goodbye!")