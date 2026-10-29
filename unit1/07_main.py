# Standard module import and attribute/function access
import sys, os, importlib
sys.path.append(os.path.dirname(__file__))
sensors = importlib.import_module("06_sensors")

readings = [62, 84, 71]
print("threshold:", sensors.THRESHOLD)
print("average:", sensors.average(readings))
for r in readings:
    print(r, "->", "ALERT" if sensors.is_alert(r) else "ok")

# Inspects __name__ special variable for main vs imported module
print("__name__inside main.py is:", __name__)
print("__name__ inside sensors.py is:", sensors.__name__)

# Compares standard import, from-import, and module aliasing (as sn)
is_alert = sensors.is_alert
sn = sensors

print(sensors.is_alert(85))
print(is_alert(85))
print(sn.is_alert(85))

# Demonstrates wildcard import and local variable shadowing pitfall
THRESHOLD = sensors.THRESHOLD
print("my THRESHOLD is", THRESHOLD)
THRESHOLD = 30.0
print("my THRESHOLD is", THRESHOLD)
print("is_alert950 says", is_alert(50))