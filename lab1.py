from collections import deque

class cpre_lab1:
#Author - Noah Cantrell
#Cipher - RSR Cipher (Rotate, Substitue, Rotate)

    val = None
    message = None
    rotate_by = None
    regular_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    reverse_alphabet = regular_alphabet[::-1]

    #Rotate input message, substitute via a reversed alphabet key, rotate encrypted message
    def encrypt(message: str, reg_a, rev_a):
        result = []

        #remove spaces from message
        for x in message:
            if x.strip():
               result.append(x)

        d = deque(result)
        rotate_by = ((len(result) % 2) + 1)
        d.rotate(rotate_by)
        ind = 0

        for i in d:
            for j in reg_a:
                if i == j:
                    d[ind] = rev_a[reg_a.index(j)]
                    ind += 1
                    break
              
        d.rotate(rotate_by)
        message = ''.join(d)
        return message

    #Reverse encryption process
    def decrypt(message: str, reg_a, rev_a):
        d = deque(message)
        rotate_by = ((len(message) % 2) + 1)
        d.rotate(-rotate_by)
        ind = 0

        for i in d:
            for j in rev_a:
                if i == j:
                    d[ind] = reg_a[rev_a.index(j)]
                    ind += 1
                    break
        
        d.rotate(-rotate_by)
        message = ''.join(d)
        return message
    
    #Take input for encrypt or decrypt and then the user's message, output encrypted/decrypted message
    while True:
        val = input("Input 'E' for encryption or 'D' for decryption: ")

        if val == 'E' or val == 'e':
            message = input("Input the message you would like to encrypt: ")
            encrypted_msg = encrypt(message, regular_alphabet, reverse_alphabet)
            print(encrypted_msg)
            break
        elif val == 'D' or val == 'd':
            message = input("Input the message you would like to decrypt: ")
            decrypted_msg = decrypt(message, regular_alphabet, reverse_alphabet)
            print(decrypted_msg)
            break
        else:
            print("Unexpected input, try again.\n")
            continue