
Here I have studied different cases which I have encountered and which are related to optimization or financial world

 
_EXAMPLE 1_  In the first example I have insurance data from three years, namely dates and claims costs from 68
different days. Let us assume we can expect 100 claims to happen next year and we want to calculate, based on the 
data  given in claims.xlsx that what are the claim costs next year. First thought might be that we sum 100 random 
costs from that data over and over again, say, one million times. This yields the following distribution (left)



<p float="left" align= "center">
  <img src="https://raw.githubusercontent.com/ereekaur/finance/main/onemillion.png" width="300" height="300">
  <img src="https://raw.githubusercontent.com/ereekaur/finance/main/totalcost.png" width="300" height="300">
</p>


with the expected value ~600k. It is no coincidence that the graph looks normally distributed because of the central limit theorem.
However this approach does not take account that the claim costs is a sample from some distribution itself. It is therefore 
convenient to assume that the sample is from (for example) binomial distribution with the success rate non zero claims / all claims. 
This in turn yields the distribution on the right-hand side above and  gives expected value roughly 223k. In insurance company we would
be interested in what premium we could offer, say, with 99% confidence. In this case it would be 469k without profit marginal. If we want to put
more weight on tails we could use Cauchy distribution with the expected value of 36 which gives 600k with 99% confidence which is a very extreme estimate. 
One could go further in analysis by replacing the discrete distribution of claim costs by a negative exponential function. It is notable that the linear 
regression in this case does not give any meaningful results; first of all, at year level there are too few data-points (though p-value is very small) to draw 
any conclusions and on the other hand if one wants to use all data points then the model is not useful since time is not explanatory factor for one claim cost itself.



_EXAMPLE 2_ In the second example I consider certain bonus classes in a insurance company and I will try to find out
how steep difference there should be between classes in order to minimize variance
between classes. In what follows is that we have the following QP problem:

$$
\begin{equation}
min ~ \frac{1}{N}\sum_{i=1}^N a_i(c_i - \mu)^2, ~~\sum_{i=1}^6 a_i c_i = M  ~~ \text{and} ~~  (c_i) ~\text{is a decreasing sequence}\\
\end{equation}
$$

where M is the average of the claim costs, a=(2, 1.5, 1, 0.9, 0.8, 0.6) and sixth class is the best bonus class if no claims occurred in 
three years. It is convenient to assume that claims admits Poisson distribution. Thus we get the following transition matrix between
bonus classes and we can calculate this Markov process stationary point by calculating the eigenvector of the transpose of the 
transition matrix. If we choose the eigen vector which lies on the simplex we get the distribution. Let us now extend the QP problem
into MOP problem namely add another objective function.


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




_EXAMPLE 3_ The third example considers how much certain crypto currency data deviates from Brownian motion. It is 
convenient to use logarithmic differences. Here we have data of two different hours for ethereum currency, and
the histogram of logarithmic differences are


<p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/ETH1.png" width="300" height="300">
<img src="https://raw.githubusercontent.com/ereekaur/finance/main/ETH2.png" width="300" height="300">
</p>

The Shapiro-Wilkinson test for normality shall be used here as sample size << 2000, and it gives different p-values so that the
other data seems to behave like  Brownian motion and other does not. Let us now take a look at bitcoin data of last 
five years and try to find a three month timeframe when the bitcoin behave mostly like a Brownian motion and least like 
a Brownian motion. We are lead to




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
logarithmic ratios. This leads to theory of so called Levy-processes whose caracteristic function is given by


$$ \phi(u) = \exp\{it\left(i \alpha u - \frac{1}{2} \sigma^2 u^2 + \int_{-\infty}^{\infty} \(e^{iux} - 1 - \chi_{B(0,1)}            \right) \Pi(dx))\} $$







One of these models is CGMY process


_EXAMPLE 5_ At certain poker site one can play a tournament format which consists of 30 players where the buy-in is 10$. In addition top five placements has a prize. 
In addition if you knock someone out of the tournament, you will get so called bounty prize; at the beginning  everyone has a bounty of worth 2.5$ which progressively
increases such that your own bounty increases with 0.5*(bounty of the dropped player) and you will win actual money same amount. If one wins the whole tournament one 
can keep his own bounty. Furthermore the chance of winning the jackpot worth 1050$ after knocking someone out is 1/1000. Suppose that some player is skilled in a way that
the prize vector (70, 23, 18, 15, 13, 0) corresponds to the probability vector  (3/100, 3/100, 4/100, 4/100, 4/100, 82/100). Moreover let us also define a random variable
Y * 1.25 * 1.2^X describing the bounty prize where X and Y are random variables itself taking values from {1,2,3,4} uniformly and (4/20, 10/20, 3/20, 2/20, 1/20) contains 
the probabilities of  knocking out zero to four players. Is the player able to break-even in the described tournament with the given statistics ? After simulating one thousand 
times one thousand tournaments we get the following distribution:


<p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/totalearnings.png" width="400" height="400">
</p>


This graph tells us that the player is expected to lose 1200 dollars if he plays one thousand tournaments and break-even with the probability of 20%.





_EXAMPLE 5_ Optimization example. Suppose we have a sparse binary matrix containing information about watched movies. Our aim is to consider the problem of movie recommendations. Suppose
that 20000 users have all liked the same movie. Let A be a 10000 x 1000 matrix where $A_{ij}$ tells that user i has watched the movie j
 
 
 <p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/SPARSE.png" width="400" height="400">
</p>


$$
\begin{equation*}
max ~c^t x \quad
Ax \leq b \quad
x \geq 0
\end{equation*}
$$

where c is a weight vector, b contains maximum amount of movies we want to recommend. Solving system like this calculating every feasible solution and taking maximum would take literally forever. Therefore
there has been an interest finding algorithms solving big systems with constraints. Note that in the case of square matrix it is well known that the time complexity is polynomial. But in the rectangle case
it is not so simple. Systems like this are calculated using so called simplex method which goes through edge points of xx dimensional in the R^nm space.
Solving this system in Python directly using REVISED simplex method took 187 seconds


TODO:  

1) Add SL/XL -insurance analyses example
2) Try to simulate data in Example 1 using Panjer algorithm








