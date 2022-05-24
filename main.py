from string import printable
import time



solution_string = 'Hello World!'
answer_string = ''


for i in range(0,len(solution_string)):
    for j in printable:
        time.sleep(0.05)
        print(answer_string + j)
        if solution_string[i] == j:
            answer_string = answer_string + j
            break