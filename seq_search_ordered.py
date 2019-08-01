def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    count = 0

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1
        count += 1
    print(count , "elements checked")
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3)) #return False
print(orderedSequentialSearch(testlist, 13)) #return True