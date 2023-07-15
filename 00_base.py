# 00_base.py
# BMX Club point calculator and write to file-er
import pandas
from datetime import date

# Maximum placing that a rider can get. 50 riders per race, so default is 50
MAX_PLACING = 50

# Points rider received depending on what place they got
PLACEMENT_POINTS = {
    1: 5,
    2: 3,
    3: 1,
}


# Gets an integer and returns the value
# Default min an max is -999,999 respectively
# Takes input as first argument, then optional min and max values
def get_int(question, min=-999, max=999):
    while True:
        try:
            integer = int(input(question))
            if integer < min or integer > max:
                raise ValueError
            return integer
        except:
            print(f"Please enter a valid integer between {min} and {max}.")
            continue


# get inp
# gets user input and checks it against optional array of possible answers
def get_inp(question, answers=[]):
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
                raise ValueError
            return response
        except:
            # More optimal text based on if only 1 answer or more
            if len(answers) > 1:
                error_text = f"such as '{answers[0]}' or '{answers[1]}'."
            else:
                error_text = f"such as '{answers[0]}'."
            print(f"Please provide a valid response, {error_text}")


# calculate points
# calculate how many points the rider has earned based off placing
def calculate_points(placing):
    if placing in PLACEMENT_POINTS:
        return PLACEMENT_POINTS[placing]
    return 0


# get_rider_information
# gets each individual riders name, placing per race, and calculates points per race
# returns dictionary in form {"Name":string,{variable number of placings per races},"Calculated Tally",integer}
def get_rider_information(races):
    rider_dictionary = {}
    rider_dictionary["Name"] = get_inp("Please enter a riders name: ")

    total_points = 0
    # Get information for each race
    for i in range(races):
        placing = get_int(
            f"Please enter your placing for race {i+1} (enter 0 if did not compete): ",
            0,
            MAX_PLACING,
        )
        rider_dictionary[f"Race {i+1}"] = placing
        total_points += calculate_points(placing)

    # Add Total Points
    rider_dictionary["Calculated Tally"] = total_points

    return rider_dictionary


# prepare_print
# returns formatted array, ready to be printed in form similar to [heading,paragraph,heading,paragraph]
def prepare_print(team_name, rider_information):
    # The main heading
    main_heading = f"Team {team_name} Placings"
    # Convert our data into pandas dataframe
    rider_information_dataframe = pandas.DataFrame.from_records(rider_information)
    # Set index of our dataframe
    rider_information_dataframe = rider_information_dataframe.set_index(
        rider_information_dataframe.columns[0]
    )
    # Stringify our dataframe so we are able to print it
    rider_information_str = rider_information_dataframe.to_string()
    
    return [main_heading, rider_information_str]


# Get race amount & riders per team
# These values seem to be constant over all teams based on standard
race_amount = get_int(
    "Please enter the amount of races your teams will be competing in: ", 0
)
riders_per_team = get_int("Please enter the number of riders per team: ", 0)

# Main program loop
while True:
    team_name = get_inp("Please enter your team name (or type 'xxx' to exit): ")
    if team_name == "xxx":
        break

    rider_information = []

    # Get rider information
    for rider_index in range(riders_per_team):
        rider_information.append(get_rider_information(race_amount))

    # Prepare the printout (array)
    printout = prepare_print(team_name, rider_information)

    # Get date for fomatting
    today = date.today()
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%y")

    # Write to file & print to console
    filename = f"{team_name}_{day}_{month}_{year}.txt"
    text_file = open(filename, "w")
    for element in printout:
        print(element)
        text_file.write(element)
        text_file.write("\n")
    text_file.close()
