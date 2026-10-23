# CBT Test Application


# methods
# list_of_student[]
# print(list_of_student.index(('mayowa', 'hikmat', 'samuel', 'victor')))
# print(list_of_student.count((('mayowa', 'hikmat', 'victor', 'azeez'))))
# list_of_question=[]
# landing_page=print("""
#                         Welcome TO AYO-D
#                 select:
#                 1.to register
#                 2.to login
#         """)
# user_opt=input('option>>> ')
# if user_opt =='1':
#         for each_name in range(2):
#                 name=input('enter your name>>> ')
#                 username=input('input your username>>> ')
#                 pwd=input('enter youe password>>> ')
#                 list_of_question.extend((name, username, pwd))


# Admin questions and answers
# questions = [
#     {"question": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja", "Kano", "Port Harcourt"], "answer": "Abuja"},
#     {"question 2": "What is the largest state in Nigeria?", "options": ["Kano", "Lagos", "Niger", "Taraba"], "answer": "Niger"},
#     {'question 3':"What is my name?", "options": ["Yusuf", "Ayodeji", "Victor", "Sammy"], "answer": "Yusuf"},
#     {"question 4":"what is the atomic number for lithum?", "option": ["3", "8", "7", "2"]},
#     {"question 5":"who is the president of Nigeria", "option":["Muhammad Buhari", "Ibikunle Amosun", "Bola Ahmed Tinubu", "Yusuf Akinbode-Ajayi"], "answer":["Yusuf Akinbode-Ajayi"]}
# ]

# Student score
# score = 7

# Main program
# while True:
#     print("\nCBT Test Application")
#     print("1. Take Test")
#     print("2. View Questions")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         for i, question in enumerate(questions, 1):
#             print(f"\nQuestion {i}: {question['question']}")
#             for j, option in enumerate(question['options'], 1):
#                 print(f"{j}. {option}")
#             answer = input("Enter your answer (1/2/3/4): ")
#             if question['options'][int(answer) - 1] == question['answer']:
#                 score += 1
#         print(f"\nYour score is {score}/{len(questions)}")
#         score = 0 # Reset score for next test
#     elif choice == "2":
#         for i, question in enumerate(questions, 1):
#             print(f"\nQuestion {i}: {question['question']}")
#             for j, option in enumerate(question['options'], 1):
#                 print(f"{j}. {option}")
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice. Please try again.")


Student_register=[]
# questions={'question':['1.what is the capital of nigeria', 'how many state does Nigeria has',

# "option":['1. a, b, c, d']

        # ]}

questions={"1. what is the capital of nigeria? a)abuja b)lagos c)ibadan d)ogbomosho":'a',
        "2. how many state does Nigeria has? a)14 b)12 c)13 d)16":'c',
        "3. correct spelling of cat?  a)kat b)cat c)kkat d)cart":'c',
        "4. who is the mother of jesus? a)Hikmat b)opemipo c)ibunkun d)mary":'d'
        "5. full meaning of SQI? a)soft quest incoporated b)soft quest incoporating c)soft quest incoporated d)soft quest incoporal"'a',
        
        
        }

def landing_page():
                print("""Welcome to new era group of school 


select
        1.Login
        2.Register
        3.Exit

        """)
user_opt=input('enter option>>> ')
if user_opt == '1':
        login_page()
elif user_opt =="2":
        register_page()
        
        



def login_page():
        username=input('enter username>>> ')
pwd=input('enter password>>>')
if Student_register:
        print('login successful! \n kindly proceed to take the test')
else:
        print('You have to register first. pls go back and register')

        def register_page():
                num_of_student=int(input('how many student>>> '))
                for each_std in range(1, num_of_student+1):
                
                        fullname=input('enter fullname>>> ')
                username=input('enter username>>> ')
                pwd=input('enter password>>> ')
                Student_register.append({'fullname':fullname, 'username':username, 'psswd':pwd})
                # Student_register.update(list_student)
        print(Student_register)
        print('Registration completed\n select 1. login\n 2. exit')

        for each in Student_register:
                score=0
                studt_score={}
                student_name=each['fullname']
                print(f"Dear {student_name} kindly sit for your test")
                for ques, ansa in ques.items():
                        print(ques)
                        opt=input('enter your answer>>>> ')
                        if opt == ansa:
                                score+=5
                                studt_score[student_name]=score
                for each_name, std_result in studt_score.items():
                        username=input('enter username>>> ')
                        pwd=input('enter password>>> ')
                        print()
                        result_pass=any(each['username']==username and each ['psswd']==pwd for each in 
                        Student_register)
                        if result_pass:
                                print(f'\nDear {each_name}, you score is {std_result}')

                        while True:
                                landing_page()

                        




















