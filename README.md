
 In this portfolio I have collected and calculated some common cases which could occur or are
 otherwise interesting in finance world.                                                      

 
#1 In the first example I have insurance data, namely dates and claims costs for each day. 
Let us assume we can expect 100 claims to happen and we want to calculate, based on this data
what are the claim costs. First thought might be that we take 100 random costs from that 
data over and over again,say one million times which yields


<img src="https://raw.githubusercontent.com/ereekaur/finance/main/onemillion.png" width="500" height="500">

and the expected value is roughly 600k. However, this does not take account that the claim costs is a sample
from some distribution itself. It is convenient therefore to assume that the sample is from binomial distribution
with the success probability of non zero claims / all claims. This in turn yields the distribution



<img src="https://raw.githubusercontent.com/ereekaur/finance/main/totalcost.png" width="500" height="500">

which gives expected value roughly 223k. In insurance company we would be interested what premium we could
offer, say, with 99% confidence. In this case it would be 469k. If we want to put more weight on tails
we could use Cauchy distribution with expected value of 36, this gives 600k as 95% confidence value
which is a very extreme estimate. One could go further in analysis by replacing the discete distribution
of claim costs by a negative exponential function.



#2 In the second example I consider certain (imaginary) bonus classes in insurance companies and I will find out
how steep difference there should be between classes taking account the variance in order to maximize revenue.

#3 The third example considers how much certain crypto currency data deviates from Brownian motion. It is 
convenient to use logarithm differences. Here we have data of two different hours for ethereum currency, and
the histogram of logarithm differences are

<img src="https://raw.githubusercontent.com/ereekaur/finance/main/ETH1.png" width="500" height="500">
<img src="https://raw.githubusercontent.com/ereekaur/finance/main/ETH2.png" width="500" height="500">

The Shapiro-Wilkinson test gives different p-values so that the other hour seems to behave like 
Brownian motion and other does not. Let us now take a look at bitcoin data of last five years
and try to find a three month timeframe when the bitcoin behave mostly like a Brownian motion
and least like a Brownian motion. As there are 90 datapoints we will now use Kolmogorov test
in the place of Shapiro Wilkinson.





TODO:  

1) Add SL/XL -insurance analyses example
2) Try to simulate data in #1 using Panjer algorithm
3) What happens if the Poisson distribution in the example #1 is being replaced with Cauchy distribution
as it in some sense describes better the worst case scenario







