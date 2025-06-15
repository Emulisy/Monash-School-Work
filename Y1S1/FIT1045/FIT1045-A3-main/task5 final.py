"""
Team: Applied5 <Insert Your Team Name>
Student Names: Chew Zu Yuet, Ian Zhang
Date: January 22, 2025
"""

############## ENCRYPT OR DECRYPT ##############

def encrypt_decrypt(given_string,password:str,encrypt:bool) -> list:
    """
    This function will encrypted and decrypted text according to given boolean signal using given string and password
    param:
    given_string: String that we are going to encrypt or decrypt
    password: String that is use for the encrypting or decrypting of the string
    encrypt: signal whether to encrypt or decrypt text
    """
    encrypted_string= [ord(symbol) for letter in given_string for symbol in letter] # encrypting string given
    encrypted_password=[ord(letter) for letter in password] #encrypting password given
    new_encrypted_password=list(map(lambda encrypted_number:int((encrypted_number + 1) / 2)if encrypted_number%2!=0 else encrypted_number//2 ,encrypted_password)) #key password of each index /2
    encrypted_password=new_encrypted_password.copy() #copy from new_encrypted_password to encrypted_password so new_encrypted_password can be use later
    direction = 1  #indicate which direction to append

    
    while len(encrypted_password)<len(encrypted_string): #loop for repeating key but backward if length of string is longer than key
        for encrypted_password_index in range((len(new_encrypted_password))):
            if len(encrypted_password)<len(encrypted_string): 
                if direction==1: #append from the back
                    encrypted_password.append(new_encrypted_password[-(encrypted_password_index+1)]) #add from the back of the new encryption password list 
                else:
                    encrypted_password.append(new_encrypted_password[encrypted_password_index]) # add from the front of the new encryption password list
        direction*=-1 #change direction when one iteration is done 

    if encrypt==True:
        encrypted_text =[] 
        for encrypted_string_index in range(len(encrypted_string)):#get encrypted text by adding key and word
            sum_of_encrypted_password_string=encrypted_password[encrypted_string_index]+encrypted_string[encrypted_string_index] #sum up the key and word on each index
            encrypted_text.append(sum_of_encrypted_password_string) # add into list
    

        for number in range(len(encrypted_text)): # to convert encrypted text for output
            encrypted_text[number]=chr(encrypted_text[number])

        return encrypted_text

    #DECRYPTED
    elif encrypt==False: # to decrypted text
        decrypted_text=[]
        for symbol in range(len(encrypted_string)):#work backward and minus encrypted text with encrypted password
            sum_of_decrypted_password_string=encrypted_string[symbol]-encrypted_password[symbol]
            if sum_of_decrypted_password_string<0:
                sum_of_decrypted_password_string*=-1
            decrypted_text.append(sum_of_decrypted_password_string)

        for number in range(len(decrypted_text)): #convert into actual text
            decrypted_text[number]=chr(decrypted_text[number])
        return decrypted_text

#add any other Task 1 helper functions here
    
############## DECRYPT FILE ##############

def decrypt_file(file_name_decrypted,file_name_possible_password) -> list:
    """
    This function is to read file and decrypt the enncrypted text using the encrypt_decrypt function
    param:
    file_name_decrypted: file we need to decrypted
    file_name_possible_password: file with possible password
    """
    with open(file_name_decrypted,'r') as message: # open file_name_decrypted and read file line by line
        content_message=message.readlines()

    encrypted_content=[]
    actual_message=[]
    for lines in range(len(content_message)): #loop thru content_message and find ";" because that is the delimiter
        for symbol in range(len(content_message[lines])):
            if content_message[lines][symbol]==';':
                actual_message.append(content_message[lines][symbol+2:].strip('\n').strip(' ')) #list containing last 3 actual_message
                new_line_content_message=content_message[lines][:symbol-1].strip('\n') 
                encrypted_content.append(new_line_content_message)#message we got to decrypt and put it in a list

    with open(file_name_possible_password,'r') as password: #read password file
        content_password=password.read().split('\n')[:-1]
    decrypted_message=[]

    for content in range(len(encrypted_content)): #loop thru every thing on the encrypted_content list to decrypt the text in it one by one
        for password_index in range(len(content_password)): # for every content in encrypted_content we try with diffrent password possible
            new_decrypted_message=''.join(encrypt_decrypt(encrypted_content[content],content_password[password_index],False)) # decrypt text using the encrypt_decrypt function
            if new_decrypted_message[-3:]in actual_message: # if last 3 of the decrypted_content is in actual_message list add into decrypted_message list and break the inner loop
                decrypted_message.append(new_decrypted_message) 
                break
            else: 
                pass

    return decrypted_message

#add any other Task 2 helper functions here

############## EXPELLINUMBERS EASY MODE ##############

def expellinumbers(decrypted_message:list):
    '''expellinumbers game that takes in a list of decrpted message containing 
    several lines of expression, player will be asked to answer each expression 
    and will receive scores according to their answers.
    decrypted_message: list of decrypted message
    no return value
    '''
    round_index = 1
    survived = True
    previous_round_percentage = 0 #the percentage score of previous round, varies every round

    while round_index <= len(decrypted_message) and survived: #loop thru every row in decrypted message if survived
        print(f"\n✩₊˚.⋆☾⋆⁺₊✧ Round {round_index}:")
        expression = decrypted_message[round_index-1].split(';') #turn the current row into list of every expression
        score = 0 #player's score
        total_score = 0 #total score of the round

        for each_expression in expression: #loop thru every expression in the row
            total_score += 2
            correct_answer = eval(each_expression)
            
            try:#try to turn the input into math expressions
                answer = float(input(f"What is {each_expression}? "))
                if answer == correct_answer:
                    score += 2
                    print("Correct! Score: +2\n")
                elif correct_answer * 0.8 <= answer <= correct_answer * 1.2 and correct_answer+2 != 0: #if answer is in the 20% correctness margin (inclusive)
                    score += 1
                    print("Oopsie, nearly there! Score: +1\n")
                else:
                    print("Wrong!\n")
            except:#if user input is non-numerical(letters, symbols or blank)
                print("Wrong!\n")
        accuracy = score/total_score
        print(f"You've received {score} out of {total_score}. That's {accuracy * 100:.0f}%!")

        if len(decrypted_message) == 1:# if there is only one row in the decrypted message
            print("There is only one round!")
        elif accuracy >= 0.8 or accuracy >= previous_round_percentage: #if the accuracy is above 80% or exceed previous round accuracy
            if round_index == len(decrypted_message):
                print("Brilliant! You've made it to the last round!")
            else:
                print("You've conjured well! On to the next round!")
                previous_round_percentage = accuracy
        else:
            survived = False
            print("Alas, your spellcasting failed to keep you alive."
                  "\nYou need to either exceed the previous round's percentage or receive a minimum of 80% to continue!"
                  f"\nYou have survived {round_index - 1} round{"s"if round_index - 1 > 1 else ""}!")
        round_index += 1

#add any other Task 3 helper functions here

############## EXPELLINUMBERS WITH CURSES #############

#uncomment if completing task 4
import curses 
import threading
import time

def get_user_input(stdscr)->float or None:
    """
    Capture numerical input until Enter is pressed
    or after 5s. Returns the input as a float or None if invalid.
    """
    input_value = []
    stdscr.nodelay(True) 

    def timer():# cound down from 5s
        time.sleep(5)

    timer_thread = threading.Thread(target=timer)
    timer_thread.start()#start timer thread

    while True: #keep looping until user interupt or timeup or user press enter

        if not timer_thread.is_alive():#if not timeup
            print("Time up!")
            return None

        try:
            ch = stdscr.getch()
            if ch == -1:  # No input yet
                continue
            elif ch in (10, 13):  # Enter key pressed
                break
            elif ch == 127:  # Handle backspace
                if input_value:
                    input_value.pop()
                    print("\b \b", end='', flush=True)  # Erase character
            elif ch in range(48, 58):  # Digits 0-9
                input_value.append(chr(ch))
                print(chr(ch), end='', flush=True)
            elif ch == ord('-') and len(input_value) == 0:  # Allow '-' at start
                input_value.append('-')
                print('-', end='', flush=True)

        except KeyboardInterrupt:#user interrupt
            break

    result = ''.join(input_value).strip()
    try:#try to turn result to float
        return float(result) if result else None
    except ValueError:
        return None

def expellinumbers_with_curses(stdscr, decrypted_message):
    '''
    hard mode, expllinumbers game with curses, for each expression
    player has 5s to answer, everything else is the same as simple mode
    decrypted_message: list of decrypted message
    no return value
    '''
    round_index = 1
    survived = True
    previous_round_percentage = 0  # The percentage score of the previous round

    while round_index <= len(decrypted_message) and survived:#while game not over
        print(f"\n✩₊˚.⋆☾⋆⁺₊✧ Round {round_index}:")
        expression = decrypted_message[round_index - 1].split(';')
        score = 0
        total_score = 0

        for each_expression in expression:#loop thru each row
            total_score += 2
            correct_answer = eval(each_expression)
            print(f"\nWhat is {each_expression}? (You have 5 seconds to answer): ", end='', flush=True)

            answer = get_user_input(stdscr)

            if answer is None:
                print("Incorrect: Time's up or invalid input.")
            elif answer == correct_answer:
                score += 2
                print(" Correct! Score: +2")
            elif correct_answer * 0.8 <= answer <= correct_answer * 1.2:
                score += 1
                print(" Oopsie, nearly there! Score: +1")
            else:
                print("Wrong!")

        accuracy = score / total_score
        print(f"\nYou've received {score} out of {total_score}. That's {accuracy * 100:.0f}%!")

        if len(decrypted_message) == 1:
            print("\nThere is only one round!")
        elif accuracy >= 0.8 or accuracy >= previous_round_percentage:
            if round_index == len(decrypted_message):
                print("\nBrilliant! You've made it to the last round!")
            else:
                print("\nYou've conjured well! On to the next round!")
                previous_round_percentage = accuracy
        else:
            survived = False
            print("\nAlas, your spellcasting failed to keep you alive.")
            print("You need to either exceed the previous round's percentage or receive a minimum of 80% to continue!")
            print(f"You have survived {round_index - 1} round{'s' if round_index - 1 > 1 else ''}!")

        round_index += 1

#add any other Task 4 helper functions here

########MAIN GAME FUNCTION#########

def main():
    print("WELCOME TO EXPELLINUMBERS: CONFUSING CALCULATIONS!")
    print("\nGAME SETUP...")
    print('''No. File Name
[1] encrypted_message1.txt
[2] encrypted_message2.txt
[3] encrypted_message3.txt
[4] encrypted_message4.txt''')
    choice=input("\nSelect an encrypted_message file: ")

    chosen_encrypted_file = ""
    chosen_password_file = ""
    if choice == "1":
        chosen_encrypted_file="encrypted_message1.txt"
        chosen_password_file="passwords1.txt"
    elif choice == "2":
        chosen_encrypted_file="encrypted_message2.txt"
        chosen_password_file="passwords2.txt"
    elif choice == "3":
        chosen_encrypted_file="encrypted_message3.txt"
        chosen_password_file="passwords3.txt"
    elif choice == "4":
        chosen_encrypted_file="encrypted_message4.txt"
        chosen_password_file="passwords4.txt"
    puzzle=decrypt_file(chosen_encrypted_file,chosen_password_file)

    difficulty = input("\nSelect [1] expellinumbers or [2] expellinumbers with curses: ")
    print("\nGAME STARTS...")
    
    if difficulty== "1":
        expellinumbers(puzzle)
    elif difficulty=="2":
        curses.wrapper(expellinumbers_with_curses, puzzle)


    


if __name__ == "__main__":
    main()
