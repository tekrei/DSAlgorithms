"""
Created on May 15, 2015

Examples from Chapter 12 Stochastic Programs, Probability, and Statistics of 
Introduction to Computation and Programming Using Python
"""
import random
from matplotlib import pylab


def CV(X):
    """Assumes that X is a list of numbers.
    Returns the coefficient of variation for X"""
    mean = sum(X) / float(len(X))
    try:
        return std_dev(X) / mean
    except ZeroDivisionError:
        return float("NaN")


def std_dev(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot / len(X)) ** 0.5  # Square root of mean difference


def flip(flip_count):
    heads = 0.0
    for _ in range(flip_count):
        if random.random() < 0.5:
            heads += 1
    return heads / flip_count


def flip_sim(flips_per_trial, trial_count):
    heads_frac = []
    for _ in range(trial_count):
        heads_frac.append(flip(flips_per_trial))
    mean = sum(heads_frac) / len(heads_frac)
    sd = std_dev(heads_frac)
    return (heads_frac, mean, sd)


def labelPlot(flip_count, trial_count, mean, sd):
    pylab.title(str(trial_count) + " trials of " + str(flip_count) + " flips each")
    pylab.xlabel("Fraction of Heads")
    pylab.ylabel("Number of Trials")
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(
        xmin + (xmax - xmin) * 0.02,
        (ymax - ymin) / 2,
        "Mean = " + str(round(mean, 4)) + "\nSD = " + str(round(sd, 4)),
    )


def flip_plot(min_exp, max_exp):
    """Assumes min_exp and max_exp positive integers; min_exp < max_exp
    Plots results of 2**min_exp to 2**max_exp coin flips"""
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(min_exp, max_exp + 1):
        xAxis.append(2 ** exp)
    for flip_count in xAxis:
        head_count = 0
        for _ in range(flip_count):
            if random.random() < 0.5:
                head_count += 1
        tail_count = flip_count - head_count
        ratios.append(head_count / float(tail_count))
        diffs.append(abs(head_count - tail_count))

    pylab.title("Difference Between Heads and Tails")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Abs(#Heads - #Tails)")
    pylab.rcParams["lines.markersize"] = 10
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(xAxis, diffs, "bo")
    pylab.figure()
    pylab.title("Heads/Tails Ratios")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Heads/Tails")
    pylab.plot(xAxis, ratios)


def make_plot(
    x_vals, yVals, title, xLabel, yLabel, style, newFig=False, logX=False, logY=False
):
    """Plots x_vals vs. yVals with supplied titles and labels."""
    if newFig:
        pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(x_vals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()


def makeHistogramPlots(flip_count1, flip_count2, trial_count):
    val1, mean1, sd1 = flip_sim(flip_count1, trial_count)
    pylab.hist(val1, bins=20)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    labelPlot(flip_count1, trial_count, mean1, sd1)
    pylab.figure()
    val2, mean2, sd2 = flip_sim(flip_count2, trial_count)
    pylab.hist(val2, bins=20)
    pylab.xlim(xmin, xmax)
    pylab.ylim(ymin, ymax)
    labelPlot(flip_count2, trial_count, mean2, sd2)


def run_trial(flip_count):
    head_count = 0
    for _ in range(flip_count):
        if random.random() < 0.5:
            head_count += 1
    tail_count = flip_count - head_count
    return (head_count, tail_count)


def flip_plot1(min_exp, max_exp, trial_count):
    """Assumes min_exp and max_exp ints; min_exp < max_exp
    trial_count a positive integer
    Plots summaries of results of trial_count trials of
    2**min_exp to 2**max_exp coin flips"""
    mean_ratios, mean_diffs = [], []
    ratiosSDs, diff_sds = [], []
    ratio_cvs, diff_cvs = [], []
    xAxis = []
    for exp in range(min_exp, max_exp + 1):
        xAxis.append(2 ** exp)
    for flip_count in xAxis:
        ratios = []
        diffs = []
        for _ in range(trial_count):
            head_count, tail_count = run_trial(flip_count)
            ratios.append(head_count / float(tail_count))
            diffs.append(abs(head_count - tail_count))
        mean_ratios.append(sum(ratios) / float(trial_count))
        mean_diffs.append(sum(diffs) / float(trial_count))
        ratiosSDs.append(std_dev(ratios))
        ratio_cvs.append(CV(ratios))
        diff_sds.append(std_dev(diffs))
        diff_cvs.append(CV(diffs))
    make_plot(
        xAxis,
        mean_ratios,
        "Mean Heads/Tails Ratios (" + str(trial_count) + " Trials)",
        "Number of flips",
        "Mean Heads/Tails",
        "bo",
        logX=True,
    )
    make_plot(
        xAxis,
        ratiosSDs,
        "SD Heads/Tails Ratios (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Standard Deviation",
        "bo",
        newFig=True,
        logX=True,
        logY=True,
    )
    make_plot(
        xAxis,
        mean_diffs,
        "Mean abs(#Heads - #Tails) (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Mean abs(#Heads - #Tails)",
        "bo",
        newFig=True,
        logX=True,
        logY=True,
    )
    make_plot(
        xAxis,
        diff_sds,
        "SD abs(#Heads - #Tails) (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Standard Deviation",
        "bo",
        newFig=True,
        logX=True,
        logY=True,
    )
    make_plot(
        xAxis,
        diff_cvs,
        "Coeff. of Var. abs(#Heads - #Tails) (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Coeff. of Var.",
        "bo",
        newFig=True,
        logX=True,
    )
    make_plot(
        xAxis,
        ratio_cvs,
        "Coeff. of Var. Heads/Tails Ratio (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Coeff. of Var.",
        "bo",
        newFig=True,
        logX=True,
        logY=True,
    )


def show_error_bars(minFlips, max_exp, trial_count):
    means, sds = [], []
    x_vals, _ = [], []
    exp = minFlips
    while exp <= max_exp:
        x_vals.append(2 ** exp)
        _, mean, sd = flip_sim(2 ** exp, trial_count)
        means.append(mean)
        sds.append(sd)
        exp += 1
    pylab.errorbar(x_vals, means, yerr=2 * pylab.array(sds))
    pylab.semilogx()
    pylab.title("Mean Fraction of Heads (" + str(trial_count) + ")")
    pylab.xlabel("Number of flips")
    pylab.ylabel("Fraction of heads & 95% confidence")


if __name__ == "__main__":
    # for i in range(10):
    #    print i, flip_sim(1000, 10)
    # flip_plot(4, 20)
    # flip_plot1(4, 20, 20)
    x = [random.randint(0, 1000) for x in range(1000)]
    print(x, std_dev(x))
    random.seed(0)
    # makeHistogramPlots(100, 1000, 100000)
    show_error_bars(3, 10, 100)
    pylab.show()

"""
Law of large numbers (LLN): the average of the results obtained from a large number of trials should be 
close to the expected value, and will tend to become closer as more trials are performed.
 
Bernoulli trial (or binomial trial) is a random experiment with exactly two possible outcomes, "success"
and "failure", in which the probability of success is the same every time the experiment is conducted.
"""
