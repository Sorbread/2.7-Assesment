PLACEMENT_POINTS = {
    1: 5,
    2:3,
    3:1,
}

# calculate points
# calculate how many points the rider has earned based off placing
def calculate_points(placing):
    if placing in PLACEMENT_POINTS:
        return PLACEMENT_POINTS[placing]
    return 0

# Testing
print(calculate_points(1))
print(calculate_points(2))
print(calculate_points(3))
print(calculate_points(5))