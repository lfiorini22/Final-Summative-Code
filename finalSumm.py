# Welcome to my text-based game program!

# Below I have defined all parts of my code...

def ans():

    global ans_response 
    
    print("1. Yes")
    print("2. No")
    print("")
    print("Choose one of the options above after reading below")
    print ("--------------------------------------------------------------------------------------------------------------------")

    ans_response = int(input("Have you already read Jabari Jumps and are ready to continue?"))

    if ans_response == 1:   
        print ("Amazing! Let's head on to the game! However, before we start, just to make sure you are ready to play, let's do a practice question, just so you can get used to how the multiple choice system works")
        print ("----------------------------------------------------------------------------------------------------------------")
        tutorial1()

# If the user hasn't yet read Jabari Jumps, they are provided a link to a read aloud of Jabari Jumps to do so
    elif ans_response == 2:
        print ("Ok, no worries. Click this link here to watch a read aloud of Jabari Jumps: https://www.youtube.com/watch?v=RfpIivqO3ic&ab_channel=CultivatingProgress After that, you should be ready to go!")
        print ("----------------------------------------------------------------------------------------------------------------")     
        tutorial1()

# Else, if the user does not respond with either the #1 or 2, they will be informed that the choice is an invalid option and be brought back to the main menu with the question again  
    else: 
        print("Sorry, this is an invalid choice")
        print("--------------------------------------------------------------------------------------------------------------------")
        tutorial1()


print("--------------------------------------------------------------------------------------------------------------------")

# Lines like this seperate pieces of different code from each other, allowing for the user's to more easily digest the information in a more organized manner


def tutorial1():

    global tutorial_response 

    print("Question #1: If Carl has 35 marbles, but then gives 22 to his friend Joe so he can play as well, how many is Carl left with?")

    print("")
    print("1. 24 marbles")
    print("2. 12 marbles")
    print("3. 13 marbles")
    print("4. 18 marbles")
    print ("--------------------------------------------------------------------------------------------------------------------")

    tutorial_response = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))

    if tutorial_response == 1:
        print("Please Try Again")
        print("")
        tutorial1()

    elif tutorial_response == 2:
        print ("Close! Please Try Again")
        print ("----------------------------------------------------------------------------------------------------------------")
        print ("")
        tutorial1()
 
  
    elif tutorial_response == 3:
        print("Amazing!")
        print("")
        print("Now we will move on to the beginning of the game, starting with the 1st actual question. There will be 4 questions tested on each difficulty; easy, medium or hard. First, you will choose which difficulty you would like to play the game in.")
        print ("----------------------------------------------------------------------------------------------------------------")
        print("")
        difficulty_of_game()

    elif tutorial_response == 4:
        print ("Great attempt! Please Try Again")
        print ("----------------------------------------------------------------------------------------------------------------")
        print ("")
        tutorial1()
        
    
    else:
        print("This is not a valid choice, please try again")
        print ("----------------------------------------------------------------------------------------------------------------")
        print("")
        tutorial1()

def difficulty_of_game():

    global difficulty_response 

# Once, or if users have already read Jabari Jumps, they are given a random math question to ensure theyt understand how multiple choice questions function   
    print ("Of the 3 following game-mode difficulties, which would you like to play the video game in?")
    
    print("")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print ("--------------------------------------------------------------------------------------------------------------------")

    difficulty_response = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))

    if difficulty_response == 1:
        print("Amazing, let's head onto the first question!")
        print("")
        question_1()
    

    elif difficulty_response == 2:
        print ("Wow, get ready for a great challenge!")
        print ("----------------------------------------------------------------------------------------------------------------")
        print ("")
        question_5()
 
  
    elif difficulty_response == 3:
        print("Very impressive! Good luck!")
        print("----------------------------------------------------------------------------------------------------------------")
        print("")
        question_9()
    
    else:
        print("This is not a valid choice, please try again")
        print ("----------------------------------------------------------------------------------------------------------------")
        print("")
        difficulty_of_game()


# PLEASE REFERENCE TO QUESTION #1 as a demonstration of the specific implications each part of code in the rest of my question contain 

def question_1():

# This defines "question_1", and the following information is the basis of what make up question #1 in my program

    global response1 

# A global command like this allows the terms "response_1" to be visible to the rest of the code, and thus, is important for the code to run properly as the variable is used continously

# Users are brought to their first question in the easy difficulty mode

    print("Here is the first question of the easy difficulty mode, good luck!")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("")

    print("Question #1: Who are the three main characters in Jabari Jumps?")

    print("")
    print("1. Jabari, his parents, and his sisters")
    print("2. Jabari, his friends, and his dad")
    print("3. Jabari, his dad, and his sister")
    print("4. Jabari, his cousins and his dad.")
    print("")

    response1 = int(input("Please Type 1, 2, 3, or 4 to select one of the options below"))

    print("--------------------------------------------------------------------------------------------------------------------")

    if response1 == 1:
        print("Please Try Again")
        print("--------------------------------------------------------------------------------------------------------------------")
        print("")
        question_1()
# If the user incorrectly answers the question, they will be re-asked the question

    if response1 == 2:
        print("Please Try Again")
        print( "--------------------------------------------------------------------------------------------------------------------")
        print("")
        question_1()
 # If the user incorrectly answers the question, they will be re-asked the question


    if response1 == 3:
        print("Great Job!")
        print("")
        print( "--------------------------------------------------------------------------------------------------------------------")
        print("Now we will move on to question number 2!")
        print("")
# Calling question #2 here, as the user correctly answered the question, and is able to move on
        question2()

    if response1 == 4:
        print("Please Try Again")
        print( "--------------------------------------------------------------------------------------------------------------------")
        print("")
        question_1()
# If the user incorrectly answers the question, they will be re-asked the question 

    else:
        print("This is not a valid choice, please try again")
        print( "--------------------------------------------------------------------------------------------------------------------")
        print("")
        question_1()
# If the user does not respond with a valid answer (#1, 2, 3 or 4), they will be re-directed to the question


def question2():

    global response2
   
    print ("Question #2: Where is the setting of Jabari Jumps?")
    print ("\u001b[33m Question #2: What is the setting of Jabari Jumps?\u001b[0m")

    print("")
    print("1. Pool")
    print("2. Park")
    print("3. Museum")
    print("4. Zoo")
    print("")

    response2 = int(input("Please Type 1, 2, 3, or 4 to select one of the options below"))

    print("--------------------------------------------------------------------------------------------------------------------")

    if response2 == 1:
        print("Great Job!")
        print("--------------------------------------------------------------------------------------------------------------------")
        print("")
        print("Now we will move on to question number 3!")
        print("")
        question_3()
       

    elif response2 == 1:
        print("Please Try Again")
        print("--------------------------------------------------------------------------------------------------------------------")
        print("")
        question2()
  
    elif response2 == 3:
        print ("Please Try Again")
        print("--------------------------------------------------------------------------------------------------------------------")
        print ("")
        question2()
   
    elif response2 == 4:
        print ("Please Try Again")
        print ("")
        question2()
   
    else:
        print("This is not a valid choice, please try again")
        print("--------------------------------------------------------------------------------------------------------------------")
        print("")
        question2()

def question_3():

    global response3
  
    print ("Question #3: What did Jabari tell his dad he was going to do?")
    print("--------------------------------------------------------------------------------------------------------------------")

    print("")
    print("1. Swim in the pool")
    print("2. Relax on the pool deck ")
    print("3. Ride his bike")
    print("4. Jump off the diving board")
    print("")

    response3 = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")
  
    if response3 == 1:
        print("Please Try Again")
        print("")
        question_3()
   
  
    elif response3 == 2:
        print ("Please Try Again")
        print ("")
        question_3()
  
  
    elif response3 == 3:
        print ("Please Try Again")
        print ("")
        question_3()

    elif response3 == 4:
        print("Amazing work!")
        print("Now we will move on to the final question, question #4!")
        print("")
        question4()
   
    else:
        print("This is not a valid choice, please try again")
        print("")
        question_3()

def question4():

    global response4
  
    print ("Question #4: What does Jabari say right before he jumps off the diving board?")
    print ("--------------------------------------------------------------------------------------------------------------------")

    print("")
    print("1. I do not like surprises")
    print("2. I love surprises")
    print("3. What time is it?")
    print("4. This pool is very deep")
    print("")
  
    response4 = int(input("Please Type 1, 2, 3 or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")

    if response4 == 1:
        print("Please Try Again")
        print("")
        question4()
   
  
    elif response4 == 2:
        print("Great Job!")
        print("")
        print('''
░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗██╗░░░██╗██╗░░░░░░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗░░░
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝░░░
██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░██║░░░██║██║░░░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░░░░
██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗██╗
╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝╚█║
░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░░╚╝

██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░██╗░█████╗░██╗░░░██╗███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░██║██╔══██╗██║░░░██║██╔════╝
░╚████╔╝░██║░░██║██║░░░██║  ███████║███████║╚██╗░██╔╝█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══██║██╔══██║░╚████╔╝░██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░██║██║░░██║░░╚██╔╝░░███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝

░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗░██████╗███████╗██╗░░░██╗██╗░░░░░██╗░░░░░██╗░░░██╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██║░░░██║██║░░░░░██║░░░░░╚██╗░██╔╝
╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░█████╗░░██║░░░██║██║░░░░░██║░░░░░░╚████╔╝░
░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██║░░░██║██║░░░░░██║░░░░░░░╚██╔╝░░
██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝██║░░░░░╚██████╔╝███████╗███████╗░░░██║░░░
╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░

░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗██████╗░  ████████╗██╗░░██╗███████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝██╔══██╗  ╚══██╔══╝██║░░██║██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░██║░░██║  ░░░██║░░░███████║█████╗░░
██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░██║░░██║  ░░░██║░░░██╔══██║██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗██████╔╝  ░░░██║░░░██║░░██║███████╗
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

███████╗░█████╗░░██████╗██╗░░░██╗  ███╗░░░███╗░█████╗░██████╗░███████╗  ░█████╗░███████╗  ███╗░░░███╗██╗░░░██╗
██╔════╝██╔══██╗██╔════╝╚██╗░██╔╝  ████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔════╝  ████╗░████║╚██╗░██╔╝
█████╗░░███████║╚█████╗░░╚████╔╝░  ██╔████╔██║██║░░██║██║░░██║█████╗░░  ██║░░██║█████╗░░  ██╔████╔██║░╚████╔╝░
██╔══╝░░██╔══██║░╚═══██╗░░╚██╔╝░░  ██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░  ██║░░██║██╔══╝░░  ██║╚██╔╝██║░░╚██╔╝░░
███████╗██║░░██║██████╔╝░░░██║░░░  ██║░╚═╝░██║╚█████╔╝██████╔╝███████╗  ╚█████╔╝██║░░░░░  ██║░╚═╝░██║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░  ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝  ░╚════╝░╚═╝░░░░░  ╚═╝░░░░░╚═╝░░░╚═╝░░░

░██████╗░░█████╗░███╗░░░███╗███████╗██╗
██╔════╝░██╔══██╗████╗░████║██╔════╝██║
██║░░██╗░███████║██╔████╔██║█████╗░░██║
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░╚═╝
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝''')
        print("")
        print("Congratulations on a job well done! You have now completed the game and may exit, however, if you would like to continue to play, choose your new difficulty mode down below:")
        print ("--------------------------------------------------------------------------------------------------------------------")
        difficulty_of_game()
 # The user has now officially completed the easy difficulty version of my text-based video game!     
  
    elif response4 == 3:
        print ("Please Try Again")
        print ("")
        question4()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question4()

def question_5():

    global response5 
  
# Users are brought to their first question in the medium difficulty mode, "question_5"
 
    print ("Here is the first question of the medium difficulty mode, good luck!")
    print("--------------------------------------------------------------------------------------------------------------------")

    print ("Question #5: How did Jabari’s dad help him feel better about jumping off the diving board?")
    print ("\u001b[33m Question #5: How did Jabari’s dad help him feel better about jumping off the diving board?\u001b[0m")

    print("")
    print("1. He told him he did not have to jump")
    print("2. He told them that they were going to head home")
    print("3. He pushed him off the board and jumped with him")
    print("4  He told him to take a deep breath and tell himself he is ready.")
    print("")
  
    response1 = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")

    if response1 == 1:
        print("Please Try Again")
        print("")
        question_5()
   
  
    elif response1 == 2:
        print ("Please Try Again")
        print ("")
        question_5()

    elif response1 == 3:
        print ("Please Try Again")
        print ("")
        question_5()

    elif response1 == 4:
        print("Great Job!")
        print("")  
        question6()
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question_5()

def question6():

    global response6
  
    print ("Question #6: Why did Jabari climb up the ladder and then climb back down?")
    print("--------------------------------------------------------------------------------------------------------------------")

    print("")
    print("1. The lifeguard closed the pool")
    print("2. He told his dad he was a little tired and needed to rest")
    print("3. It began pouring")
    print("4. Jabari decided he was not ready to jump today.")
    print("")
  
    response6 = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")

    if response6 == 1:
        print("Please Try Again")
        print("")
        question6()
   
  
    elif response6 == 2:
        print("Great Job!")
        print("")
        question_7()
      
  
    elif response6 == 3:
        print ("Please Try Again")
        print ("")
        question6()
   
    else:
        print("This is not a valid choice, please try again")
        print("")
        question6()

def question_7():

    global response7 
  
    print("Question #7: How did Jabari feel after he jumped off the diving board?")
    print("--------------------------------------------------------------------------------------------------------------------")

    print("")
    print("1. He was excited and happy that he had jumped")
    print("2. He felt sad it was all over")
    print("3. He was still scared")
    print("4. He felt mad that his dad had made him jump")
    print("")
  
    response7 = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")

    if response7 == 1:
        print("Great Job!")
        print("")
        print("Now we will move on to the final question, question #8!")
        print("")
        question8()

    if response7 == 2:
        print("Please Try Again")
        print("")
        question_7()

  
    elif response7 == 3:
        print ("Please Try Again")
        print ("")
        question_7()

    if response7 == 4:
        print("Please Try Again")
        print("")
        question_7()
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question_7()

def question8():

    global response8 
  
    print ("Question #8: Why did Jabari think he was ready to jump off the diving board?")
    print ("\u001b[33m Question #8: Why did Jabari think he was ready to jump off the diving board?\u001b[0m")
    print("--------------------------------------------------------------------------------------------------------------------")

    print("")
    print("1. He finished all his swimming lessons")
    print("2. He passed his swimming test")
    print("3. He felt confident and ready to jump")
    print("4. All of the above")
    print("")
  
    response8 = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")

    if response8 == 1:
        print ("Please Try Again")
        print("")
        question8()

    elif response8 == 2:
        print ("Please Try Again")
        print ("")
        question8()

    elif response8 == 3:
        print ("Please Try Again")
        print ("")
        question8()

    elif response8 == 4:
        print("Great Job!")
        print("Congratulations on a job well done! You have now completed the game and may exit, however, if you would like to continue to play, choose your new difficulty mode down below")
        print('''
░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗██╗░░░██╗██╗░░░░░░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗░░░
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝░░░
██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░██║░░░██║██║░░░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░░░░
██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗██╗
╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝╚█║
░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░░╚╝

██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░██╗░█████╗░██╗░░░██╗███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░██║██╔══██╗██║░░░██║██╔════╝
░╚████╔╝░██║░░██║██║░░░██║  ███████║███████║╚██╗░██╔╝█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══██║██╔══██║░╚████╔╝░██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░██║██║░░██║░░╚██╔╝░░███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝

░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗░██████╗███████╗██╗░░░██╗██╗░░░░░██╗░░░░░██╗░░░██╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██║░░░██║██║░░░░░██║░░░░░╚██╗░██╔╝
╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░█████╗░░██║░░░██║██║░░░░░██║░░░░░░╚████╔╝░
░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██║░░░██║██║░░░░░██║░░░░░░░╚██╔╝░░
██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝██║░░░░░╚██████╔╝███████╗███████╗░░░██║░░░
╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░

░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗██████╗░  ████████╗██╗░░██╗███████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝██╔══██╗  ╚══██╔══╝██║░░██║██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░██║░░██║  ░░░██║░░░███████║█████╗░░
██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░██║░░██║  ░░░██║░░░██╔══██║██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗██████╔╝  ░░░██║░░░██║░░██║███████╗
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

███╗░░░███╗███████╗██████╗░██╗██╗░░░██╗███╗░░░███╗  ███╗░░░███╗░█████╗░██████╗░███████╗  ░█████╗░███████╗
████╗░████║██╔════╝██╔══██╗██║██║░░░██║████╗░████║  ████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔════╝
██╔████╔██║█████╗░░██║░░██║██║██║░░░██║██╔████╔██║  ██╔████╔██║██║░░██║██║░░██║█████╗░░  ██║░░██║█████╗░░
██║╚██╔╝██║██╔══╝░░██║░░██║██║██║░░░██║██║╚██╔╝██║  ██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░  ██║░░██║██╔══╝░░
██║░╚═╝░██║███████╗██████╔╝██║╚██████╔╝██║░╚═╝░██║  ██║░╚═╝░██║╚█████╔╝██████╔╝███████╗  ╚█████╔╝██║░░░░░
╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░╚═════╝░╚═╝░░░░░╚═╝  ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝  ░╚════╝░╚═╝░░░░░

███╗░░░███╗██╗░░░██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗██╗
████╗░████║╚██╗░██╔╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝██║
██╔████╔██║░╚████╔╝░  ██║░░██╗░███████║██╔████╔██║█████╗░░██║
██║╚██╔╝██║░░╚██╔╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░╚═╝
██║░╚═╝░██║░░░██║░░░  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██╗
╚═╝░░░░░╚═╝░░░╚═╝░░░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝''')
        print("")
        print("--------------------------------------------------------------------------------------------------------------------")
        difficulty_of_game()
# The user has now officially completed the medium difficulty version of my text-based video game!
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question8()

def question_9():

    global response9
  
# Users are brought to their first question in the hard difficulty mode, question_9!

    print ("Here is the first question of the hard difficulty mode, good luck!")
    print("--------------------------------------------------------------------------------------------------------------------")

    print ("Question #9: What did Jabari tell his dad after he jumped off the diving board?")
    print ("\u001b[33m Question #9: What did Jabari tell his dad after he jumped off the diving board?\u001b[0m")
    print("--------------------------------------------------------------------------------------------------------------------")

    print("")
    print("1. Surprise double backflip is next!")
    print("2. I don’t want to do that again!")
    print("3. That was amazing!")
    print("4. I want to go home!")
    print("")
  
    response9 = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")

    if response9 == 1:
        print("Great Job!")
        print("Now we will move on to question number 3!")
        print("")
        question10()
        

    if response9 == 2:
        print("Please Try Again")
        print("")
        question_9()
   
  
    elif response9 == 3:
        print ("Please Try Again")
        print ("")
        question_9()


    elif response9 == 4:
        print ("Please Try Again")
        print ("")
        question_9()

   
    else:
        print("This is not a valid choice, please try again")
        print("")
        question_9()

def question10():

    global response10 
  
    print ("Question #10: Why did Jabari let the other kids go ahead of him when he was in line to get on the diving board?")
    print("--------------------------------------------------------------------------------------------------------------------")

    print("")
    print("1. Jabari liked the kids, so he let them go first")
    print("2. Jabari had good manners")
    print("3. Jabari needed to think about his special kind of jump.")
    print("4. Jabari wanted to see what the kids were going to do.")
    print("")
  
    response10 = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")

    if response10 == 1:
        print("Please Try Again")
        print("")
        question10()

    elif response10 == 2:
        print ("Please Try Again")
        print ("")
        question10()
   
  
    elif response10 == 3:
        print("Great Job!")
        print("")
        question_11()
   
    else:
        print("This is not a valid choice, please try again")
        print("")
        question10()

def question_11():

    global response11
  
    print ("Question #11: When Jabari got to the bottom of the ladder, what did he say he forgot to do?")
    print ("\u001b[33m Question #11: When Jabari got to the bottom of the ladder, what did he say he forgot to do?\u001b[0m")
    print("--------------------------------------------------------------------------------------------------------------------")

    print("")
    print("1. I forgot my goggles!")
    print("2. I forgot to do my stretches!")
    print("3. I forgot to sing my favourite song!")
    print("4. I forgot to go run!")
    print("")
  
    response11 = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")

    if response11 == 1:
        print("Please Try Again")
        print("")
        question_11()
   
  
    elif response11 == 2:
        print("Great Job!")
        print("")
        print("Now we will move on to the final question, question #12!")
        print("")
        question12()

  
    elif response11 == 3:
        print ("Please Try Again")
        print ("")
        question_11()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question_11()

def question12():

    global response12
  
    print ("Question #12: What did Jabari do just before he was about to jump off the diving board?")
    print("--------------------------------------------------------------------------------------------------------------------")

    print("")
    print("1. He took a deep breath and spread his arms and bent his knees")
    print("2. He took a deep breath and jumped right away")
    print("3. He took a deep breath and spread his arms and kept his knees straight up")
    print("4. None of the above")
    print("")
  
    response12 = int(input("Please Type 1, 2, 3, or 4 to select one of the options"))
    print("--------------------------------------------------------------------------------------------------------------------")
  
    if response12 == 1:
        print("Great Job! Congratulations on successfully completing the hard mode of my game, fanatastic work!")
        print('''
░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗██╗░░░██╗██╗░░░░░░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗░░░
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝░░░
██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░██║░░░██║██║░░░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░░░░
██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗██╗
╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝╚█║
░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░░╚╝

██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░██╗░█████╗░██╗░░░██╗███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░██║██╔══██╗██║░░░██║██╔════╝
░╚████╔╝░██║░░██║██║░░░██║  ███████║███████║╚██╗░██╔╝█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══██║██╔══██║░╚████╔╝░██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░██║██║░░██║░░╚██╔╝░░███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝

░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗░██████╗███████╗██╗░░░██╗██╗░░░░░██╗░░░░░██╗░░░██╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██║░░░██║██║░░░░░██║░░░░░╚██╗░██╔╝
╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░█████╗░░██║░░░██║██║░░░░░██║░░░░░░╚████╔╝░
░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██║░░░██║██║░░░░░██║░░░░░░░╚██╔╝░░
██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝██║░░░░░╚██████╔╝███████╗███████╗░░░██║░░░
╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░

░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗██████╗░  ████████╗██╗░░██╗███████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝██╔══██╗  ╚══██╔══╝██║░░██║██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░██║░░██║  ░░░██║░░░███████║█████╗░░
██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░██║░░██║  ░░░██║░░░██╔══██║██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗██████╔╝  ░░░██║░░░██║░░██║███████╗
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

██╗░░██╗░█████╗░██████╗░██████╗░  ███╗░░░███╗░█████╗░██████╗░███████╗  ░█████╗░███████╗  ███╗░░░███╗██╗░░░██╗
██║░░██║██╔══██╗██╔══██╗██╔══██╗  ████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔════╝  ████╗░████║╚██╗░██╔╝
███████║███████║██████╔╝██║░░██║  ██╔████╔██║██║░░██║██║░░██║█████╗░░  ██║░░██║█████╗░░  ██╔████╔██║░╚████╔╝░
██╔══██║██╔══██║██╔══██╗██║░░██║  ██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░  ██║░░██║██╔══╝░░  ██║╚██╔╝██║░░╚██╔╝░░
██║░░██║██║░░██║██║░░██║██████╔╝  ██║░╚═╝░██║╚█████╔╝██████╔╝███████╗  ╚█████╔╝██║░░░░░  ██║░╚═╝░██║░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝  ░╚════╝░╚═╝░░░░░  ╚═╝░░░░░╚═╝░░░╚═╝░░░

░██████╗░░█████╗░███╗░░░███╗███████╗██╗
██╔════╝░██╔══██╗████╗░████║██╔════╝██║
██║░░██╗░███████║██╔████╔██║█████╗░░██║
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░╚═╝
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝''')
        print("")
        print("--------------------------------------------------------------------------------------------------------------------")
        difficulty_of_game()
# The user has now officially completed the hard difficulty version of my text-based video game!


    if response12 == 2:
        print("Please Try Again")
        print("")
        question12()
  
    elif response12 == 3:
        print ("Please Try Again")
        print ("") 
        question12()  
   
    else:
        print("This is not a valid choice, please try again")
        print("")
        question12()

############################################################################################################################################

# The line above is a line seperating my definitions from the actual commencment of my game

# Here is a program on how to create my keyboard art
# I copy and pasted text from ASCII Keyboard Art website
# My link to this art is here: https://patorjk.com/software/taag/#p=display&f=Star%20Wars&t=Welcome%20to%20my%20%0Atext-based%20video%20%0Agame%20%0A%0A


Splash = """
____    __    ____  _______  __        ______   ______   .___  ___.  _______    .___________.  ______      .___  ___. ____    ____                              
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|   |           | /  __  \     |   \/   | \   \  /   /                              
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__      `---|  |----`|  |  |  |    |  \  /  |  \   \/   /                               
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|         |  |     |  |  |  |    |  |\/|  |   \_    _/                                
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____        |  |     |  `--'  |    |  |  |  |     |  |                                  
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|       |__|      \______/     |__|  |__|     |__|                                  
                                                                                                                                                                
.___________. __________   ___ .___________.      .______        ___           _______. _______  _______     ____    ____  __   _______   _______   ______      
|           ||   ____\  \ /  / |           |      |   _  \      /   \         /       ||   ____||       \    \   \  /   / |  | |       \ |   ____| /  __  \     
`---|  |----`|  |__   \  V  /  `---|  |----`______|  |_)  |    /  ^  \       |   (----`|  |__   |  .--.  |    \   \/   /  |  | |  .--.  ||  |__   |  |  |  |    
    |  |     |   __|   >   <       |  |    |______|   _  <    /  /_\  \       \   \    |   __|  |  |  |  |     \      /   |  | |  |  |  ||   __|  |  |  |  |    
    |  |     |  |____ /  .  \      |  |           |  |_)  |  /  _____  \  .----)   |   |  |____ |  '--'  |      \    /    |  | |  '--'  ||  |____ |  `--'  |    
    |__|     |_______/__/ \__\     |__|           |______/  /__/     \__\ |_______/    |_______||_______/        \__/     |__| |_______/ |_______| \______/     
                                                                                                                                                                
  _______      ___      .___  ___.  _______                                                                                                                     
 /  _____|    /   \     |   \/   | |   ____|                                                                                                                    
|  |  __     /  ^  \    |  \  /  | |  |__                                                                                                                       
|  | |_ |   /  /_\  \   |  |\/|  | |   __|                                                                                                                      
|  |__| |  /  _____  \  |  |  |  | |  |____                                                                                                                     
 \______| /__/     \__\ |__|  |__| |_______|                                                                                                                    
                                                                                                                                                                
                                                                                                                                                                                                                                                                     
"""
print (Splash)

# User's are first introduced to the "welcome page" of the game
# There are no specific rules within the game
print("Hello, welcome to my text-based game! Throughout the game, all questions will be asked in a multipe-choice style, meaning that you will be given multiple options of which you believe is the correct answer")
print("Although there are no specific rules for the game, please honestly answer the questions giving your best effort.")
print("--------------------------------------------------------------------------------------------------------------------")

# Now, I will call alll my definitions in its chronolgical order in my program, so that my program runs in the correct, intended order 
ans()
tutorial1()
difficulty_of_game()
question_1()
question2()
question_3()
question4()
question_5()
question6()
question_7()
question8()
question_9()
question10()
question_11()
question12()

input("When you have finished the game, please press ENTER to do so.")