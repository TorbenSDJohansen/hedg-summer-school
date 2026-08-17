

# ==== Libraries ====
library(tidyverse)

# ==== Load data ====
stockholm = read_csv("Stockholm1920.csv")

# ==== Naive estimate ====
est1 = lm(log_labor_income ~ female_pred, data = stockholm)
summary(est1)
est1_w_se = summary(est1)$coefficients[2,1:2]

# ==== Gold standard ====
est2 = lm(log_labor_income ~ female, data = stockholm)
summary(est2)
est2_w_se = summary(est2)$coefficients[2,1:2]

# ==== Oracle ====
# The true gender wage gap parameter (if we had access to it)
est0 = -0.822
se = NA
est0_w_se = c(est0, se)

# ==== Showing results ====

# We gather all results in a data frame
all_estimates = rbind(
  est0_w_se,
  est1_w_se,
  est2_w_se
) %>%
  data.frame() %>% 
  mutate(
    method = c("0. Oracle", "1. Naive", "2. Only labeled"),
  )

# We estimate CI with +/- 1.96 * SE
all_estimates = all_estimates %>% 
  mutate(
    lower = Estimate - 1.96 * Std..Error,
    upper = Estimate + 1.96 * Std..Error
  )

# We plot the results
p1 = all_estimates %>% 
  ggplot(aes(x = Estimate, y = method)) +
  geom_point() +
  geom_errorbarh(aes(xmin = lower, xmax = upper), height = 0.2) +
  geom_vline(xintercept = est0, linetype = "dashed") + 
  theme_bw()

print(p1)
