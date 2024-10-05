import random as rdm
import time as t

OPERANDS = ["+" , "-" , "*"]
MIN_OPERAND = 3
MAX_OPERAND = 13
TOTAL_PROBLEMS = 10

def problem_genatation():
    right = rdm.randint(MIN_OPERAND, MAX_OPERAND)
    left  = rdm.randint(MIN_OPERAND, MAX_OPERAND)
    operator = rdm.choice(OPERANDS)

    expr = str(left) + " " + operator + " " + str(right)

    answer = eval(expr)
    return expr, answer

input("press enter to start")
print("---------------------------")
start_time = t.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = problem_genatation()
    while True:
        guess = input("problem #" + str(i+1) + ":" + " "+ expr + "=")
        if guess == str(answer):
            break

end_time = t.time()
total_time = round(end_time - start_time, 2)
print("---------------------------")
print("nice work, total time taken ", total_time,"seconds , avg:", total_time/TOTAL_PROBLEMS)