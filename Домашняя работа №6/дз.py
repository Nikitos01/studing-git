from dataclasses import dataclass, field


class UserAccount(object):
    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password: str) -> None:
        self.__password = new_password

    def check_password(self, password: str) -> bool:
        return password == self.__password


class Vehicle(object):
    '''
    make: str
    model: str
    '''

    def __init__(self, make: str, model: str, v: int) -> None:
        self.make = make
        self.model = model
        self.v = v

    def get_info(self) -> str:
        return (f"Марка: {self.make}\n"
                f"Модель: {self.model}")

    def recount_v(self, s):
        k = 0.01  # расход топлива
        self.v -= s * k


class Car(Vehicle):
    def __init__(self, make: str, model: str, fuel_type: str):
        super(Vehicle, self).__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self) -> str:
        return (f"Марка: {self.make}\n"
                f"Модель: {self.model}\n"
                f"Вид топлива: {self.fuel_type}")


def main() -> None:
    account = UserAccount("Alex", "Lion194@gmail.com", "1234")
    account.set_password('qwerty')
    # print(account._UserAccount__password)
    print('Совпадают' if account.check_password('1234') else 'Не совпадают')


if __name__ == "__main__":
    main()
