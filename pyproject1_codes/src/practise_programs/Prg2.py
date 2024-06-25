# Function to remove the duplicate element from the list
list1: list = [23, 7, 9, 22, 4, 7, 66, 5]
list2: list = [67, 88, 92, 99, 67, 51]


def remove_the_duplicate(lt: list, first_or_last: bool = False) -> None:
    for i in range(0, lt.__len__() - 1):
        for j in range(i + 1, lt.__len__() - 1):
            # print(lt[j], " ", lt[i])
            if lt[j] == lt[i]:
                if first_or_last:
                    lt.remove(lt[j])
                else:
                    lt.remove(lt[i])


def remove_the_duplicate_and_original(lt: list) -> list:
    return [i for i in lt if lt.count(i) == 1]
# return [lt[i] for i in range(0, len(lt) - 1) for j in range(i + 1, len(lt) - 1) if lt[i] == lt[j]]


print(list1)
remove_the_duplicate(list1, True)
print(list1)
print(list2)
list2 = remove_the_duplicate_and_original(list2)
print(list2)
