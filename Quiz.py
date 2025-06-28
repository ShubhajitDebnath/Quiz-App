QN = [{
    "ques": "Which is the longest river in the world?",
    "options": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
    "answer": "B"
  },
{
    "ques": "Who was the first President of independent India?",
    "options": ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Dr. Rajendra Prasad", "D. Sardar Vallabhbhai Patel"],
    "answer": "C"
  },
{
    "ques": "What is the capital of Australia?",
    "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"],
    "answer": "C"
  },
{
    "ques": "Which planet is known as the 'Red Planet'?",
    "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
    "answer": "B"
  },
{
    "ques": "In which year did India win its first Cricket World Cup?",
    "options": ["A. 1975", "B. 1983", "C. 1996", "D. 2007"],
    "answer": "B"
  },
{
    "ques": "Which gas do plants absorb from the atmosphere during photosynthesis?",
    "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
    "answer": "C"
  },
{
    "ques": "Who invented the light bulb?",
    "options": ["A. Nikola Tesla", "B. Thomas Edison", "C. Alexander Graham Bell", "D. Isaac Newton"],
    "answer": "B"
  },
{
    "ques": "What is the national animal of India?",
    "options": ["A. Elephant", "B. Peacock", "C. Lion", "D. Tiger"],
    "answer": "D"
  },
{
    "ques": "Which day is celebrated as World Environment Day?",
    "options": ["A. June 5", "B. April 22", "C. March 21", "D. July 11"],
    "answer": "A"
  },
{
    "ques": "Who is known as the 'Father of the Indian Constitution'?",
    "options": ["A. Jawaharlal Nehru", "B. B.R. Ambedkar", "C. Mahatma Gandhi", "D. Subhas Chandra Bose"],
    "answer": "B"
  }]

# QNs = QN["ques"]git init
global score
score = 0
global QNA
global opt
for question in QN:
    QNA= question["ques"]
    print(QNA, "\n")
    options = question["options"]
    for option in options:  
        opt= option
        print(opt)
    user_input = input("Enter your Answer: ").upper()
    if user_input in question["answer"]:
      print("Correct Answer!")
      score += 1
    else:
      print("Wrong Answer!")


print("your score is :",score)



























#try this is work but no complete
# while True:
#     print("Welcome to the Quiz App!","\n")

#     questions_1={
#         "ques":"Which is the longest river in the world?",
#         "options" : ["A. Amazon","B.Nile","C. Yangtze","D. Mississippi"],
#         "check": ["A","B","C","D"],
#         "answer":"B",
#     }
#     global score
#     score = 0


#     qna=questions_1["ques"]
#     opt=questions_1["options"]
#     for i in opt:
#      print(i)
#     user_input = input("Enter your Answer:").upper().strip()
#     if user_input in questions_1["answer"]:
#         print("correct Answer")
#         score += 1
#         #print(score)
#         break
#     else:
#         print("Wrong Answer!\n \n Please try again.")
        
# print("Your Score is:",score)












#second try but few works manuallly

# while True:
#     print(questions_1["ques"],"\n")
#     print(questions_1["options"],"\n")
#     user_input = input("Enter your Answer:").upper()
#     if user_input in questions_1["answer"]:
#         print(questions_1["check"])
#         print("Correct Answer!")
#         break
#     else:
#         print("Wrong Answer!")
        













#try Frist:


# while True:
#     print(questions_1["ques"])
#     for i ,values in questions_1["options"]:
        
#         print(values)
#     if user_input==questions_1["answer"]:
#         print("Correct Answer!")
#         break

