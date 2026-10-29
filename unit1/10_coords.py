# Demonstrates sets: unordered collections of unique elements and O(1) membership testing
visited = {(0, 0), (0, 1)}
visited.add((1, 1))
visited.add((0, 0))
print(visited)
print("count:", len(visited))
print("(1, 1) visited?", (1, 1) in visited)
print("(9, 9) visited?", (9, 9) in visited)
#----------------------------------------------------
# Uses set() constructor to deduplicate a list of items
codes = ["E2", "E7", "E2", "E1", "E7"]
print("raw: ", codes)
print("unique:", set(codes))
print("unique count:", len(set(codes)))
#-----------------------------------------------------
# Demonstrates tuple creation, tuple unpacking, and single-element tuple syntax (5,)
position = (4.2, 7.8)
print(position, type(position))
x, y = position
print("x =", x, "| y =", y)
single = (5,)
print(single, type(single))
#---------------------------------------------------------------------------
""""
    write a program to simulate a robot visiting grid cells. start with an empty set, 
    add 8 coordinates of which 3 repeats, then print how many distinct cells were 
    visited and test whether (2, 2) was among them.
"""
# Simulates robot grid visits using a set to store distinct coordinate tuples
c = set()
c.add((0, 0))
c.add((0, 1))
c.add((0, 2))
c.add((0, 3))
c.add((0, 2))
c.add((1, 2))
c.add((1, 1))
c.add((1, 0))
print(c)
print(len(c))
print((2, 2) in c)