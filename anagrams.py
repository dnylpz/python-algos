test_input = ['star','rats','car','arc','arts','start']
output = [['star','rats','arts'],
         ['car','arc'],
          ['start']]


def group_anagrams(ingest):
    mydict = {}
    for i in ingest:
        sumed=0
        largest=0
        for char in i:
            sumed += ord(char) 
            largest = max(largest,ord(char))
        hashed = "{}|{}|{}".format(len(i),largest,sumed)
        if hashed not in mydict.keys():
            mydict[hashed] = [i]
        else:
            mydict[hashed].append(i)
    return mydict

print(group_anagrams(test_input))