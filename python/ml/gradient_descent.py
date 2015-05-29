'''
Created on May 18, 2015

@author: tekrei
A simple gradient descent usage for function optimization
Source: http://en.wikipedia.org/wiki/Gradient_descent#A_computational_example
'''

x_old = 0
x_new = 5 # The algorithm starts at x=5
learningRate = 0.1 # step size/learning rate
precision = 0.00001

#derivation of the function x**2+2x+1
def f_derivative(x): return 2 * x + 2

if __name__ == '__main__':
    iteration = 0
    while abs(x_new - x_old) > precision:
        iteration+=1
        x_old = x_new
        x_new = x_old - (learningRate * f_derivative(x_old))
    
    print "Local minimum occurs at", x_new, "iteration:",iteration