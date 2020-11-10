print("Press e to encrypt and d to decrypt ")
while True :
  encryption = input()

  if encryption == "e":
    print("What would you like to encrypt?")
    message = input()
    print("What key would you like to use?")
    key = input()
    
    ran = range(len(message))
    
    encrypted = ""
    
    for i in ran:
      currentLetter = message[i]
      currentKeyLetter = key[i % len(key)]

      numberLetter = ord(currentLetter)
      numberKeyLetter = ord(currentKeyLetter)
          
      sumOfTwoLetters = numberLetter + numberKeyLetter
          
      newNumberLetter = sumOfTwoLetters % 128

      newLetter = chr(newNumberLetter)

      encrypted = encrypted + newLetter
    
    print()
    print("The encrypted message is : ")
    print(encrypted)
    break
  elif encryption == "d":
    print("what would you like to decrypt?")
    message = input()
    print("What key would you like to use?")
    key = input()
    
    ran = range(len(message))
    
    decrypted = ""
    
    for i in ran:
      currentLetter = message[i]
      currentKeyLetter = key[i % len(key)]

      numberLetter = ord(currentLetter)
      numberKeyLetter = ord(currentKeyLetter)
          
      sumOfTwoLetters = numberLetter - numberKeyLetter
          

      newNumberLetter = sumOfTwoLetters % 128

      newLetter = chr(newNumberLetter)

      decrypted = decrypted + newLetter
    
    print()
    print("The decrypted message is : ")
    print(decrypted)
    break
  else:
    print("press e or d only")
