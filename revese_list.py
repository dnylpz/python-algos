array = [0,1,2,3,4,5,10,11,12,45,124]

def reverse_by_groups(ingest,groupsize):
    last_changed=0
    for times in range(0,len(ingest)//groupsize):
        temp = ingest[last_changed]
        ingest[last_changed] = ingest[groupsize-1+last_changed]
        ingest[groupsize-1+last_changed] = temp
        last_changed += groupsize

print("before: \n{}".format(array))
reverse_by_groups(array,4)
print("after: \n{}".format(array))
