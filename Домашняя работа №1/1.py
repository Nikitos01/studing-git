#  print(*((i + 1) for i in range(int(input("Введите число: ")))), sep="\n")

max_number = int(input("Введите число: "))
for i in range(1, max_number + 1):
    print(i)
