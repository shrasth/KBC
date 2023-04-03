#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Create a program capable of displaying questions to the user like KBC
# Use list data type to store the questions and their correct answers
# Display the final amount the person is taking home after playing the game


questions = [
    [
        "What is the maximum length of a Python identifier?", "32", "16", "128", "No fixed Length is specifed",
    ],
    
    [
        "How is a code block indicated in Python?", "Brackets","Indentation", "Key", "None of the above"
    ],
    
    [
        "Which of the following concepts is not a part of Python?","Pointers", "Loops", "Dynamic Typing", "All of the above"
    ],
    
    [
        "Who developed Python Programming Language?", "Wick van Rossum","Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"
    ],
    
    [
        "Which type of Programming does Python support?", "object-oriented programming","structured programming", "functional programming", "all of the mentioned"
    ],
    
    [
        "Is Python case sensitive when dealing with identifiers?","no", "yes", "machine dependent", "none of the mentioned"
    ],
    
    [
        "Which of the following is the correct extension of the Python file?",".python", ".pl", ".py", ".p"
    ],
    
    [
        "Is Python code compiled or interpreted?", "Python code is both compiled and interpreted","Python code is neither compiled nor interpreted", "Python code is only compiled", "Python code is only interpreted"
    ],
    
    [
        "Which of the following statements are used in Exception Handling in Python?","try", "except", "finally", "All of the above"
    ],
    
    [
        "Which of the following is used to define a block of code in Python language?","Indentation", "Key", "Brackets", "All of the mentioned"
    ],
    
    [
        "Which keyword is used for function in Python language?","Function", "def", "Fun", "Define"
    ],
    
    [
        "Which of the following character is used to give single-line comments in Python?","//", "#", "!", "/*"
    ],
    
    [
        "Which of the following functions can help us to find the version of python that we are currently working on?","sys.version(1)", "sys.version(0)", "sys.version()", "sys.version"
    ],
    
    [
        "Python supports the creation of anonymous functions at runtime, using a construct called __________","pi", "anonymous", "lambda", "none of the mentioned"
    ],
    
    [
        "What is the order of precedence in python?", "Exponential, Parentheses, Multiplication, Division, Addition, Subtraction", "Exponential, Parentheses, Division, Multiplication, Addition, Subtraction","Parentheses, Exponential, Multiplication, Division, Subtraction, Addition", "Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"
    ],
    
    [
        "What will be the output of the following Python code snippet if x=1? x<<2","4", "2", "1", "8"
    ],
    
    [
        "What does pip stand for python?", "Pip Installs Python","Pip Installs Packages", "Preferred Installer Program", "All of the mentioned"
    ],

]

answers = ["D","B","A","C","D","B","C","A","D","A","B","B","D","C","D","A","C"]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for {levels[i]}")
    print(f"{question[0]}")
    print(f"A. {question[1]}      B. {question[2]}   C. {question[3]}  D. {question[4]}")
    reply = input("Enter your response (A, B, C or D) or Q to quit: ").upper()
    if (reply == "Q"):
        money = levels[i-1]
        break
    if (reply == answers[i]):
        print(f"Correct answer, you have won {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 13):
            money = 7500000
        elif (i == 15):
            money = 75000000

    else:
        print("Wrong answer!")
        break

print(f"Thank you for playing.\nCongratulations, You have won ₹{money}")


# In[ ]:




