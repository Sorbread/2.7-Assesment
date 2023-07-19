import pandas

# prepare_print
# returns formatted array, ready to be printed in form similar to [heading,paragraph,heading,paragraph]
def prepare_print(team_name, rider_information):
    # The main heading
    main_heading = f"Team {team_name}"
    # Convert our data into pandas dataframe
    rider_information_dataframe = pandas.DataFrame.from_records(rider_information)
    # Set index of our dataframe
    rider_information_dataframe = rider_information_dataframe.set_index(
        rider_information_dataframe.columns[0]
    )
    # Stringify our dataframe so we are able to print it
    rider_information_str = rider_information_dataframe.to_string()
    
    return [main_heading, rider_information_str]

print(prepare_print("RED",[{'Name': 'David', 'Race 1': 2, 'Race 2': 3, 'Calculated Tally': 4},{'Name': 'George', 'Race 1': 3, 'Race 2': 4, 'Race 3': 4, 'Calculated Tally': 1}]))