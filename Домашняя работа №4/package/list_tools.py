def chain(*args):
    lst = []
    for el in args:
        if hasattr(el, "__iter__"):
            lst += chain(*el)
        else:
            lst.append(el)
    return lst


if __name__ == "__main__":
    arr = [1, 2, [3, 4, 5, 6], [7, 8, [9]]]
    print(chain(arr))
    