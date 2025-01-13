def show_file(filename, mode:[1, 2]):
    with open(filename + '.txt') as file:
        if mode == 1:
            print(file.read())
        else:
            for line in file:
                print(line)


def write(filename):
    with open(filename + '.txt', 'w+') as file:
        old = file.read()
        file.write(old + input())

def main():
    show_file('example')

def show_file_prr(filename, mode:[1, 2]=1):
    try:
        with open(filename + '.txt') as file:
            if mode == 1:
                print(file.read())
            else:
                for line in file:
                    print(line)
    except FileNotFoundError:
        print("You are using a non-existent file! Change the file name.")


if __name__ == "__main__":
    main()
