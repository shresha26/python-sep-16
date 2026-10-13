def add(number, *data):
    return data


print(add(1, 2, 3, "testing"))
print(add(1, 2, 3, 5))
print(add(1))


def count_occurences(target, *args):
    count = 0
    for i in args:
        if i == target:
            count = count + 1

    return target, count


target, count = count_occurences("hello", 1, 2, 3, 4, 5, 6, 7, 4, 4, 5, 6)
print(f"{target} occurs {count} times")


def test(**kwargs):
    print(kwargs)


test(ename="ram", lname="sharma", age=26, role="developer", epassport=True)
test(lname="sharma", age=26)


a = "test"
print(a.startswith("t"))
print(a[0] == "t")
