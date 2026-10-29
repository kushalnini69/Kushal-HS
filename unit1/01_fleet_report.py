# Repetitive code without functions checking battery status for 3 robots
r1_battery = 8
if r1_battery < 15:
    print("Alpha: CRITICAL")
elif r1_battery < 30:
    print("Alpha: LOW")
else:
    print("Alpha: OK")

r2_battery = 22
if r2_battery < 15:
    print("Beta: CRITICAL")
elif r2_battery < 30:
    print("Beta: LOW")
else:
    print("Beta: OK")

r3_battery = 76
if r3_battery < 15:
    print("Gamma: CRITICAL")
elif r3_battery < 30:
    print("Gamma: LOW")
else:
    print("Gamma: OK")
#-----------------------------------------------------------
# Reusable function definition with a default parameter name="neev"
def battery_band(pct, name="neev"):
    """Classify a battery percentage into a band."""
    if pct < 15:
        print(f"{name}: CRITICAL")
    elif pct < 30:
         print(name,": LOW")
    else:
        print(f"{name}: OK")
battery_band(8, "Alpha")
battery_band(22,"Beta")
battery_band(76)
#----------------------------------------------------------
# Redefining function to return a string value instead of printing
def battery_band(pct):
    if pct<15:
        return "critical"
    elif pct<30:
        return "low"
    return "OK"
#----------------------------------------------------------------
# Using the return function inside a dictionary iteration loop
fleet = {"Alpha": 8, "Beta": 22, "Gamma": 76, "Delta": 41}
for name, pct in fleet.items():
    print(f"{name: <7} {pct: >3}% {battery_band(pct)}")
#----------------------------------------------------------------
# Compares printing inside a function (returns None) vs returning a calculated value
def area(r):
    print(3.14 * r * r)
total = area(2) + area(3)
print("total:", total)

def area(r):
    return 3.14 * r * r
total = area(2) + area(3)
print("total:", total)
#--------------------------------------------------------------
# Demonstrates calling functions with positional, default, and keyword arguments
def move_robot(x, y, speed = 1.0):
    print(f"moving to ({x}, {y}) at {speed} m/s")
move_robot(3, 4)
move_robot(3, 4, 0.5)
move_robot(y = 4, x = 3)
move_robot(3, speed = 2.0, y = 4)
#-----------------------------------------------------------
# Demonstrates variable-length arguments (*args for positional tuple, **kwargs for keyword dict)
def log(*values, **options):
    print("values:", values)
    print("options:", options)

log("start")
log("waypoint", 3, 4.5)
log("alert", level = "high", retries = 2)
log()
#--------------------------------------------------
# Demonstrates the mutable default argument trap (route=[] is shared across all function calls)
def add_waypoint(wp, route = []):
    route.append(wp)
    return route
#-------------------------------------------------
r1 = add_waypoint((0, 0))
r2 = add_waypoint((5, 5))
print("r1 = ", r1)
print("r2 = ", r2)
print("same objects?", r1 is r2)