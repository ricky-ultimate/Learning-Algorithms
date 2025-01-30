def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


if __name__ == "__main__":
    my_list = [2, 4, 6]
    print(count(my_list))
