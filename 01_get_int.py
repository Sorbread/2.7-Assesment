# Gets an integer and returns the value
# Default min an max is -999,999 respectively
# Takes input as first argument, then optional min and max values (must be a number)
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
# inputs: -1,0,1,9,10,11,Crtl+C,.1
# expected outcome: <asks again>,<continues>,<continues>,<continues>,<continues>,<asks again>,<asks again>,<asks again>

# with parameters get_int("bread:")
# inputs: -1,11,Crtl+C,.1
# expected outcome: <continues>,<continues>,<asks again>, <asks again>

get_int("bread: ")
