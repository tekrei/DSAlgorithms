'''
Created on May 15, 2015

@author: tekrei
Plotting examples from Introduction to Computation and Programming Using Python
'''
import pylab

if __name__ == '__main__':
    principal = 10000  # initial investment
    interestRate = 0.05
    years = 20
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal += principal * interestRate
    pylab.plot(values, 'b-', linewidth=5)
    pylab.title('5% Growth, Compounded Annually', fontsize='xx-large')
    pylab.xlabel('Years of Compounding', fontsize='x-small')
    pylab.ylabel('Value of Principal ($)', fontsize='x-small')
    pylab.show()
