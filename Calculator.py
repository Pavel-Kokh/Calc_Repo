import math


def calculator(num1: float, num2: float, choose_action: str):
    """
    calculator. Supports actions: plus, minus, multiply, divide, cosine, sine
    """

    def suma():
        result = math.fsum([num1, num2])
        print(f"{num1} + {num2} = {result}")

    def minus():
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    def mult():
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    def division():
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")

    def cosinus():
        result = math.cos(num1)
        print(f"Cos {num1} = {result}")

    def sinus():
        result = math.sin(num1)
        print(f"Sin {num1} = {result}")

    if choose_action == "1":
        suma()

    elif choose_action == "2":
        minus()

    elif choose_action == "3":
        mult()

    elif choose_action == "4":
        if num2 == 0:
            print("Число 2 не може дорівнювати 0")
            return

        division()

    elif choose_action == "5":
        cosinus()

    elif choose_action == "6":
        sinus()

    else:
        print("Ви ввели не вірні дані")
