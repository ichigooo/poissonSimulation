# A taxi driver in the city of New York wants to decide how much time he should work per day to
# maximize his income. Assume that the average money per ride is p dollars. The number of trips he
# could fulll depends, of course, on how much time he works. If he works for t hours, the number of
# dispatches D he gets is a Poisson random variable with mean (t) = log(1 + t). In other words (as
# expected), the longer he works the more (on average) rides he gets.
# Also, the cost (fuel, car depreciation, etc) of working increases as the working time t increases. Let
# us assume here that there is a cost of $c for working per hour (half an our costs then c=2 etc.). If he
# chooses to work 3 hours, the total operating cost is 3c.

import numpy as np
from numpy.random import poisson

# Simulate the demand and estimate the expected net income through Monte Carlo
# for t = 0,1,2,...,10 hours of working amount

if __name__=="__main__":
    n_sim = 2000 # number of simulations for each t
    p = 12 # price per dispatch
    c = 3 # cost per working hour

    incomes = { t : 0.0 for t in range(11) } # the dictionary that stores
    # the simulated net income for each t
    for t in range(11):
        # For each t, simulate n_sim times, compute the net income for each
        # round of simulation and take the average of all rounds as the
        # estimated expected net income for that t.
        mu = np.log(1+t) # mean of the demand
        for i in range(n_sim):
            demand = poisson(lam=mu)
            incomes[t] += demand*p - c*t
        incomes[t] /= n_sim

    optimal_time = sorted(incomes.items(), key = lambda x: x[1],
            reverse=True)[0][0]

    print ("Optimal working amount is: ", format(optimal_time), "hours")
