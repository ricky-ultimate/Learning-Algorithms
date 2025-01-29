def findSmallest(list):
    smallest = list[0]
    index = 0
    for i in range(len(list)):
        if list[i] < smallest:
            smallest = list[i]
            index = i
    return index


def selection_sort(list):
    newList = []
    for i in range(len(list)):
        smallest = findSmallest(list)
        newList.append(list.pop(smallest))
    return newList


if __name__ == "__main__":
    my_list = [5, 3, 6, 2, 10]
    print(findSmallest(my_list))
    print(selection_sort(my_list))
