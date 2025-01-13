from package import list_tools, string_tools
import my_module
import datetime
import math


def get_datetime() -> str:
    x = datetime.datetime.now()
    return f"{x.hour}:{x.minute}:{x.second}\t{x.year}.{x.month}.{x.day}"


def sqrt(x: int | float) -> float:
    return math.sqrt(x)


def main() -> None:
    print(sqrt(int(input("Введите число: "))))    
    print(get_datetime())
    print(my_module.my_sum(1, 2, 3, 4, 5))
    print(list_tools.chain([1, 2, 3], [4, 5, 6]))
    

if __name__ == "__main__":
    main()
