collection1 = {1, 2, 3, "k"}
print(collection1)

mymap = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
print("Map: ", mymap)


def split_input_map(inputMap):
    evenMap = {}
    oddMap = {}
    for (k) in inputMap.keys():
        if k % 2 == 0:
            evenMap[k] = inputMap[k]
        else:
            oddMap[k] = inputMap[k]

    print("EvenMap: ", evenMap)
    print("OddMap: ", oddMap)

split_input_map(mymap)


