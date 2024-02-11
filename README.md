
Here I have studied different cases which I have encountered and which are related to optimization or financial world.

 
$\color{red} Example ~ 1$ In this example I have insurance data from three years, namely dates and claims costs from 68
different days. Let us assume we can expect 100 claims to happen next year and we want to calculate, based on the 
data given in claims.xlsx that what are the claim costs next year. First thought might be that we sum 100 random 
costs from the data over and over again, say, one million times. This yields the following distribution (left)

 


<p float="left" align= "center">
  <img src="https://raw.githubusercontent.com/ereekaur/finance/main/onemillion.png" width="300" height="300">
  <img src="https://raw.githubusercontent.com/ereekaur/finance/main/totalcost.png" width="300" height="300">
</p>


with the expected value ~600k. It is no coincidence that the graph looks normally distributed because of the central limit theorem.
However this approach does not take account that the claim costs is a sample from some distribution itself. It is therefore 
convenient to assume that the sample is from (for example) binomial distribution with the success rate of non zero claims / all claims. 
This in turn yields the distribution on the right-hand side above and  gives the expected value roughly 223k. In an insurance company we would
be interested in what premium we could offer, say, with 99% confidence. In this case it would be 469k without profit marginal. If we want to put
more weight on tails we could use Cauchy distribution with the expected value of 36 which gives 600k with 99% confidence which is a very extreme estimate. 
One could go further in analysis by replacing the discrete distribution of claim costs by a negative exponential function. It is notable that the linear 
regression in this case does not give any meaningful results; first of all, at year level there are too few data-points (though p-value is very small) to draw 
any conclusions and on the other hand if one wants to use all data points then the model is not useful since the time is not explanatory factor for one claim cost itself.

Yet another ubiquitous distribution, Weibull distribution, could be fitted to data for analysis. If we want to approach as in Bayes i.e. using the Weibull distribution as the prior
leads us into complex calculations but which we could overcome using fast fourier transform (FFT). A good candidate for prior is the gamma distribution since its conjugate is also a gamma distribution
and thus calculations will become simpler. Using Gamma(20,300) as a prior gives us the following posterior distribution:

<p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/bayesplot.png" width="300" height="300">
</p>


From here we can say with the confidence level of 99% that the total costs are less than 459332.7









$\color{red} Example ~ 2$ In this example I shall consider certain bonus classes in an insurance company and I will try to find out
how steep difference there should be between classes. From client point of view we want to minimize variance
between classes and maximize revenue from the company point of view. In what follows is that we have the following QP problem:

$$
\begin{align*}
&\text{minimize}  \quad \sum_{i=1}^6 a_i(c_i - \mu)^2 \\
\end{align*}
$$ 

but we can extend this into MOP problem via

$$
\begin{align*}
&\text{minimize}  \quad \sum_{i=1}^6 a_i(c_i - \mu)^2 \\
&\text{maximize}  \quad  \sum_{i=1}^6 a_ic_i \\
\text{s.t} \quad & \sum_{i=1}^6 a_i c_i = \mu
\end{align*}
$$ 

where $\mu$ is a predetermined average of the claim costs, c=(2, 1.5, 1, 0.9, 0.8, 0.6) and sixth class is the best bonus class, $a_i$ is the probability of being in class i. 
It is convenient to assume that claims occurence admits Poisson distribution; then we could have, for example the following transition matrix:

$$
\begin{bmatrix}
1 - e^{-\lambda} & 0 & e^{-\lambda} & 0 & 0 & 0 \\
1 - e^{-\lambda} & e^{-\lambda} & 0 & 0 & 0 & 0 \\
1 - (1 + \lambda)e^{-\lambda} & 1 - e^{-\lambda} & 0 & e^{-\lambda} & 0 & 0 \\
1 - \left(1 + \lambda + 0.5\lambda^2\right)e^{-\lambda} & 0 & 0 & 0 & e^{-\lambda} & 0 \\
1 - \left(1 + \lambda + 0.5\lambda^2\right)e^{-\lambda} & 1 - (1 + \lambda)e^{-\lambda} & \lambda e^{-\lambda} & 0 & 0 & e^{-\lambda} \\
1 - \left(1 + \lambda + 0.5\lambda^2\right)e^{-\lambda} & 1 - (1 + \lambda)e^{-\lambda} & \lambda e^{-\lambda} & 0 & 0 & e^{-\lambda}
\end{bmatrix}
$$

between bonus classes and we can calculate this Markov process' stationary point by calculating the eigenvector of the transpose of the 
transition matrix. If we choose the eigenvector which lies on the simplex we get the desired probability distribution $a$.






 
With weighting elements $\alpha$ and $\beta$ lets us try to formulate a well-defined problem 


$$
\begin{align*}
&\text{minimize}  \quad \alpha\sum_{i=1}^6 a_i(c_i - \mu)^2 - \beta\sum_{i=1}^6 a_ic_i \\
\text{s.t} \quad & \sum_{i=1}^6 a_i c_i = \mu, \qquad \alpha + \beta = 1.
\end{align*}
$$ 

For brevity let $\beta := 1-\alpha$. We thus reduced MOP problem back to QP problem. Let us solve it with python code

```python

import cvxpy as cp
import numpy as np

def solve_optimization_problem(a, mu, alpha):
    
    c = cp.Variable(len(a))

    # objective function
    objective = cp.Maximize(cp.sum(cp.multiply(a, c)))

    # constraints
    constraints = [cp.sum(cp.multiply(a, c)) == mu]

    prob = cp.Problem(objective, constraints)
    prob.solve()

    optimal_c = c.value

    return optimal_c

# example
a = np.array([0.2, 0.1, 0.05, 0.3, 0.15, 0.2]) 
mu = 10  
alpha = 0.5  # example value

optimal_c = solve_optimization_problem(a, mu, alpha)
print("Optimal values of c_i:", optimal_c)


```

which gives

```python
Optimal values of c_i: [ 8.95208668 15.0555552  25.32032479  6.60474165 11.10780715  8.95208668]
```
However finding a Pareto optimal solution for MOLP problem seems to be trivial, thus something has to be adjusted.




${\color{green} (to~ be ~continued)}$

$\color{red} Example  ~ 3$ This example considers how much certain crypto currency data deviates from Brownian motion. It is 
convenient to use logarithmic differences. Here we have data of two different hours for ethereum currency, and
the histogram of logarithmic differences are


<p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/ETH1.png" width="300" height="300">
<img src="https://raw.githubusercontent.com/ereekaur/finance/main/ETH2.png" width="300" height="300">
</p>

The Shapiro-Wilkinson test for normality shall be used here as sample size << 2000, and it gives different p-values so that the
other data seems to behave like  Brownian motion and other does not. It should be noticed that some care is needed when considering
normality tests, for example it might be a good idea to use the QQ-plot. Let us now take a look at bitcoin data of last  five years
and try to find a three month timeframe when the bitcoin behave mostly like a Brownian motion and least like a Brownian motion. 
We are lead to




Suppose now that we have an option to buy ethereum with the price p and the expire date is x and one can exercise it anytime before the date of
expiration i.e. the option is so called European option. For European call option it is well-known that the  Black-scholes formula

$$
\begin{equation}
 callOptionPrice = S(0) \varphi  \bigg{(} \frac{rt +{\color{orange}\sigma^2}\frac{t}{2} - log ( K/S(0))}{\sigma\sqrt{t}}\bigg{)}  -  K e^{-rt} \varphi \bigg{(}\frac{rt +{\color{orange}\sigma^2} \frac{t}{2} - log ( K/S(0))}{\sigma\sqrt{t}} \bigg{)}
\end{equation}
$$ 

gives the arbirtrage free price provided that data follows geometric brownian motion. Here
where K is the strike price, t is the exercise time, $\varphi$ is the normal distribution function $S(0)$ is the price at the time $t=0$ and  ${\color{orange}\sigma^2}$ is the variance.
However, it seems by the empirical data that data does not follow geometric brownian motion in general. There are also other models rather than normal distribution to use with 
logarithmic ratios. This leads to theory of so called Levy-processes whose characteristic function is


$$ \phi(u) = \exp\{it\left(i \alpha u - \frac{1}{2} \sigma^2 u^2 + \int_{-\infty}^{\infty} \(e^{iux} - 1 - \chi_{B(0,1)}            \right) \Pi(dx))\} $$

and the integral can be calculated using fast fourier transform.

One of these models is CGMY process (ADD)


$\color{red} Example ~ 4$ At certain poker site one can play a tournament format which consists of 30 players where the buy-in is 10$. Furthermore top five placements has a prize. 
In addition if you knock someone out of the tournament, you will get so called bounty prize; at the beginning  everyone has a bounty of worth 2.5$ which progressively
increases such that your own bounty increases with 0.5*(bounty of the dropped player) and you will win actual money same amount. If one wins the whole tournament one 
can keep his own bounty. Furthermore the chance of winning the jackpot worth 1050$ after knocking someone out is 1/1000. Suppose that some player is skilled in a way that
the prize vector (70, 23, 18, 15, 13, 0) corresponds to the probability vector  (3/100, 3/100, 4/100, 4/100, 4/100, 82/100). Moreover let us also define a random variable
$Y * 1.25 * 1.2^X$ describing the bounty prize where X and Y are random variables itself taking values from {1,2,3,4} uniformly and (4/20, 10/20, 3/20, 2/20, 1/20) contains 
the probabilities of  knocking out zero to four players, respectively. Is the player able to break-even in the described tournament with the given statistics ? After simulating 
one thousand times one thousand tournaments we get the following distribution:


<p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/totalearnings.png" width="400" height="400">
</p>


This graph tells us that the player is expected to lose 1200 dollars if he plays one thousand tournaments and break-even with the probability of 20%.




TODO:  

1) Add SL/XL -insurance analyses example
2) Try to simulate data in Example 1 using Panjer algorithm








