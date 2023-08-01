MAX_PLACING = 50
# Points rider received depending on what place they got
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

# get inp
# gets user input and checks it against optional array of possible answers
# not recommended to use when all answers are acceptable (just use input())
def get_inp(question,answers=[]):
    # If no answer is given, input can still return an error
    # so is put inside while True loop
    if len(answers) == 0:
        while True:
            try:
                response = input(question)               
                return response
            except:
                print("Please enter a valid response.")

    # If we are given answer/s
    while True:
        try:
            response = input(question)
            if not response in answers:
                raise  ValueError
            return response
        except:
            # More optimal text based on if only 1 answer or more
            if len(answers) > 1:
                error_text = f"such as '{answers[0]}' or '{answers[1]}'."
            else:
                error_text = f"such as '{answers[0]}'."
            print(f"Please provide a valid response, {error_text}")

# Gets an integer and returns the value
# Default min an max is -999,999 respectively
# Takes input as first argument, then optional min and max values
def get_int(question,min=-999,max=999):
    while True:
        try:
            integer = int(input(question))
            if integer < min or integer > max:
                raise ValueError
            return integer
        except:
            print(f"Please enter a valid integer between {min} and {max}.")
            continue


# get_rider_information
# gets each individual riders name, placing per race, and calculates points per race
# returns dictionary in form {"Name":string,{variable number of placings per races},"Calculated Tally",integer}
def get_rider_information(team_name,races):
    rider_dictionary = {}
    rider_dictionary[f"Team {team_name} Placings"] = get_inp("Please Enter a Riders Name: ")    
    
    total_points = 0
    # Get information for each race
    for i in range(races):
        placing = get_int(f"Please Enter this Riders Placing Placing For Race {i+1} (enter 0 if did not compete): ",0,MAX_PLACING)
        rider_dictionary[f"Race {i+1}"] = placing
        total_points += calculate_points(placing)
    
    # Add Total Points
    rider_dictionary["Calculated Tally"] = total_points
    
    return rider_dictionary

# Testing
# Ensure no negative values can be inputted
print(get_rider_information("RED",3))