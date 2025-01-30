def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


if __name__ == "__main__":
    my_list = [2, 4, 6]
    print(sum(my_list))
