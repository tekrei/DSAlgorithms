#!/usr/bin/python
# coding=utf-8
'''
@author: tekrei
Linear Regression example from Introduction to Computation and Programming Using Python
'''
import numpy as np
import matplotlib.pyplot as plot
from scipy.stats import stats
from utility import *

def linear_fit_byhand(x_vals, y_vals):
    '''
    Calculate regression line using linear fit
    y = ax + b
    '''
    x_sum = sum(x_vals)
    y_sum = sum(y_vals)
    xy_sum = sum(x_vals*y_vals)
    xsquare_sum = sum(x_vals**2)
    count = len(x_vals)

    # y = ax + b
    # a = (NΣXY - (ΣX)(ΣY)) / (NΣX^2 - (ΣX)^2)
    a_value = (((count*xy_sum)-(x_sum*y_sum))/((count*xsquare_sum)-x_sum**2))
    # b =  (ΣY - b(ΣX)) / N 
    b_value = (y_sum-a_value*x_sum)/count 
    print a_value, b_value, x_vals
    est_yvals = a_value * x_vals + b_value
    print est_yvals
    # calculate spring constant
    k = 1 / a_value
    # plot regression line
    plot.plot(x_vals, est_yvals, label='Linear fit by hand, k = ' + str(round(k)) + ", RSquare = " + str(r_square(y_vals, est_yvals)))

def linregress(x_vals, y_vals):
    '''
    least-squares regression of scipy
    '''
    a_value, b_value, r_value, p_value, std_err = stats.linregress(x_vals,y_vals)
    est_yvals = a_value * x_vals + b_value
    k = 1 / a_value
    plot.plot(x_vals, est_yvals, label='Least-squares fit, k = ' + str(round(k)) + ", RSquare = " + str(r_value**2))

def linear_fit(x_vals, y_vals):
    '''
    Calculate regression line using linear fit
    y = ax + b
    '''
    a_value, b_value = np.polyfit(x_vals, y_vals, 1)
    est_yvals = a_value * np.array(x_vals) + b_value
    # calculate spring constant
    k = 1 / a_value
    # plot regression line
    plot.plot(x_vals, est_yvals, label='Linear fit, k = ' + str(round(k)) + ", RSquare = " + str(r_square(y_vals, est_yvals)))

def quadratic_fit(x_vals, y_vals):
    '''
    cubic fit
    ax^2+bx+c
    '''
    a_value, b_value, c_value = np.polyfit(x_vals, y_vals, 2)
    est_yvals = a_value * (x_vals ** 2) + b_value * (x_vals) + c_value
    plot.plot(x_vals, est_yvals, label='Quadratic fit, RSquare = ' + str(r_square(y_vals, est_yvals)))

def cubic_fit(x_vals, y_vals):
    '''
    cubic fit
    ax^3+bx^2+cx+d
    '''
    a_value, b_value, c_value, d_value = np.polyfit(x_vals, y_vals, 3)
    est_yvals = a_value * (x_vals ** 3) + b_value * (x_vals ** 2)
    est_yvals += c_value * x_vals + d_value
    plot.plot(x_vals, est_yvals, label='Cubic fit, RSquare = ' + str(r_square(y_vals, est_yvals)))

def printStatisticalSummary(x_vals,y_vals):
    print "Mean(x)="+str(np.mean(x_vals))," Mean(Y)="+str(np.mean(y_vals))
    print "Median(x)="+str(np.median(x_vals))," Median(Y)="+str(np.median(y_vals))
    print "StdDev(x)="+str(np.std(x_vals))," StdDev(Y)="+str(np.std(y_vals))
    print "Variance(x)="+str(np.var(x_vals))," Variance(Y)="+str(np.var(y_vals))
    print "Covariance(x,y)="+str(np.cov(x_vals, y_vals))
    print "Correlation(x,y)="+str(np.correlate(x_vals, y_vals))

def plot_data(vals):
    '''
    plot x and y values together with regression line
    '''

    x_vals = np.asarray([i[0]*9.81 for i in vals])
    y_vals = np.asarray([i[1] for i in vals])

    # plot measurement values
    plot.plot(x_vals, y_vals, 'bo', label='Measured displacements')
    plot.title('Measurement Displacement of Spring', fontsize='x-large')
    plot.xlabel('|Force| (Newtons)')
    plot.ylabel('Distance (meters)')
    linear_fit_byhand(x_vals, y_vals)
    linear_fit(x_vals, y_vals)
    linregress(x_vals, y_vals)
    quadratic_fit(x_vals, y_vals)
    cubic_fit(x_vals, y_vals)
    printStatisticalSummary(x_vals,y_vals)

def r_square(measured, estimated):
    '''
    measured: one dimensional array of measured values
    estimated: one dimensional array of predicted values
    returns coefficient of determination (R^2) using
    1 - EE/MV equation.
        EE: estimated error
        MV: variance of the actual data

    0<=r_square<=1
    r_square=1 -> the model explains all of the variability in the data
    r_square=0 -> there is no linear relationship
    '''
    estimated_error = ((estimated - measured) ** 2).sum()
    m_mean = measured.sum() / float(len(measured))
    m_variance = ((m_mean - measured) ** 2).sum()
    return 1 - (estimated_error / m_variance)

if __name__ == '__main__':
    plot_data(np.genfromtxt("data/spring.csv", delimiter=","))
    plot.legend(loc='best')
    plot.tight_layout()
    plot.show()
