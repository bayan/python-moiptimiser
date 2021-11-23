from gurobipy import GRB

def print_model(model):
    OutputFlag = model.Params.OutputFlag
    model.Params.OutputFlag = 1
    model.display()
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
