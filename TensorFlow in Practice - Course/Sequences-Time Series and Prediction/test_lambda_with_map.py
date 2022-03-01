# With def come the advantages of multiple lines, loops, comments, tests and what have you.
# lambda is a simple version of def (already integrated RETURN)
a = lambda n: n * 2
print(a(2))

result = list(map(lambda n: n * 2, [1, 2, 3, 4, 5]))
print(result)


# Map is often used with lambda, but it works with a def too.
def test(n):
    t = [i for i in range(n)]
    return sum(t)


print(list(map(test, [10])))

# As a companion to map(),
# the filter() function takes a function and a list,
# and returns a sub-set list of the ELEMENTS where the function returns true.
print(list(filter(lambda x: x % 2 == 0, range(10))))
print(list(map(lambda x: x % 2 == 0, range(10))))
