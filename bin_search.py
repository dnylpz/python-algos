import random
number_list = [random.randrange(0,100) for x in range(0,50)]

number_list.sort()

def bin_search(objective,group):
    print("current group:\n {}".format(group))
    pivot = len(group)//2
    if len(group) > 1:
        if objective < group[pivot]:
            return bin_search(objective,group[:pivot])
        elif objective > group[pivot]:
            return bin_search(objective,group[pivot:])
        elif objective == group[pivot]:
            print(group)
            print("idx found: {}".format(pivot))
            return group[pivot]
    else:
        if objective == group[0]:
            print(group)
            return group[0]
        else: return False

found = bin_search(5,number_list)
if found:
    print("found!")
    print(found)
else:
    print('5 not in list')

