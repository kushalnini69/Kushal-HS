"""Sensor helpers for the mission console."""

# Module constant for sensor threshold
THRESHOLD = 70.0

# Helper function to check if value exceeds alert threshold
def is_alert(value):
    """True whe a reading exceeds the alert threshold."""
    return value > THRESHOLD

# Helper function calculating mean of sensor readings list
def average(values):
    """Mean of a list of readings."""
    return sum(values)/len(values)

# Main guard block executing self-test ONLY when script is run directly
if __name__ == '__main__':
    print("self-test:", is_alert(85), average([10, 20, 30]))