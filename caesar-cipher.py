# Función duplicar el alfabeto ABC..XYZABC...XYZ
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Pide al usuario un mensaje y retorna el valor
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Pida al usuario la llave para cifrar
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Encripta en un mensaje con base en una llave y un alfabeto
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper() # string se coloca en mayuscula
    
    # recorre todos los caracteres del mensaje
    # para cada caracter en mensaje realiza
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter) # atrapo el índice que tiene el caracter en mi alfabeto
        newPosition = position + int(cipherKey) # calculo el nuevo índice
        
        if currentCharacter in alphabet: # Verifica que el caracter pertenezca al alfabeto
            encryptedMessage += alphabet[newPosition] # anexar el caracter a mi mensaje encriptado
        else:
            encryptedMessage = encryptedMessage + currentCharacter # anexo el caracter sin alteración
    return encryptedMessage # retornaría el mensaje encriptado

# Desencriptar el mensaje
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# El orden del código
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # declaramos nuestro alfabeto
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet) # obtenemos el doble
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage() # obtenemos el mensaje a encriptar 
    print(myMessage)
    myCipherKey = getCipherKey() # obtenemos la llave para encriptar
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2) # Encriptamos
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2) # Desencriptamos
    print(f'Decypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()