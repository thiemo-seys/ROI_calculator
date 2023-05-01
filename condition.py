# TODO: this needs some work and testing

class Condition:
    def __init__(self, operator: str, value):
        self.operator = operator
        self.value = value

    def fulfilled(self, input_value):
        self.operator(input_value, self.value)