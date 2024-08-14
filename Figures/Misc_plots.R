# Misc plots
#
# Date updated:   2024-07-24
# Auhtor:         Christian Vedel 
# Purpose:        Misc plots to use in slides


# ==== Libraries ====
library(tidyverse)

# ==== Colours ====
cvcolors = list(
  blue = "#273a8f",
  green = "#2c5c34",
  red = "#b33d3d"
)

# ==== Load data ====
kaggle_survey = read_csv("Figures/kaggle_survey_2022_responses.csv", skip = 1) # Is in gitignore, but can be downloaded here: https://www.kaggle.com/competitions/kaggle-survey-2022/data

# ==== Make plot ====
capN = NROW(kaggle_survey)

# ==== Data cleaning ====
languages = kaggle_survey %>%
  select(
    starts_with("What programming languages do you use on a regular basis? (Select all that apply) - Selected Choice")
  ) %>%
  pivot_longer(cols = everything(), names_to = "question", values_to = "language") %>%
  drop_na(language) %>%
  group_by(language) %>%
  count() %>%
  mutate(
    pct = n / capN
  ) %>%
  arrange(desc(n)) %>% 
  ungroup()

frameworks = kaggle_survey %>%
  select(
    starts_with("Which of the following machine learning frameworks do you use on a regular basis? (Select all that apply) - Selected Choice")
  ) %>%
  pivot_longer(cols = everything(), names_to = "question", values_to = "framework") %>%
  drop_na(framework) %>%
  group_by(framework) %>%
  count() %>%
  mutate(
    pct = n / capN
  ) %>%
  arrange(desc(n)) %>% 
  ungroup()

# ==== Plots ====
p1 = languages %>%
  ggplot(aes(x = reorder(language, pct) , y = pct)) +
  geom_bar(stat = "identity", fill = cvcolors$red) +
  labs(
    title = "Usage of Programming Languages",
    x = "Programming Language",
    y = "Percentage",
    caption = "Kaggle Survey 2022 respondents."
  ) +
  theme_minimal() +
  coord_flip() + 
  scale_y_continuous(labels = scales::percent)

ggsave("Figures/languages.png", width = 8, height = 6, plot = p1, dpi = 600)


p1 = frameworks %>%
  ggplot(aes(x = reorder(framework, pct) , y = pct)) +
  geom_bar(stat = "identity", fill = cvcolors$green) +
  labs(
    title = "Usage of machine learning frameworks",
    x = "ML Frameworks",
    y = "Percentage",
    caption = "Kaggle Survey 2022 respondents."
  ) +
  theme_minimal() +
  coord_flip() + 
  scale_y_continuous(labels = scales::percent)

ggsave("Figures/frameworks.png", width = 8, height = 6, plot = p1, dpi = 600)
