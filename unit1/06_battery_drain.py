# Simulates battery drain over time using a basic while loop
battery = 100
minutes = 0
while battery > 20:
    battery -= 7
    minutes += 1
print(f"Low battery alert {minutes} minutes ({battery})%")
#--------------------------------------------------------------
# Prints per-minute battery status log inside the while loop
battery = 100
minutes = 0
while battery > 20:
    battery -= 7
    minutes += 1
    print(f"minute {minutes:2d} -> battery {battery}%")
print("Alert")
#--------------------------------------------------------------
# Validates user input range using an infinite while True loop and break statement
while True:
    test = input("Enter battery %(0 - 100): ")
    value = float(test)
    if 0 <= value <= 100:
        break
    print("Out of range, try again")
print("accepted: ", value)
#----------------------------------------------------------------
"""
   WRITE A PYTHON PROGRAM IN WHICH A LOOP STARTS OF VALUE 10 & COUNTS DOWN TO 1, 
   PRINTING EACH VALUE OF THE COUNT AND THEN PRINTS LIFT OFF
"""
# Countdown loop from 10 to 1 using while True and break
value = 10
while True:
    print(value)
    value -= 1
    if value == 0:
        break
print("Take off")

"""OR"""
# Countdown loop from 10 to 1 using a conditional while loop
value = 10
while value >= 1:
    print(value)
    value -= 1
print("Take off")
#-----------------------------------------------------------------------------------
"""
    WRITE A PYTHON PROGRAM THAT ADDS NUMBERS FROM 1 TO 100 AND PRINTS THE TOTAL
"""
# Accumulator loop summing numbers using while True and break
j = 0
i = 1
while True:
    j = j+1
    i += 1
    if i == 100:
        break
print(j)