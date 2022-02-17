from art import logo

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+','@','^','_','-','=','~',':',';',',','<','.','>','?','/','{','}','|','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

print(logo)
print("\n\n")
#Defining Encoder
def Encoder() :
    message = input("Type your message: ")
    shift_number = int(input("Type the shift number: "))
    encoded_msg = ""

    #Encryption part
    for any in message :
        if any in letters:
            position = letters.index(any)
            #Encryption key
            shift_number%= 89
            new_shift_num = position + shift_number
            #Encryption
            if new_shift_num < 89:
                encoded_msg += letters[new_shift_num]
            else :
                encoded_msg += letters[new_shift_num-89]
        else:
            encoded_msg+=any

        

        
    
    print(f"Here's the encoded result: {encoded_msg}")


# Defining Decoder
def Decoder() :
    message = input("Type your message: ")
    shift_number = int(input("Type the shift number: "))
    decoded_msg = ""
    #Decryption part
    for any in message :
        if any in letters:
            position = letters.index(any)
            #Decryption key
            shift_number%=89
            new_shift_num = position - shift_number
            #Decryption 
            if new_shift_num >= 0:
                decoded_msg += letters[new_shift_num]
            else :
                decoded_msg += letters[new_shift_num+89]
        else:
            decoded_msg+=any

        

        
    
    print(f"Here's the decoded result: {decoded_msg}")
        

do_again = True
while(do_again) :
    code = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if code == "encode" :
        Encoder()
    elif code == "decode" :
        Decoder()
    else :
        print("Invalid Input")
    run_again = input("Type 'yes' if you want to go again, Otherwise type 'no'.")
    if run_again == "no":
        do_again = False
    else :
        continue


