buy_in <- 10


top_five_prizes <- c(35, 23, 18, 15, 13, 0)
top_five_probabilities <- c(3/100, 3/100, 4/100, 4/100, 4/100, 82/100)
simulate_tournament <- function() {
  num_players <- 30
  prize <- sample(top_five_prizes, 1, prob = top_five_probabilities)
  total <- prize
  
  for (i in 1:sample(0:4, 1)) {
    
    jackpot <- sample(c(1500, 25000, 0), 1, prob = c(1/1000, 1/100000, 99899/100000))
    howmany <- sample(c(0,1,2,3,4), 1, prob = c(5/6, 1/12, 1/25, 1/30, 9/200))
    bounty <- howmany * 1.25 * 1.2^sample(1:4, 1)
    total <- total + jackpot + bounty
  }
  return(total - buy_in)
}

num_sims <- 1000

earnings <- replicate(num_sims, simulate_tournament())

hist(earnings, main = "Total earnings", xlab = "Total earnings", col = "orange", border = "black")
mean(sum(earnings))
