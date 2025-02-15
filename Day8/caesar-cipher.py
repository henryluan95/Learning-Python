alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
import numbers

print(logo)
should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
        #e.g.
        #plain_text = "hello"
        #shift = 5
        #cipher_text = "mjqqt"
        #print output: "The encoded text is mjqqt"

        ##HINT: How do you get the index of an item in a list:
        #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

    def caesar (text, shift, direction):
        if(shift > 26):
            shift = shift % 26

        if(direction == "encode"):
            alphabet_first_haft = alphabet[0: shift]
            alphabet_second_haft = alphabet[shift:]
        else:
            alphabet_second_haft = alphabet[-shift:]
            alphabet_first_haft = alphabet[0: -shift]

        shifted_alphabet = alphabet_second_haft + alphabet_first_haft

        index_list = []
        for letter in text:
            if (alphabet.count(letter) > 0):
                index_list.append(alphabet.index(letter))
            else:
                index_list.append(letter)

        encoded_string = ""
        for index in index_list:
            if(isinstance(index, numbers.Number)):
                encoded_string += shifted_alphabet[index]
            else:
                encoded_string += index

        print(f'Your code is {encoded_string}')

    caesar(text, shift, direction)
    code_again = input("Do you want to continue? Answer yes or no\n")
    if (code_again == "no"):
        should_continue = False
        print("Bye")
