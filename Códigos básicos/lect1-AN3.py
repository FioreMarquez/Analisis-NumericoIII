#-----Codigos Básicos de los conceptos teóricos---
#---Se harán en python porque los profesores lo piden asi--- 

"""The forward finite difference approximation of the derivative f'(x0) 
This is the slope of the secant crossing the graph of f at the points (x0, f(x0)) and (x0 +
h, f(x0 + h))"""

#codigo
import numpy as np

def f(x):
  y = x*np.sin(x)
  return y
x0 = np.pi/2
h = 0.01
 # approximation of the derivative using the forward diferrence 
derivative = ( f(x0+h) - f(x0) ) / h
print('df(x) =',derivative, 'Error =',np.abs(derivative-1.0))

""" This approximation is called backward difference approximation and it is denoted by
Dbf(x0) = [f(x0) − f(x0 − h)]/h"""

#This formula can be implemented with the following simple code
x0 = np.pi/2
h = 0.01
 # approximation of the derivative using 
derivative = ( f(x0) - f(x0-h) ) / h
print('df(x) =',derivative, 'Error =',np.abs(derivative-1.0))

'''This result has the same accuracy as the forward finite difference approximation indicating
that the backward finite difference approximation is again first-order accurate'''

#---Second-order accurate finite difference approximations
"""This approximation of the first derivative will be denoted by
Dcf(x0) = [f(x0 + h) − f(x0 − h)]/2h

An implementation of the central finite difference approximation in Python for the same
f as before can be the following"""

#Codigo
x0 = np.pi/2
h = 0.01
derivative = (f(x0+h) - f(x0-h))/(2.0*h)
print('df(x) =',derivative, 'Error =',np.abs(derivative-1.0))


#Falta Richardson

