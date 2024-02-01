
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

Yet another ubiquitous distribution, Weibull distribution, could be fitted to data for analysis. If we want to approach as in Bayes using it as the prior leads complex calculations but which
could overcome using FFT? Good candidate for finding posterior distribution is to use gamma distribution as prior since its conjugate is gamma as well and thus results are easy to achieve.








$\color{red} Example ~ 2$ In this example I shall consider certain bonus classes in a insurance company and I will try to find out
how steep difference there should be between classes in order to minimize variance
between classes. In what follows is that we have the following QP problem:

$$
\begin{equation}
min ~ \sum_{i=1}^6 a_i(c_i - \mu)^2, ~~\sum_{i=1}^6 a_i c_i = \mu \\
\end{equation}
$$

where $\mu$ is the predetermined average of the claim costs, c=(2, 1.5, 1, 0.9, 0.8, 0.6) and sixth class is the best bonus class if no claims occurred in 
three years, a_i is probability of being in class i. It is convenient to assume that claims admits Poisson distribution. Thus we get the transition matrix

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
transition matrix. If we choose the eigenvector which lies on the simplex we get the sought probability distribution. Let us now extend 
the QP problem into MOP problem, that is, we add another objective function. From the insurance company point of view we would like to
maximize revenue but author did not solve this problem yet.

$$
\begin{align*}
&\text{minimize}  \quad \alpha \sum_{i=1}^6 a_i(c_i - \mu)^2 + \beta\sum_{i=1}^6 a_i c_i \\
\text{wrt} \quad & \sum_{i=1}^6 a_i c_i = \mu \quad \quad\alpha + \beta = 1
\end{align*}
$$

$\color{red} Example  ~ 3$ This example considers how much certain crypto currency data deviates from Brownian motion. It is 
convenient to use logarithmic differences. Here we have data of two different hours for ethereum currency, and
the histogram of logarithmic differences are


<p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/ETH1.png" width="300" height="300">
<img src="https://raw.githubusercontent.com/ereekaur/finance/main/ETH2.png" width="300" height="300">
</p>

The Shapiro-Wilkinson test for normality shall be used here as sample size << 2000, and it gives different p-values so that the
other data seems to behave like  Brownian motion and other does not. It should be notice that some care is need when considering
normality tests, for example QQ-plot might be needed. Let us now take a look at bitcoin data of last  five years and try to find a 
three month timeframe when the bitcoin behave mostly like a Brownian motion and least like a Brownian motion. We are lead to




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


$\color{red} Example  ~ 5$ Optimization example. Suppose we have a sparse binary matrix containing information about watched movies meaning that
1 = watched and 0 = not watched. Our aim is to consider a problem of movie recommendation for certain user. Suppose that 100000 users have all liked
the same particular movie. Let A be a 100000 x 1000 matrix where $A_{ij}$ tells that user i has watched the movie j. Consider

$${\color{green}
\begin{equation*}
max ~c^t x \quad
Ax \leq b \quad
x \geq 0
\end{equation*}}
$$

 <p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/SPARSE.png" width="400" height="400">
  <em>100x100 block from the matrix A </em>
</p>


where c is a weight vector, b contains the maximum amount of movies we want to recommend. Note that in the case of square matrix it is well-known that the time complexity is at most polynomial as the
Gauss-Jordan method has the time complexity of $O(n^3)$. For solving rectangle systems the system is usually being transformed into equation form and then so called Simplex method is introduced in which at every
iteration step one checks the values at the vertices which are intersection points of the linear subspaces constructed from the constraints. There also exist so called interior point methods in which the convergence
towards to the solution is made within interior points. From the picture

<p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/SimplexVsHighs.png" width="400" height="400">
</p>

it comes clear that for our 100000 x 1000 matrix we would need ridiculous amount of time to solve the system using (revised) simplex method; interior point methods are more efficient. Here I used Python library called linprog and compared
the Highs and Revised simplex. For a 100000 x 1000 matrix the calculation using highs took roughly one minute. Can this be reduced further? As our matrix does not have any a priori structure to take advantage it might be good idea to 
consider matrix reordering i.e. find permutation of rows and columns which reduces fill-in when factorizing the system.








TODO:  

1) Add SL/XL -insurance analyses example
2) Try to simulate data in Example 1 using Panjer algorithm








