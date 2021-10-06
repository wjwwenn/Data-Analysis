birthwt
# t-test
# alternative hypothesis: statistical difference between the two means
t.test(birthwt$bwt ~ birthwt$smoke, data = birthwt)
# wilcox test: nonparametric test comparing 2 paired groups
wilcox.test(birthwt$bwt ~ birthwt$smoke, data = birthwt)

# Hypothesis: t-test is a test comparing means, while Wilcoxon’s tests the ordering of the data. 
# For example, if you are analyzing data with many outliers such as individual wealth (where few billionaires can greatly influence the result), Wilcoxon’s test may be more appropriate.
# Interpretation: Although confidence intervals can also be computed for Wilcoxon’s test, 
# it may seem more natural to argue about the confidence interval of the mean in the t-test than the pseudomedian for Wilcoxon’s test.
# Fulfillment of assumptions: The assumptions of t-test may not be met for small sample sizes. 
# In this case, it is often safer to select a non-parametric test. 
# However, if the assumptions of the t-test are met, it has greater statistical power than Wilcoxon’s test.
# Wilcoxon-Mann-Whitney test tests equality of medians ONLY when the population shapes are identical. 
# This is what Fagerland & Sandvik refer to as the "pure shift" model 

# p.value, conf.int
names(birthwt.t.test)
birthwt.t.test$p.value 
birthwt.t.test$conf.int
conf.level <- attr(birthwt.t.test$conf.int, "conf.level") * 100

# Calculate difference in means between smoking and nonsmoking groups
birthwt.t.test$estimate

# alternative t-test
with(birthwt, t.test(x=birthwt$bwt[birthwt$smoke=="0"], 
                     y=birthwt$bwt[birthwt$smoke=="1"]))

# Boxplot below:
# https://www.andrew.cmu.edu/user/achoulde/94842/lectures/lecture07/lecture07-94842.html
# MASS - Modern Applied Statistics with S
# as_tibble: coerce lists/matrices into data frames
birthwt <- as_tibble(MASS::birthwt)

# Rename variables
birthwt <- birthwt %>%
  rename(birthwt.below.2500 = low, 
         mother.age = age,
         mother.weight = lwt,
         mother.smokes = smoke,
         previous.prem.labor = ptl,
         hypertension = ht,
         uterine.irr = ui,
         physician.visits = ftv,
         birthwt.grams = bwt)

# Change factor level names
birthwt <- birthwt %>%
  mutate(race = recode_factor(race, `1` = "white", `2` = "black", `3` = "other")) %>%
  mutate_at(c("mother.smokes", "hypertension", "uterine.irr", "birthwt.below.2500"),
            ~ recode_factor(.x, `0` = "no", `1` = "yes"))

# Boxplot for birthwt.grams varying between mother who smokes or not
qplot(x = mother.smokes, y = birthwt.grams,
      geom = "boxplot", data = birthwt,
      xlab = "Mother smokes", 
      ylab = "Birthweight (grams)",
      fill = I("lightblue"))