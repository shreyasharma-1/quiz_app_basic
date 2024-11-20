import random
import os

#To clear the above terminal
def clear_terminal():
    """Clears the terminal screen based on the operating system."""
    if os.name == 'nt':  # For Windows
        os.system('cls')

# Questions:
questions_python = [
    ("What is the correct file extension for Python files?", [".py", ".java", ".cpp", ".txt"], "1"),
    ("How do you create a variable with the numeric value 5?", ["x = 5", "int x = 5", "x <- 5", "let x = 5"], "1"),
    ("Which keyword is used to define a function in Python?", ["func", "define", "def", "function"], "3"),
    ("Which function is used to output data to the screen in Python?", ["print()", "output()", "echo()", "write()"], "1"),
    ("What keyword is used to start a conditional statement in Python?", ["if", "when", "cond", "switch"], "1"),
    ("What is the output of '2**3' in Python?", ["6", "9", "8", "7"], "3"),
    ("How do you add a comment in Python?", ["// This is a comment", "/* This is a comment */", "# This is a comment", "-- This is a comment"], "3"),
    ("What keyword is used to create a loop in Python?", ["for", "loop", "iterate", "foreach"], "1"),
    ("How do you start a while loop in Python?", ["while condition:", "while (condition)", "until (condition)", "loop while condition"], "1"),
    ("Which of the following data structures is immutable in Python?", ["list", "set", "tuple", "dictionary"], "3")
]

questions_java = [
    ("What is the file extension for Java files?", [".java", ".class", ".cpp", ".js"], "1"),
    ("Which keyword is used to define a class in Java?", ["class", "def", "function", "object"], "1"),
    ("How do you define a method in Java?", ["void methodName()", "def methodName()", "func methodName()", "function methodName()"], "1"),
    ("What is the main method signature in Java?", ["public static void main(String[] args)", "public void main(String[] args)", "static main(String args)", "public method main()"], "1"),
    ("What is used to output data in Java?", ["System.out.print()", "System.out.println()", "cout <<", "echo"], "2"),
    ("Which keyword is used to create an object in Java?", ["new", "create", "class", "object"], "1"),
    ("What is the size of an int in Java?", ["2 bytes", "4 bytes", "8 bytes", "16 bytes"], "2"),
    ("Which of these is a valid access modifier in Java?", ["public", "get", "static", "final"], "1"),
    ("How do you define a loop in Java?", ["for loop", "foreach loop", "loop while", "for iteration"], "1"),
    ("What keyword is used for inheritance in Java?", ["extends", "inherits", "implements", "derives"], "1")
]

questions_cpp = [
    ("What is the file extension for C++ files?", [".c", ".cpp", ".class", ".java"], "2"),
    ("Which operator is used for input in C++?", ["<<", ">>", "==", "++"], "2"),
    ("Which operator is used for output in C++?", ["<<", ">>", "++", "--"], "1"),
    ("Which keyword is used to define a class in C++?", ["class", "def", "function", "object"], "1"),
    ("What is the correct way to include a library in C++?", ["#include", "import", "using", "require"], "1"),
    ("What is the size of an int in C++?", ["2 bytes", "4 bytes", "8 bytes", "16 bytes"], "2"),
    ("What is the entry point for a C++ program?", ["main()", "start()", "init()", "entry()"], "1"),
    ("How do you start a while loop in C++?", ["while (condition)", "until (condition)", "loop while", "for (condition)"], "1"),
    ("What is used to handle exceptions in C++?", ["try/catch", "if/else", "switch/case", "throw/catch"], "1"),
    ("How do you declare a variable in C++?", ["int a;", "a = 0;", "var a;", "int[] a;"], "1")
]


def run_quiz(language, questions):
    """Runs the quiz for a specified language and set of questions."""
    score = 0  

    
    random.shuffle(questions)
    selected_questions = questions[:5]

    for i, (question, options, correct_answer) in enumerate(selected_questions):
        clear_terminal()  
        print(f"\nQ{i + 1}: {question}") 
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")  
        
        
        answer = input("Your answer (number or option): ").strip().lower()

        
        if answer == correct_answer or answer == options[int(correct_answer) - 1].lower():
            score += 1  
            print("Correct!")  
        else:
            print(f"Wrong! The correct answer is: {options[int(correct_answer) - 1]}")  

    print(f"\nYou scored {score} out of 5.") 


def checker_password(password):
    """Checks the validity of the password based on specific criteria."""

    # Check if the password length is between 8 and 12 characters
    if len(password) < 8 or len(password) > 12:
        print("Password must be between 8 and 12 characters.")
        return False
    
   
    special_character = ["@", "#", "$", "&", "!"]
    
    
    if not any(char in special_character for char in password):
        print("Password must have at least one special character.")
        return False
    
    
    if not any(char.isdigit() for char in password):
        print("Password must have at least one numeric digit.")
        return False
    
    
    if not any(char.isupper() for char in password):
        print("Password must have at least one uppercase letter.")
        return False
    
    return True  

def main():
    """Main function to run the quiz application."""
    print("WELCOME TO THE QUIZE GAME APPLICATION!")  

    username = input("Enter your username: ")  

    print("Password validation includes:\n- Length between 8 and 12 characters.\n- At least one special character (@, #, $, &, !).\n- At least one numeric digit.\n- At least one uppercase letter.")

    
    while True:
        password = input("Enter your password: ")
       
        if checker_password(password):
            print("Accepted")  
            break 
        else:
            print("Please try again.")  

    while True:
        clear_terminal()  
        print("\nChoose a language for the quiz:")  
        print("1/a. Python")
        print("2/b. Java")
        print("3/c. C++")

        choice = input("Enter the number of your choice: ") 

        
        if choice == '1' or choice.lower() == "python" or choice == "PYTHON" or choice == "Python" or choice == "a":
            print("\nYou have selected Python!")
            run_quiz("Python", questions_python)
        elif choice == '2' or choice.lower() == "java" or choice.upper() == "JAVA" or choice == "java" or choice == "b":
            print("\nYou have selected Java!")
            run_quiz("Java", questions_java)
        elif choice == '3' or choice.lower() == "c++" or choice == "C++" or choice == "c":
            print("\nYou have selected C++!")
            run_quiz("C++", questions_cpp)
        else:
            print("Invalid choice. Please select a valid option.")
            continue  # Prompt for choice again if invalid

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower() 
        if play_again != 'yes':
            print("Thank you for playing the Game! Goodbye.")  # Exit message
            break  # Exit the loop

if __name__ == "__main__":
    main()  # Start the application


