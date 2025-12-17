n = int(input())
integer_list = tuple(map(int,input().split()))

print(hash(integer_list))

########################################################
def custom_sort(s):
    def sort_key(c):
        if c.islower():
            return (0, c)
        elif c.isupper():
            return (1, c)
        elif c.isdigit():
            if int(c) % 2 != 0:
                return (2, c)
            else:
                return (3, c)

    return "".join(sorted(s, key=sort_key))


s = input()
print(custom_sort(s))