from gurobipy import GRB

import pprint

def print_model(model):
    OutputFlag = model.Params.OutputFlag
    model.Params.OutputFlag = 1
    model.display()
    print("")
    model.Params.OutputFlag = OutputFlag

def Mone(value):
    if value >= GRB.MAXINT: return 'M'
    if value <= -GRB.MAXINT: return '-M'
    return value

def Mall(values):
    constructor = type(values)
    return constructor( [MD(value) for value in values] )

def MD(value):
    return Mall(value) if type(value) in (list, tuple, set) else Mone(value)

def disp(name, var):
    print(f"{name}: {MD(var)}")


def replace_Ms(values, offset=0):
    datastructure = type(values)
    if datastructure in (set, list, tuple):
        return datastructure([replace_Ms(value, offset) for value in values])
    else:
        if values + 100 >= GRB.MAXINT:
            return 'M'
        elif values - 100 <= -GRB.MAXINT:
            return '-M'
        else:
            return values + offset

def print_vals(message, values, offset=0):
    message = f"{message}: {replace_Ms(values, offset)}"
    message = message.replace("'","")
    print(message)
