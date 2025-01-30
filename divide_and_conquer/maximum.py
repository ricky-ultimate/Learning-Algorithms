def findMax(list):
    if list == []:
        return None
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    max = findMax(list[1:])

    if list[0] > max:
        return list[0]
    else:
        return max


if __name__ == "__main__":
    my_list = [2, 4, 6]
    print(findMax(my_list))
