N = int(input())
index = 0
for i in range(N):
    command = input()
    if command[0:3] == "push":
        x = int(command[5:-1])
        array[index] = x
        index += 1
    elif command == "pop":
        index -= 1
        if index < 0:
            result = -1
            index = 0
        else:
            result = array[index]
    elif command == "size":
        result = index
    elif command == "empty":
        if index == 0:
            result = 1
        else:
            result = 0
    elif command == "top":
        if index == 0:
            result = -1
        else:
            result = array[index-1]
    print(result)
