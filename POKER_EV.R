buy_in <- 10
simulate_tournament <- function() {
  num_players <- 30
  prize <- sample(c(35, 23, 18, 15, 13, 0), 1, prob = c(1/60, 2/60, 2/60, 2/60, 5/60, 18/19))
  total <- prize
  for (i in 1:sample(0:4, 1)) {
    jackpot <- sample(c(1500, 25000, 0), 1, prob = c(1/1000, 1/100000, 99899/100000))
    howmany <- sample(c(0,1,2,3,4), 1, prob = c(5/6, 1/12, 1/30, 1/25, 9/200))
    bounty <- howmany * 1.25 * 1.2^sample(1:4, 1)
    total <- total + jackpot + bounty
  }
  return(total - buy_in)
}

num_sims <- 1000

num_iterations <- 1000

earnings_matrix <- replicate(num_iterations, replicate(num_sims, simulate_tournament()))

total_earnings <- colSums(earnings_matrix)


hist(total_earnings, main = "Total earnings", xlab = "Total earnings", col = "orange", border = "black")
mean(total_earnings)
