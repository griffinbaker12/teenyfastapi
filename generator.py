def doh2():
    yield "Homer"
    yield "Marge"
    yield "Bart"


for name in doh2():
    print(name)
