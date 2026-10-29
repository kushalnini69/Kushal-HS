# Demonstrates local variable shadowing (local count hides global count)
count = 0
def tick():
    count = 0
    count += 1
    return count
print(tick(), tick(), count)
#-----------------------------------
# Function reading global THRESHOLD constant without modifying it
THRESHOLD = 70
def is_alert(value):
    return value > THRESHOLD
print(is_alert(85), is_alert(60))
#-------------------------------------
# Demonstrates UnboundLocalError when trying to modify a global variable without global keyword
count = 0
def tick():
    count += 1
    return count

print(tick())
#-------------------------------------------
# Modifies global variable count inside function using global keyword
count = 0
def tick():
    global count
    count += 1
    return count

print(tick(), tick(), tick())
print("global count is now:", count)
#--------------------------------------
# Pure function pattern passing variable as argument and returning updated value
def tick(count):
    return count + 1
count = 0
count = tick(count)
count = tick(count)
print("count:", count)
#---------------------------------------
# Demonstrates local list variable scope inside make_report()
lines = 0
def make_report():
    lines = ["header"]
    lines.append("body")
    return len(lines)
print(make_report())
print(make_report())
print("lines" in dir())