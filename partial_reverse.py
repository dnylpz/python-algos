import random
random.seed(1234)
array_len = random.randrange(50)
stop = random.randrange(array_len)
array = [random.randrange(50) for x in range(0,array_len)]
print("input: \n {}".format(array))

print("subset\n: {}".format(array[:stop]))
def partial_reverse(input_array, end_reverse):
    if end_reverse > len(input_array):
        print("Bad End_reverse")
    for i in range(0, end_reverse//2):
        temp = input_array[i]
        input_array[i] = input_array[end_reverse-1-i]
        input_array[end_reverse-1-i] = temp

    return input_array

partial_reverse(array,stop)
print("result \n: {}".format(array))
print("result subset\n: {}".format(array[:stop]))
