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


# Testing [comma seperates inputs]

# parameters: get_inp("enter y/n: ",["n","y"])
# inputs: n,y,Y,Crtl+C,7
# expected outcome: <accepted>, <accepted>, <asks again>, <asks again>, <asks again>

# parameters: get_inp("",[])
# inputs: y,1,Crtl+C
# expected outcome: <accepted>, <accepted>, <asks again>

# parameters: get_inp("",["y"])
# inputs: y,n,7,Crtl+C    
# expected outcome: <accepted>, <asks again>, <asks again>, <asks again>

get_inp("",[])