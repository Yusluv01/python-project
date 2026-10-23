# build a quiz application


# Define the question and answer
question = "What is the capital of France?"
correct_answer = "Paris"

# Ask the question
user_answer = input(f"{question} ")

# Check the answer
if user_answer.strip().lower() == correct_answer.lower():
    print("Correct!")
else:
    print(f"Incorrect! The correct answer is {correct_answer}.")


question = " What is my name?"
correct_answer = "Ayodeji"
user_answer = input(f"{question} ")
if user_answer.strip().lower() == correct_answer.lower():
    print("correct!")
else:
    print(f"incorrect! The correct answer is {correct_answer}. ")


question = " What is H2S04 called?"
correct_answer = "Hydrogen tetraoxo sulphate vi acid"
user_answer = input(f"{question} ")
if user_answer.strip().lower() == correct_answer.lower():
    print("correct!")
else:
    print(f"incorrect! The correct answer is {correct_answer}. ")


question = " What is the name of my bestie?"
correct_answer = "Roseline"
user_answer = input(f"{question} ")
if user_answer.strip().lower() == correct_answer.lower():
    print("correct!")
else:
    print(f"incorrect! The correct answer is {correct_answer}. ")

question = " Do you enjoy python class?"
correct_answer = "YES"
user_answer = input(f"{question} ")
if user_answer.strip().lower() == correct_answer.lower():
    print("correct!"'point+=5')
else:
    print(f"incorrect! The correct answer is {correct_answer}. ")



# Buid a to-do list application

def show_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"'{deleted_task}' has been removed from the to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()







