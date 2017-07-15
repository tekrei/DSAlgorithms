'''
A gradient descent and linear regression example by Matt Nedrich
We are going to solve y = mx + b equation using gradient descent
m is slope, b is y-intercept

Source: http://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/
GitHub: https://github.com/mattnedrich/GradientDescentExample
'''
import numpy as np

def compute_error_for_line_given_points(b, m, points):
    '''
    Error function: Mean Squared Error (MSE) 
    MSE = (1/N)(sum((yi-(mxi+b))^2))
    '''
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

def step_gradient(b_current, m_current, points, learningRate):
    '''
    Gradient descent step
    Uses partial derivatives of each parameter (m and b) of the error function
    - learningRate variable controls how large of a step we take downhill during each iteration
     
    '''
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2 / N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    '''
    main runner of the gradient descent
    Calls steps of the gradient descent
    '''
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, np.array(points), learning_rate)
    return [b, m]

def run():
    #read data
    points = np.genfromtxt("data/data.csv", delimiter=",")
    #set learning rate
    learning_rate = 0.0001
    # starting guesses of the parameters
    initial_b = 0  # initial y-intercept guess
    initial_m = 0  # initial slope guess
    # number of iterations to perform the GD
    num_iterations = 1000
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))
    print "Running..."
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points))
    print "Linear Fit Equation -> y="+str(m)+"x+"+str(b)

if __name__ == '__main__':
    run()
