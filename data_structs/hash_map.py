# dicts = HashMaps, is not that hard


class HashMap():

    def __init__(self, array=[]):
        self.array = [None for x in range(0, 65)]
        self.lenght = 64

    def __gen_hash__(self, key):
        return 64//len(key)

    def get(self, key):
        hash_result = self.__gen_hash__(key)
        if self.array[hash_result] is None:
            return False # item not in  map
        if key == self.array[hash_result][0][0]:
            return self.array[hash_result]
        else:
            for item in self.array[hash_result]:
                if key == item[0]:
                    return item[1]
            return False # not in hash

    def add(self, key, value):
        hash_result = self.__gen_hash__(key)
        if self.array[hash_result] is None:
            # initialiting list
            self.array[hash_result] = [[key, value]]
            return True
        elif self.array[hash_result][0][0] == key:
            # first/unique key
            self.array[hash_result][0] = [key, value]
            return True
        for item in range(0,len(self.array[hash_result])):
            if key == self.array[hash_result][item][0]:
                self.array[hash_result][item] = [key, value]  # validate if this works later
                return True
        # if reaches this point kv is new in hash
        self.array[hash_result].append([key, value])
        return True

    def remove(self,key):
        hash_result = self.__gen_hash__(key)
        if self.array[hash_result] is None:
            return False # item not in map
        if key == self.array[hash_result][0][0]:
            self.array[hash_result] = None
            return True
        for item in range(0,len(self.array[hash_result])):
            if key in self.array[hash_result][item][0]:
                self.array[hash_result].remove(self.array[hash_result][item])
                return True
        return False # not in key

    def __repr__(self):
        array = []
        for item in self.array:
            if item is not None:
                array.append(item)
        return "{}".format(array)


this_hash = HashMap()
print("{}\n".format(this_hash))
this_hash.add("message","hello")
print("{}\n".format(this_hash))
this_hash.add("message","world")
print("{}\n".format(this_hash))
this_hash.add("vampire","something")
print("{}\n".format(this_hash))
this_hash.add("vampire","something else")
print("{}\n".format(this_hash))

print(this_hash.get('vampire'))
print(this_hash.get('message'))
print(this_hash.get('notinhash'))
this_hash.add('minecra','steve')
print(this_hash)
this_hash.remove('vampire')
print(this_hash)
