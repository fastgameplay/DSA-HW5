def FindSq(a, b):
    lenA = len(a)
    lenB = len(b)
    output = ""
    bPointer = 0
    for i in range(lenA):
        for j in range(bPointer,lenB):
            if(a[i] == b[j]):
                output += a[i]
                bPointer = j
                break
    print(output)

a = input()
b = input()
FindSq(a,b)