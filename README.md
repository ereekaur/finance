
Here I have collected and calculated some common cases which could occur or are
 otherwise interesting in finance world.                                                      

 
_EXAMPLE 1_  In the first example I have insurance data from three years, namely dates and claims costs from 68
different days. Let us assume we can expect 100 claims to happen next year and we want to calculate, based on the 
data  given in claims.xlsx that what are the claim costs next year. First thought might be that we sum 100 random 
costs from that data over and over again, say, one million times. This yields the following distribution (left)



<p float="left" align= "center">
  <img src="https://raw.githubusercontent.com/ereekaur/finance/main/onemillion.png" width="300" height="300">
  <img src="https://raw.githubusercontent.com/ereekaur/finance/main/totalcost.png" width="300" height="300">
</p>


with the expected value ~600k. It is no coincidence that the graph looks normally distributed (central limit theorem).
However this approach does not take account that the claim costs is a sample from some distribution itself. It is therefore 
convenient to assume that the sample is from (for example) binomial distribution with the success rate non zero claims / all claims. 
This in turn yields the distribution on the right-hand side above and  gives expected value roughly 223k. In insurance company we would
be interested in what premium we could offer, say, with 99% confidence. In this case it would be 469k without profit marginal. If we want to put
more weight on tails we could use Cauchy distribution with the expected value of 36 which gives 600k with 99% confidence which is a very extreme estimate. 
One could go further in analysis by replacing the discrete distribution of claim costs by a negative exponential function. It is notable that linear 
the regression here does not give any meaningful results; first of all at year level there are too few data-points (though p-value is very small) to draw 
any conclusions and on the other hand if one wants to use all data points then the model is not useful since time is not explanatory factor for one claim cost itself.



_EXAMPLE 2_ In the second example I consider certain (imaginary) bonus classes in insurance companies and I will find out
how steep difference there should be between classes taking account the variance in order to maximize revenue.



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
expiration i.e. the option is so called American option. We want to find an optimal price for that option with Black-scholes formula.
One needs the assumption that the data follows the geometric Brownian motion; however it turns out that in reality this does not happen often.
There are also other models rather than normal distribution to use with logarithmic ratios. This leads to theory of so called 
Levy-processes. One of these models is CGMY process


_EXAMPLE 5_ Certain poker company has a 30 player variant tournament with 10$ buy-in where top five placements being paid. In addition if you 'knock out'
someone during the tournament, you will get so called bounty prize; at the beginning  everyone has a bounty of worth 2.5$ which progressively increases such that your 
own bounty increases with 0.5*(bounty of the dropped player) and you will win half of the bounty of the dropped player. Furthermore with the chance of 1/1000
you can win a jackpot worth 1500$ and with the chance of 1/100000 you can win 25000$. Suppose that the player is a skilled in a way that the vector (35, 23, 18, 15, 13, 0)
corresponds to the probabilities  (1/100, 2/100, 3/100, 4/100, 8/100, 82/100) being placed 1 to 5 places and the tuples last element tells that you are placed 6-30 with the 
probability of 82/100. Moreover let us also define randomvariable Y * 1.25 * 1.2^X describing bounty prize where X and Y are random variables itself taking values from {1,2,3,4}
equally. Can the player with above statistics break-even in this variant? With the above information we can simukate and get the following distribution of earnings in 1000 games:


<p float="left" align= "center">
 <img src="https://raw.githubusercontent.com/ereekaur/finance/main/earnings.png" width="400" height="400">
</p>

which gave the mean -578$.





_EXAMPLE 5_ Portfolio selection problem: 




TODO:  

1) Add SL/XL -insurance analyses example
2) Try to simulate data in Example 1 using Panjer algorithm








