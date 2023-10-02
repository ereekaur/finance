suppressPackageStartupMessages({
  library(readxl)
  library(dplyr)
  library(ggplot2)
  library(survival)
})

d <- read_excel("claims.xlsx")
d <- rename(d, year = Year, cost = `Claim cost (€)`, date = `Claim date`)

yearly_inflation <- 2
ref_date <- min(d$date)
d <- mutate(d, 
            daydiff = as.numeric(date - ref_date) / 60 / 60 / 24,
            cost_discounted = cost / (1 + 0.01 * yearly_inflation * daydiff / 365))

n_vehicles <- tibble(year = 2018:2022, vehicles = c(1, 2, 87, 100, 100))
n_claims_per_year <- d %>%
  group_by(year) %>%
  summarise(n = n())


claim_prob <- sum(filter(n_claims_per_year, year %in% c(2020, 2021))$n)/ 
  sum(filter(n_vehicles, year %in% c(2020, 2021))$vehicles)

plt_claims <- ggplot(d, aes(x = cost)) +
  geom_histogram() +
  facet_wrap(~ factor(year))

plt_claims_total <- ggplot(d, aes(x = cost)) +
  geom_histogram()

plt_claim_scatter <- ggplot(d, aes(x = date, y = cost)) +
  geom_point()

# Total cost simulation.
nsim <- 1000000
totalcost <- vector("numeric", length = nsim)
nclaims <- rbinom(nsim, size = 100, prob = claim_prob)
for (i in 1:nsim) {
  costs <- sample(d$cost_discounted, nclaims[i], replace = TRUE)
  totalcost[i] <- sum(costs)
}

#Quantiles.
qs <- c(0.01, 0.025, 0.05, 0.25, 0.5, 0.75, 0.95, 0.975, 0.99)
quantile(totalcost * 1.02 ^ 4, qs) 
