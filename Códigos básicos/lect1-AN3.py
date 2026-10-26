#-----Codigos Básicos de los conceptos teóricos---
#---Se harán en python porque los profesores lo piden asi--- 

"""The forward finite difference approximation of the derivative f'(x0) 
This is the slope of the secant crossing the graph of f at the points (x0, f(x0)) and (x0 +
h, f(x0 + h))"""

#codigo
def f(x):
  y = x*np.sin(x)
  return y
x0 = np.pi/2
h = 0.01
 # approximation of the derivative using the forward diferrence 
derivative = ( f(x0+h) - f(x0) ) / h
print('df(x) =',derivative, 'Error =',np.abs(derivative-1.0))


