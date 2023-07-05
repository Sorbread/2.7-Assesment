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


# Testing Plan 
# with parameters get_int("",0,10)
# -1,0,1,9,10,11,Crtl+C

