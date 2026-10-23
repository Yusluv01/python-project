#string manipulation
#Ask the user to input a sentence and
#convert it to uppercase using upper()
#convert it to lowercase using lower()
#count the number of words (split by spaces)
#Build a perlindroma checker weight converter(split with kg then strip without kg)



print("welcome yusluv")


sentence=input("enter the sentence>>>")
print(sentence.upper())
print(sentence.lower())
print(sentence.strip())
print(sentence.count(""))

#palindrome checker
#A palindrome checker is a program or function that determines whether a given input (typically a string or number) reads the same forward and backward. 
def is_palindrome(s):
    return s == s[::-1]

input_name= input("Entee your name : ")

if is_palindrome(input_name ):
    print("Palindrome")
else:
    print("Not a palindrome")


# build a quiz application

ques=('what is the capital of nigeria','what is your name','spell ball')
for question in ques:
    user_ansa=input('enter your name>>')
    if user_ansa=="abuja":
        print('correct')
    print+=()

# Define the questions and answers
questions = [
    

    ]

# Function to display the quiz and get the score
def run_quiz():
    score = 0

    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for idx, option in enumerate(q['options']):
            print(f"{idx + 1}. {option}")
        
        answer = input("Your answer (1-4): ")
        if q['options'][int(answer) - 1] == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {q['answer']}\n")
    
    print(f"Your final score is: {score} out of {len(questions)}")

# Start the quiz
if __name__ == "__main__":
    print("Welcome to the Quiz Application!")
    print("----------------------------")
    run_quiz()






