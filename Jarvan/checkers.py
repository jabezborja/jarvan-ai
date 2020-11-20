
class Checkers:
    def __init__(self):
        pass

    def is_operation(self, command):
        operations = ['+', '-', 'x', '*', '/',
                      'plus', 'minus', 'times', 'divide']

        for operation in operations:
            if operation in command:
                return True
