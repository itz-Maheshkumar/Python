my_set = {"apple", "banana", "cherry"}
print(my_set)

my_set_2 = set(["one", "two", "three"])
my_set_2 = set(("one", "two", "three"))
print(my_set_2)

my_set_3 = set("aaabbbcccdddeeeeeffff")
print(my_set_3)

a = {}
print(type(a))
a = set()

my_set = set()
my_set.add(42)
my_set.add(True)
my_set.add("Hello")
print(my_set)

my_set.add(42)
print(my_set)

my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print(my_set)

my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)

my_set.clear()
print(my_set)

a = {True, 2, False, "hi", "hello"}
print(a.pop())
print(a)

my_set = {"apple", "banana", "cherry"}
if "apple" in my_set:
    print("yes")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff_set = setA.difference(setB)
print(diff_set)

diff_set = setB.difference(setA)
print(diff_set)

diff_set = setA.symmetric_difference(setB)
print(diff_set)

diff_set = setB.symmetric_difference(setA)
print(diff_set)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issubset(setB))
print(setB.issubset(setA)) 

print(setA.issuperset(setB)) 
print(setB.issuperset(setA))

setC = {7, 8, 9}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

a = frozenset([0, 1, 2, 3, 4])

odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))
