# deleting items from list mid loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in range(len(numbers)-1, 0, -1):
    print("i", i)
    print("numbers list", numbers)
    if numbers[i] % 2 == 0:
        print("DELETING")
        del numbers[i]
    