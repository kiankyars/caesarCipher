def encryptOrDecrypt():
    '''Asks the user whether they want to encrpyt of decrypt'''

    Input = input("Would you like to encrypt or decrypt? (E/D): ")

    return Input[0].upper()

def getKeyAndCode():
    '''Gets the desired key and code for encryption'''

    code = input("Enter code to be encrypted: ")

    key = int(input("Enter key: "))
    
    return key, code

def getInputFile():
    '''this function requests a txt input from the user and
    asks for a file until a string ending in .txt is received,
    it then returns the file name to the main function'''

    code = ""

    while len(code) < 5 or code[-4:] != ".txt":

        if code != "":

            print(f"Invalid filename extension. Please re-enter the input filename: {code}")

        code = input("Enter file name: ")

    return code

def readFile(name):
    '''opens the file in read made and extracts the key from the
    first line and the encryption from the second line
    returns both to the main function'''

    with open(name,"r") as file:

        list = file.readlines()

        key = int(list[0].strip())

        encryptedWords = list[1].strip().lower()

        return key,encryptedWords

def decrpyt(k,c):
    '''decrypts the code using the key, has an alphabet to use for decrypting
    and the decryption is executed via a for loop with two conditions'''

    alphabet = "abcdefghijklmnopqrstuvwxyz"
        
    decryptedWord = ""

    for char in c:

        if char == " ":

            decryptedWord+=" "

        else:
            
            index = alphabet.index(char)

            new_char = alphabet[index-k]

            decryptedWord+=new_char

    return decryptedWord

def encrypt(k,c):
    '''Encrypts a code given a key'''

    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        
    encryptedWord = ""
    
    for char in c:

        if char == " ":

            encryptedWord+=" "

        else:
            
            index = alphabet.index(char)

            new_char = alphabet[index+k]

            encryptedWord+=new_char

    return encryptedWord

def writeFile(encryption,key):
    '''Writes to a .txt file'''

    with open("encryptedCode.txt", "w") as file:

        file.write(f"{key}\n{encryption}")

def main():
    '''main function that calls all of the other functions'''

    procedure = encryptOrDecrypt()

    if procedure == "D":

        name = getInputFile()

        key,code = readFile(name)

        decryptedWord = decrpyt(key,code)

        answer = ' '.join(decryptedWord.split())
        
        print(f'The decrypted message is: {answer}')

    elif procedure == "E":

        key,code = getKeyAndCode()

        encryptedWord = encrypt(key,code)

        writeFile(encryptedWord,key)

        answer = ' '.join(encryptedWord.split())
        
        print(f'The encrypted message is: {answer}\nA new file has also been added to your directory with the key and encypted code')

main()