def greet(name):
    username = input("Введите имя: ")
    print(f"Привет, {username}!")


def square(number):
    return number * number
    # return number ** 2


def max_of_two(x, y):
    if x > y:
        return x
    return y


def describe_person(name, age=30):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")


def is_prime(number):
    q = number ** 0.5
    if q % 1 == 0:
        return False

    for d in range(2, int(q) + 1):
        if number % d == 0:
            return False
    return True
