#CaesarChipher

from base64 import encode

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
exit = False
while(not exit):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text,shift,direction):
        print("In Caesar")

        if direction == "encode":
            output_string=""
            for letter in text:
                if letter in alphabet:
                    alpha_index=alphabet.index(letter)
                    alpha_index+=shift
                    if alpha_index > 25:
                        alpha_index=alpha_index%26
                    output_string+=alphabet[alpha_index]
                else:
                    output_string+=letter
            print(output_string)
        elif direction == "decode":
            output_string=""
            for letter in text:
                if letter in alphabet:
                    alpha_index=alphabet.index(letter)
                    alpha_index-=shift
                    if alpha_index < 0:
                        alpha_index=(alpha_index*-1)%26
                        alpha_index=26-alpha_index
                    output_string+=alphabet[alpha_index]
                else:
                    output_string+=letter
            print(output_string)

    caesar(text,shift,direction)
    rerun = input("Do you want to rerun? yes or no:\n").lower()
    if rerun == "no":
        exit=True

