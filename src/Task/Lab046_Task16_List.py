if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range (N):
        command_line = input().split()
        command = command_line[0]
        arg = list(map(int, command_line[1:]))

    if command == "insert":
        list.insert(arg[0],arg[1])
    elif command == "print":
        print(list)
    elif command == "remove":
        list.remove(args[0])
    elif command == "append":
        list.append(arg[0])
    elif command == "sort":
        list.sort
    elif command == "pop":
        list.pop
    elif command == "reverse":
        list.reverse()