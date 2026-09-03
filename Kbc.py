import sys

#Questions

Q_1="What is the capital city of Australia?"
Q_2= "What is the chemical symbol for gold?"
Q_3="Who wrote the play Romeo and Juliet?"
Q_4="Which planet in our solar system is known as the Red Planet?"
Q_5="How many bones are in the adult human body?"
#Options
op_1=["A) Sydney","B) Melbourne","C) Canberra","D) Perth"]
op_2=["A) Ag","B) Au","C) Fe","D) Gd"]
op_3=["A) Charles Dickens","B) Jane Austen","C) Mark Twain","D) William Shakespeare"]
op_4=["A) Venus","B) Mars","C) Jupiter","D) Saturn"]
op_5=["A) 196","B) 206","C) 216","D) 226"]
#Answers
Answer_1="Canberra"
Answer_2="Au"
Answer_3="William Shakespeare"
Answer_4="Mars"
Answer_5="206"
#Questions and answers logic
print(Q_1)
print(op_1)
your_answer_1=input("\nEnter your answer: ")
if your_answer_1== Answer_1:
    print("correct answer,\nYou won 10$")
    print("Total won:10$")
    print(Q_2)
    print(op_2)
else:
    print("incorrect answer,\nYou lost 10$")
    sys.exit()
your_answer_2=input("\nEnter your answer: ")
if your_answer_2== Answer_2:
    print("correct answer,\nYou won 20$")
    print("Total won:30$")
    print(Q_3)
    print(op_3)
else:
    print("incorrect answer,\nYou lost 20$")
    sys.exit()
your_answer_3=input("\nEnter your answer: ")
if your_answer_3== Answer_3:
    print("correct answer,\nYou won 30$")
    print("Total won:60$")
    print(Q_4)
    print(op_4)
else:
    print("incorrect answer,\nYou lost 30$")
    sys.exit()
your_answer_4=input("\nEnter your answer: ")
if your_answer_4== Answer_4:
    print("correct answer,\nYou won 40$")
    print("Total won:100$")
    print(Q_5)
    print(op_5)
else:
    print("incorrect answer,\nYou lost 40$")
    sys.exit()
your_answer_5=input("\nEnter your answer: ")
if your_answer_5== Answer_5:
    print("correct answer,\nYou won 50$")
    print("Total won:150$")
else:
    print("incorrect answer,\nYou lost 50$")
    sys.exit()