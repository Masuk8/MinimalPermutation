min_dot = ([1, 2, 3, 4, 5], [0, 0, 1, 1, -4])
a = list(min_dot[0])
b = list(min_dot[1])


print(a)
print(b)


def min_dot(a, b):
    c = 0
    a.sort(reverse=True)
    b.sort()
    d = 0
    while len(a) > 0:
        c = a[0] * b[0]
        d += c
        a.remove(max(a))
        b.remove(min(b))
        print(d)
        return d


"a.remove([0])"

min_dot(a, b)


"a.remove(max(a))"

"print(max(a))"
"print(min(a))"

"if no 0 and no negative, then it doesnt matter"
"if no 0 and negative, then multiplyy 0 with highest numbers"
"if is zero AND no negative, then multiply highest of a with lowest of b"
"if is zero AND negative, then multiply negatives with highest numbers and rest of highest numbers with 0s"