
### IMPORTS ###
import math


class DoMath:
    def __init__(self):
        pass

    def calculate(self, user_input):
        input_arr = user_input.split()

        data = None
        numbers = []
        answer = 0

        for number in input_arr:
            if number.isdigit():
                numbers.append(number)

        if('+' in user_input):
            answer = 0
            for j in numbers:
                answer = answer + int(j)

            data = "It is " + str(answer)
        if('-' in user_input):
            answer = numbers[0]
            for j in numbers:
                answer = answer - int(j)

            data = "It is " + str(answer)
        if('x', 'multiplied' in user_input):
            f = numbers[0]
            for j in numbers:
                print("J: " + j)
                f = int(f) * int(j)

            answer = str(f)

            data = "It is " + str(answer)
        if('/' in user_input):
            answer = numbers[0]
            for j in numbers:
                answer = answer / int(j)

            data = "It is " + str(answer)

        return data

    def valuePi(self):
        return "The Pi is " + str(math.pi)
