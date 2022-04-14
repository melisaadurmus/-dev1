def compareTo(arr1, arr2):
    alice = []
    bob = []
    result = []
    sum1 = 0
    sum2 = 0
    if (len(arr1) != len(arr2)):
        print("Please enter a number of the same length!")
    else:
        for i in range(len(arr1)):
            if arr1[i] < arr2[i]:
                bob.append(1)

            if arr1[i] > arr2[i]:
                alice.append(1)

        for i in alice:
            sum1 = sum1 + i
        result.append(sum1)
        for i in bob:
            sum2 = sum2 + i
        result.append(sum2)

        return result


p1 = input("Alice Please enter numbers with spaces between them:")
p3 = p1.split()
p2 = input("Bob Please enter numbers with spaces between them:")
p4 = p2.split()
result = compareTo(p3, p4)
if result != None:
    print(' '.join([str(elem) for elem in result]))
