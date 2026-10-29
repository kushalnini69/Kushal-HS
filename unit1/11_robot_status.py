# Demonstrates dictionary CRUD operations (create, read key, update value, insert key)
robot = {"name": "Alpha", "battery": 78, "mode": "auto"}
print(robot)
print(robot["name"])
robot["battery"] -= 5
robot["speed"] = 0.4
print(robot)
print("keys :", list(robot.keys()))
print("values:", list(robot.values()))
#-----------------------------------------------------------------------
# Demonstrates dict.get() for safe retrieval without KeyError
robot = {"name": "Alpha", "battery": 78}
print(robot.get("speed"))
print(robot.get("speed", 0.0))
print("speed" in robot)
#-----------------------------------------------------------------------
# Builds a frequency counter dictionary and sorts keys by occurrence count
log = ["E2", "E7", "E2", "E1", "E7", "E2"]
freq = {}
for code in log:
    freq[code] = freq.get(code, 0) + 1
print(freq)
for code in sorted(freq, key = freq.get, reverse = False):
    print(f"{code} occurred {freq[code]} time(s")
print(freq)
#-----------------------------------------------------------------------------------------

"""
    write a program that counts the frequency of characters in your name, print each
    letter with its count and then prints the most frequent letter
"""
# Counts character frequency in a string name and prints sorted character counts
name = "shubham"
freq = {}
for i in range(len(name)):
    freq[name[i]] = freq.get(i, name.count(name[i]))
print(freq)
for i in sorted(freq, key = freq.get, reverse = True):
    print(f"{i} occurred {freq[i]} times")