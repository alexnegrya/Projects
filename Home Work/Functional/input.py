# inputInt( message )
# inputFloat( message )
# inputBoolean( message )

# ########### define functions #############
def inputInt(string):
    r = int( input(string) )
    return r


def inputFloat(string):
    r = float( input(string) )
    return r


def inputBoolean(string):
    r = bool( input(string) )
    return r
# ##########################################

# ############# call functions #############
n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")

print(f'Add result is {n + m}.')
# ##########################################
