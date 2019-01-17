import random
import sys
import math
import collections
import time

start = time.time()
def find_(value):
    if validator(value):
        for i in range(len(value)):
            if value[i] == "_":
                return i

    raise ValueError


def swap(value, first, last):
    tmp = value[first]
    value[first] = value[last]
    value[last] = tmp
    return value

def validator(value):
    if len(value) == 9 or not refactor(value).isalpha():
        return True
    return False

def correct_moves(value, steps):
    if validator(value):
        current_position = find_(value)
        step_list = []
        for i in range(len(steps)):
            if 0 <= steps[i] + current_position <= len(value)-1 and abs(current_position % 3 - (current_position + steps[i]) % 3) < 2:
                step_list.append(swap(value.copy(), current_position, current_position+steps[i]))
        return step_list
    raise ValueError


def refactor(lister):
    string = ""
    for element in lister:
        string += element
    return string


def defactor(stringer):
    output = []
    for element in stringer:
        output.append(element)
    return output


def counter(seq, user_value,template):
    sol = []
    current = template
    while current != user_value:
        sol.append(current)
        current = seq.get(refactor(current))
    return sol


def solution(user_value, template, steps):
    if validator(user_value):
        seq = {}
        seq[refactor(user_value)] = 1
        queue = [] # очередь
        queue.append(user_value)
        flag = False
        while not flag:
            if template in queue:
                break
            storage = queue.copy()
            if len(queue) != 0:
                queue.clear()
            for element in storage:
                for next_move in correct_moves(element, steps):
                    if not seq.get(refactor(next_move)):
                        seq[refactor(next_move)] = element
                        #seq.update(key = refactor(next_move),value = element)
                        queue.append(next_move)
        final = counter(seq, user_value, template)
        return final
    raise ValueError

if __name__ == "__main__":
    user_input = ['a', 'a', 'i',
                  'z', 'd', 'p',
                  'n', 'o', '_']

    template1 = ['d', 'i', 'a', 'p', 'a', 'z', 'o', 'n', '_']
    steps = [-3, -1, 1, 3]

    sol = solution(user_input, template1, steps)
    print(len(sol)-1, "steps need")
    for i in sol:
        print(i[:3],"\n", i[3:6],"\n",i[6:], "\n")
    print(user_input[:3], "\n", user_input[3:6], "\n", user_input[6:], "\n")

    print(time.time() - start)



