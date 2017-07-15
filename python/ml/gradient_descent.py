#!/usr/bin/python
# coding=utf-8
'''
A gradient descent and linear regression example by Matt Nedrich
We are going to solve y = mx + b equation using gradient descent
m is slope, b is y-intercept

Source: http://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/
GitHub: https://github.com/mattnedrich/GradientDescentExample
'''
import numpy
from utility import *

def compute_error(b, m, points):
    '''
    Error function: Mean Squared Error (MSE) 
    MSE = (1/N)(sum((yi-(mxi+b))^2))
    '''
    error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        error += (y - (m * x + b)) ** 2
    return error / float(len(points))

def step_gradient(b, m, points, l_rate):
    '''
    Gradient descent step
    Uses partial derivatives of each parameter (m and b) of the error function
    - learningRate variable controls how large of a step we take downhill during each iteration
    '''
    b_gradient = 0
    m_gradient = 0
    N = len(points)
    for i in range(0, N):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2.0 / N) * (y - ((m * x) + b))
        m_gradient += -(2.0 / N) * x * (y - ((m * x) + b))
    new_b = b - (l_rate * b_gradient)
    new_m = m - (l_rate * m_gradient)
    return [new_b, new_m]

def gd_runner(points, b0, m0, l_rate, n_iter):
    for i in range(n_iter):
        b0, m0 = step_gradient(b0, m0, numpy.array(points), l_rate)
    return [b0, m0]

def manual_gd(fd, x_old = 0, x_new = 5, learningRate = 0.1, precision = 0.00001):
    '''
    Created on May 18, 2015
    @author: tekrei
    A simple gradient descent usage for function optimization
    '''
    iteration = 0
    while abs(x_new - x_old) > precision:
        iteration+=1
        x_old = x_new
        x_new = x_old - (learningRate * fd(x_old))
    print "Local minimum occurs at", x_new, "iteration:",iteration

def f_derivative(x): return 2 * x + 2

def main():
    #read data
    points = load_numbers("data/data.csv")
    # starting guesses of the parameters
    b0 = 0  # initial y-intercept guess
    m0 = 0  # initial slope guess
    # number of iterations to perform the GD
    n_iter = 1000
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(b0, m0, compute_error(b0, m0, points))
    print "Running..."
    # points, starting y-intercept, slope, learning rate, number of iterations
    [b, m] = gd_runner(points, b0, m0, 0.0001, n_iter)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(n_iter, b, m, compute_error(b, m, points))
    print "Linear Fit Equation -> y={0}*x+{1}".format(m, b)
    manual_gd(f_derivative)
main()
