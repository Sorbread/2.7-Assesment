import pandas

# prepare_print
# returns formatted array, ready to be printed in form similar to [heading,paragraph,heading,paragraph]
def prepare_print(team_name,rider_information):
    # Convert our data into pandas dataframe
    rider_information_dataframe = pandas.DataFrame.from_records(rider_information)
    rider_information_dataframe = rider_information_dataframe.set_index(rider_information_dataframe.columns[0])
    rider_information_str = rider_information_dataframe.to_string()
    main_heading = f"{team_name}'s Points for this Tour."

    return [main_heading,rider_information_str]