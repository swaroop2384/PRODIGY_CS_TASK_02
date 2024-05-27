#Encrypting Image
import sys
def voidEncryption():
      try:
          path = input(r'Enter Path of Image : ')
          key = int(input('Enter key for encryption of Image : '))
          print('The path of file : ', path)
          print('key for encryption :', key)
          fin = open(path , 'rb')
          image = fin.read()
          fin.close()

          image = bytearray(image)
          # performing XOR operation on each value of bytearray
          for index, values in enumerate(image):
              image[index] = values ^ key
          fin = open(path , 'wb')

          fin.write(image)
          fin.close()
          print('Ecryption Done...')

      except Exception:
            print('Error Caught : ', Exception.__name__)

#Decrypting Image
def voidDecryption():
        try:
             path = input(r'Enter path of Image : ')
             key = int(input('Enter key for encryption of Image : '))
             print('The Path of File : ', path)
             print('Note : Encryption key and Decryption key Must be Same. ')
             print('Key for Decryption : ',key)
             fin = open(path, 'rb')
             image = fin.read()
             fin.close()
             image = bytearray(image)
             #Performing XOR Operation on each value of bytearray
             for index , values in enumerate(image):
                image[index] = values ^ key
             fin = open(path , 'wb')
             fin.write(image)
             fin.close()
             print('Decryption Done...')

        except Exception:
            print('Error Caught : ', Exception.__name__)
print("Welcome to the Image Encryption ")
choice = int(input('Please Enter 1 for Encryption or\n' 
        '           2 For Decryption of Image :'))
if choice not in [1,2]:
    print("Invalid Choice!")
    sys.exit()
if choice == 1:
    print(voidEncryption())
elif choice == 2:
    print(voidDecryption())