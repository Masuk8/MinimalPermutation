min_dot = ([1, 3, 5], [4, -2, 1])

a = list(min_dot[0])
b = list(min_dot[1])


def min_dot(a, b):
    a.sort(reverse=True)
    b.sort()
    d = 0
    while len(a) > 0:
        c = a[0] * b[0]
        d += c
        a.remove(max(a))
        b.remove(min(b))
    print(d)


min_dot(a, b)
# print(d)
# a.remove([0])
# a.remove(max(a))

# print(max(a))
# print(min(a))
#
# if no 0 and no negative, then it doesnt matter
# if no 0 and negative, then multiplyy 0 with highest numbers
# if is zero AND no negative, then multiply highest of a with lowest of b
# if is zero AND negative, then multiply negatives with highest numbers and rest of highest numbers with 0s