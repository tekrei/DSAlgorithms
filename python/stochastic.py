'''
Created on May 15, 2015

@author: tekrei
Examples from Chapter 12 Stochastic Programs, Probability, and Statistics of 
Introduction to Computation and Programming Using Python
'''
import random, pylab

def CV(X):
    """Assumes that X is a list of numbers.
    Returns the coefficient of variation for X"""
    mean = sum(X) / float(len(X))
    try:
        return stdDev(X) / mean
    except ZeroDivisionError:
        return float('NaN')

def stdDev(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot / len(X)) ** 0.5  # Square root of mean difference

def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads / numFlips

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd) 

def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of ' + str(numFlips) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax - xmin) * 0.02, (ymax - ymin) / 2, 'Mean = ' + str(round(mean, 4)) + '\nSD = ' + str(round(sd, 4)))

def flipPlot(minExp, maxExp):
    """Assumes minExp and maxExp positive integers; minExp < maxExp
    Plots results of 2**minExp to 2**maxExp coin flips"""
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads / float(numTails))
        diffs.append(abs(numHeads - numTails))
            
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.rcParams['lines.markersize'] = 10
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(xAxis, diffs, 'bo')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis, ratios)

def makePlot(xVals, yVals, title, xLabel, yLabel, style, newFig=False, logX=False, logY=False):
    """Plots xVals vs. yVals with supplied titles and labels."""
    if newFig:
        pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()
        
def makeHistogramPlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins=20)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins=20)
    pylab.xlim(xmin, xmax)
    ymin, ymax = pylab.ylim()
    labelPlot(numFlips2, numTrials, mean2, sd2)


def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)

def flipPlot1(minExp, maxExp, numTrials):
    """Assumes minExp and maxExp ints; minExp < maxExp
    numTrials a positive integer
    Plots summaries of results of numTrials trials of
    2**minExp to 2**maxExp coin flips"""
    meanRatios, meanDiffs = [], []
    ratiosSDs, diffsSDs = [], []
    ratiosCVs, diffsCVs = [], []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads / float(numTails))
            diffs.append(abs(numHeads - numTails))
        meanRatios.append(sum(ratios) / float(numTrials))
        meanDiffs.append(sum(diffs) / float(numTrials))
        ratiosSDs.append(stdDev(ratios))
        ratiosCVs.append(CV(ratios))
        diffsSDs.append(stdDev(diffs))
        diffsCVs.append(CV(diffs))
    makePlot(xAxis, meanRatios, 'Mean Heads/Tails Ratios (' + str(numTrials) + ' Trials)', 'Number of flips', 'Mean Heads/Tails', 'bo', logX=True)
    makePlot(xAxis, ratiosSDs, 'SD Heads/Tails Ratios (' + str(numTrials) + ' Trials)', 'Number of Flips', 'Standard Deviation', 'bo', newFig=True, logX=True, logY=True)
    makePlot(xAxis, meanDiffs, 'Mean abs(#Heads - #Tails) (' + str(numTrials) + ' Trials)', 'Number of Flips', 'Mean abs(#Heads - #Tails)', 'bo', newFig=True, logX=True, logY=True)
    makePlot(xAxis, diffsSDs, 'SD abs(#Heads - #Tails) (' + str(numTrials) + ' Trials)', 'Number of Flips', 'Standard Deviation', 'bo', newFig=True, logX=True, logY=True)
    makePlot(xAxis, diffsCVs, 'Coeff. of Var. abs(#Heads - #Tails) (' + str(numTrials) + ' Trials)', 'Number of Flips', 'Coeff. of Var.', 'bo', newFig=True, logX=True)
    makePlot(xAxis, ratiosCVs, 'Coeff. of Var. Heads/Tails Ratio (' + str(numTrials) + ' Trials)', 'Number of Flips', 'Coeff. of Var.', 'bo', newFig=True, logX=True, logY=True)

def showErrorBars(minFlips, maxExp, numTrials):
    means, sds = [], []
    xVals, yVals = [], []
    exp = minFlips
    while exp <= maxExp:
        xVals.append(2 ** exp)
        fracHeads, mean, sd = flipSim(2 ** exp, numTrials)
        means.append(mean)
        sds.append(sd)
        exp += 1
    pylab.errorbar(xVals, means, yerr=2 * pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads (' + str(numTrials) + ')')
    pylab.xlabel('Number of flips')
    pylab.ylabel('Fraction of heads & 95% confidence')

if __name__ == '__main__':
    #for i in range(10):
    #    print i, flipSim(1000, 10)
    # flipPlot(4, 20)
    # flipPlot1(4, 20, 20)
    x = [random.randint(0, 25) for x in range(25)]
    print x, stdDev(x)
    random.seed(0)
    #makeHistogramPlots(100, 1000, 100000)
    showErrorBars(3, 10, 100)
    pylab.show()

"""
Law of large numbers (LLN): the average of the results obtained from a large number of trials should be 
close to the expected value, and will tend to become closer as more trials are performed.
 
Bernoulli trial (or binomial trial) is a random experiment with exactly two possible outcomes, "success"
and "failure", in which the probability of success is the same every time the experiment is conducted.
"""
