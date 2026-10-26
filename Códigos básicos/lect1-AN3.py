#-----Codigos Básicos de los conceptos teóricos---
#---Se harán en python porque los profesores lo piden asi--- 

"""The forward finite difference approximation of the derivative f'(x0) 
This is the slope of the secant crossing the graph of f at the points (x0, f(x0)) and (x0 +
h, f(x0 + h))"""

#codigo
def f(x):
2 y = x*np.sin(x)
3 return y
4 x0 = np.pi/2
5 h = 0.01
6 # approximation of the derivative using (8.1)
7 derivative = ( f(x0+h) - f(x0) ) / h
8 print('df(x) =',derivative, 'Error =',np.abs(derivative-1.0))
