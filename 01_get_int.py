# Gets an integer and returns the value
# Default min an max is -999,999 respectively
# Takes input as first argument, then optional min and max values
def get_int(inp,min=-999,max=999):
    while True:
        try:
            integer = int(input(inp))
            if integer < min or integer > max:
                raise ValueError
            return integer
        except:
            print(f"Please enter a valid integer between {min} and {max}.")
            continue


print(get_int("gimme number",0,12))
