import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_QUESTIONS = 10

def generate_questions():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

incorrect = 0
username = str(input("Hello user, please enter your name: "))
initiate = str(input(f"Greetings {username}, welcome to the Timed Math Questionnaire created by @hiiwilliamss!\n"
                     f"When you are ready, press 's'! To quit, type 'q'. ")).lower()
if initiate == "q":
    print(f"Thank you for playing, see you soon {username}!")
    quit()

start_time = time.time()

for i in range(TOTAL_QUESTIONS):
    expr, answer = generate_questions()
    while True:
        question = int(input(f"QUESTIONS #{i+1}: {expr} = "))
        if question == answer:
            print(f"Good job {username}!")
            break
        else:
            print(f"That is incorrect {username}, please try again!")
        incorrect = incorrect + 1

end_time = time.time()
total_time = end_time - start_time
print("-------------------------------------------------------------")
print(f"Total time: {total_time:.2f} seconds")