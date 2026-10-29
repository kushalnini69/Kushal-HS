# Demonstrates list modification methods: append, insert, and remove
errors = ["E2", "E7"]
print(errors)

errors.append("E2")
print("after append: ", errors)

errors.insert(0, "E1")
print("after insert: ", errors)

errors.remove("E7")
print("after remove:", errors)
#--------------------------------------------------
# Demonstrates reference assignment (b = a) vs shallow copy (c = a[:])
a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c.append(99)
print("a = ", a)
print("b = ", b)
print("c = ", c)

print("b is a:", b is a, "| c is a:", c is a)
#-------------------------------------------------
# Demonstrates iteration pitfall: mutating a list while looping over it skips elements
readings = [10, -1, -1, 20, 30]
for r in readings:
    if r == -1:
        readings.remove(r)
print(readings)
#--------------------------------------------------
# Demonstrates list comprehensions for element transformation and filtering
readings = [12, 45, 7, 61, 33]
doubled = [r *2 for r in readings]
big = [r for r in readings if r > 30]
print(doubled)
print(big)