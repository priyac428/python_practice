# Topic : Parameters and Arguments
def marriage(boy,girl):
    print(f"{boy} marries {girl}")

marriage("ayush","amaya")  #positional arguments
marriage(boy="sushanth",girl="samaya") #keyword arguments

def names(name="none"):#default parameter values
    print(name)

names()