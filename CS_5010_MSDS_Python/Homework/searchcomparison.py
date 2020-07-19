
def linearSearch(target,my_list):
    for index, item in enumerate(my_list):
        if item ==target:
            return index

numberlist = [6,6,8,4,9,5,1,3,4,7,10]
print(linearSearch(5, numberlist))
print(linearSearch(10, numberlist))
print(linearSearch(4, numberlist))

zoo = ['lion','tiger','elephant','zebra','bear']
print(linearSearch("zebra", zoo))
print(linearSearch("tiger", zoo))


def BinarySearch(item_list, target):
    sorted(item_list)
    high = len(item_list)
    low = 0
    midi = round((high+low)/2)
    lastm = low
    while lastm != midi: #abs(low-high) != 1:
        midv = item_list[midi]
        if midv == target:
            return True
        elif midv > target:
            high = midi
        elif midv < target:
            low = midi
        lastm = midi
        midi = round((high+low)/2)
    return False

# Testing
list1 = [1,3,5,8,10]
print(f"Is 6 in {list1}? {BinarySearch(list1, 6)}")
print(f"Is 5 in {list1}? {BinarySearch(list1, 5)}")
print(f"Is 1 in {list1}? {BinarySearch(list1, 1)}")