import sympy as sp
from logic import *

def velocity(t):
    return 2000*sp.log(140000/(140000-2100*t))-9.8*t

time = sp.Symbol('t')
velocityFunction = velocity(time)
accelerationFunction = sp.lambdify(time, velocityFunction.diff(time))

val=centralDifference(velocity,16,2)
trueVal=accelerationFunction(16)

trueErr=abs(val-trueVal)
absoluteApproximateTrueError=trueErr*100/trueVal

print(str(absoluteApproximateTrueError)+'%')

tableData=iterate(velocity,backwardDifference,16,2,0.05,'delta T','acceleration')

print(tableData)

print(secondDerivativeEfficient(velocity,16,2))