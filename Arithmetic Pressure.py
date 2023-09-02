# Created with assistance
# Importing libraries
import random
import time

# Variable setup
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

# Defining the 'generater', as well as pushing out random integers with a min output and max output
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
# Setting math problem
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start")
print("----------------------")

# Timer, to test the user on the amount of time taken
start_time = time.time()

# Shows problem in terminal
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work, you finished in", total_time, "seconds!")