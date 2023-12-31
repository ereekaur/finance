buy_in <- 10


top_five_prizes <- c(70, 23, 18, 15, 13, 0)
top_five_probabilities <- c(3/100, 3/100, 4/100, 4/100, 4/100, 82/100)


simulate_tournament <- function() {
  
  num_players <- 30
  prize <- sample(top_five_prizes, 1, prob = top_five_probabilities)
  total <- prize
  jackpot <- sample(c(1500, 0), 1, prob = c(1/1000, 999/1000))
  howmany <- sample(c(0,1,2,3,4), 1, prob = c(4/20, 10/20, 3/20, 2/20, 1/20))
  bounty <- howmany * 1.25 * 1.2^sample(1:4, 1)
  total <- total + jackpot + bounty
  
  return(total - buy_in)
  
}

num_sims <- 1000

earnings <- replicate(num_sims, simulate_tournament())

earnings_matrix <- replicate(1000, replicate(num_sims, simulate_tournament()) )
total_earnings <- colSums(earnings_matrix)

hist(total_earnings, main = "Total earnings", xlab = "Total earnings", col = "orange", border = "black")
mean(total_earnings)
quantile(total_earnings, probs = c(.8))
