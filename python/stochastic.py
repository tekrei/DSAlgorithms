"""
Created on May 15, 2015

Examples from Chapter 12 Stochastic Programs, Probability, and Statistics of
Introduction to Computation and Programming Using Python
"""

import random
from matplotlib import pyplot
import numpy as np


def CV(X: list) -> float:
    """Returns the coefficient of variation for X"""
    mean = sum(X) / float(len(X))
    try:
        return std_dev(X) / mean
    except ZeroDivisionError:
        return float("NaN")


def std_dev(X: list) -> float:
    """Returns the standard deviation of X"""
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot / len(X)) ** 0.5  # Square root of mean difference


def flip(flip_count: int) -> float:
    heads = 0.0
    for _ in range(flip_count):
        if random.random() < 0.5:
            heads += 1
    return heads / flip_count


def flip_sim(flips_per_trial: int, trial_count: int):
    heads_frac = []
    for _ in range(trial_count):
        heads_frac.append(flip(flips_per_trial))
    mean = sum(heads_frac) / len(heads_frac)
    sd = std_dev(heads_frac)
    return (heads_frac, mean, sd)


def label_plot(flip_count: int, trial_count: int, mean: float, sd: float):
    pyplot.title(str(trial_count) + " trials of " + str(flip_count) + " flips each")
    pyplot.xlabel("Fraction of Heads")
    pyplot.ylabel("Number of Trials")
    xmin, xmax = pyplot.xlim()
    ymin, ymax = pyplot.ylim()
    pyplot.text(
        xmin + (xmax - xmin) * 0.02,
        (ymax - ymin) / 2,
        "Mean = " + str(round(mean, 4)) + "\nSD = " + str(round(sd, 4)),
    )


def flip_plot(min_exp: int, max_exp: int):
    """Assumes min_exp and max_exp positive integers; min_exp < max_exp
    Plots results of 2**min_exp to 2**max_exp coin flips"""
    ratios = []
    diffs = []
    x_axis = []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for flip_count in x_axis:
        head_count = 0
        for _ in range(flip_count):
            if random.random() < 0.5:
                head_count += 1
        tail_count = flip_count - head_count
        ratios.append(head_count / float(tail_count))
        diffs.append(abs(head_count - tail_count))

    pyplot.title("Difference Between Heads and Tails")
    pyplot.xlabel("Number of Flips")
    pyplot.ylabel("Abs(#Heads - #Tails)")
    pyplot.rcParams["lines.markersize"] = 10
    pyplot.semilogx()
    pyplot.semilogy()
    pyplot.plot(x_axis, diffs, "bo")
    pyplot.figure()
    pyplot.title("Heads/Tails Ratios")
    pyplot.xlabel("Number of Flips")
    pyplot.ylabel("Heads/Tails")
    pyplot.plot(x_axis, ratios)


def make_plot(
    x_vals,
    y_vals,
    title,
    x_label,
    y_label,
    style,
    new_fig=False,
    log_x=False,
    log_y=False,
):
    """Plots x_vals vs. yVals with supplied titles and labels."""
    if new_fig:
        pyplot.figure()
    pyplot.title(title)
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.plot(x_vals, y_vals, style)
    if log_x:
        pyplot.semilogx()
    if log_y:
        pyplot.semilogy()


def histogram_plots(flip_count1, flip_count2, trial_count):
    val1, mean1, sd1 = flip_sim(flip_count1, trial_count)
    pyplot.hist(val1, bins=20)
    xmin, xmax = pyplot.xlim()
    ymin, ymax = pyplot.ylim()
    label_plot(flip_count1, trial_count, mean1, sd1)
    pyplot.figure()
    val2, mean2, sd2 = flip_sim(flip_count2, trial_count)
    pyplot.hist(val2, bins=20)
    pyplot.xlim(xmin, xmax)
    pyplot.ylim(ymin, ymax)
    label_plot(flip_count2, trial_count, mean2, sd2)


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
        xAxis.append(2**exp)
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
        log_x=True,
    )
    make_plot(
        xAxis,
        ratiosSDs,
        "SD Heads/Tails Ratios (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Standard Deviation",
        "bo",
        new_fig=True,
        log_x=True,
        log_y=True,
    )
    make_plot(
        xAxis,
        mean_diffs,
        "Mean abs(#Heads - #Tails) (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Mean abs(#Heads - #Tails)",
        "bo",
        new_fig=True,
        log_x=True,
        log_y=True,
    )
    make_plot(
        xAxis,
        diff_sds,
        "SD abs(#Heads - #Tails) (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Standard Deviation",
        "bo",
        new_fig=True,
        log_x=True,
        log_y=True,
    )
    make_plot(
        xAxis,
        diff_cvs,
        "Coeff. of Var. abs(#Heads - #Tails) (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Coeff. of Var.",
        "bo",
        new_fig=True,
        log_x=True,
    )
    make_plot(
        xAxis,
        ratio_cvs,
        "Coeff. of Var. Heads/Tails Ratio (" + str(trial_count) + " Trials)",
        "Number of Flips",
        "Coeff. of Var.",
        "bo",
        new_fig=True,
        log_x=True,
        log_y=True,
    )


def show_error_bars(min_flips: int, max_exp: int, trial_count: int):
    means, sds = [], []
    x_vals, _ = [], []
    exp = min_flips
    while exp <= max_exp:
        x_vals.append(2**exp)
        _, mean, sd = flip_sim(2**exp, trial_count)
        means.append(mean)
        sds.append(sd)
        exp += 1
    pyplot.errorbar(x_vals, means, yerr=2 * np.array(sds))
    pyplot.semilogx()
    pyplot.title("Mean Fraction of Heads (" + str(trial_count) + ")")
    pyplot.xlabel("Number of flips")
    pyplot.ylabel("Fraction of heads & 95% confidence")


if __name__ == "__main__":
    x = [random.randint(0, 1000) for _ in range(1000)]
    print(x, std_dev(x))
    random.seed(0)
    show_error_bars(3, 10, 100)
    pyplot.show()

"""
Law of large numbers (LLN): the average of the results obtained from a large number of trials should be 
close to the expected value, and will tend to become closer as more trials are performed.
 
Bernoulli trial (or binomial trial) is a random experiment with exactly two possible outcomes, "success"
and "failure", in which the probability of success is the same every time the experiment is conducted.
"""
