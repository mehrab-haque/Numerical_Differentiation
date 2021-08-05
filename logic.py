from math import inf
from tabulate import tabulate

def forwardDifference(func,x,delX):
    return (func(x+delX)-func(x))/delX

def backwardDifference(func,x,delX):
    return (func(x)-func(x-delX))/delX

def centralDifference(func,x,delX):
    return (func(x+delX)-func(x-delX))/(2*delX)

def secondDerivative(func,x,delX):
    return (func(x+2*delX)-2*func(x+delX)+func(x))/(delX*delX)

def secondDerivativeEfficient(func,x,delX):
    return (func(x+delX)-2*func(x)+func(x-delX))/(delX*delX)

def iterate(func,operation,x,delX,tolerance,delXLabel,operationLabel):
    err=inf
    iter=1
    prevVal=0
    data=[]

    while err>tolerance:
        val=operation(func,x,delX)
        error='-'
        if iter>1:
            err=abs(val-prevVal)*100/val
            error=err
        prevVal=val
        data.append([iter,delX,val,error])
        iter+=1
        delX/=2

    return tabulate(data,headers=['Iteration',delXLabel,operationLabel,'Ea (%)'],tablefmt='pretty')
