def add(input1, input2, input3):

    count = 0

    for i in range(input3):

        for j in range(input3):

            if input1[i] == input2[j]:

                count += 1
                break

    return count


input1 = list(map(int, input("Enter first array: ").split()))

input2 = list(map(int, input("Enter second array: ").split()))

input3 = int(input("Enter size: "))

A1 = add(input1, input2, input3)

print(A1)