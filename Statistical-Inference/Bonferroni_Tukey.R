# PAIRWISE COMPARISONS
# Bonferroni v.s. Tukey

library(MASS)
birthwt
# looking at mean and sd
tapply(birthwt$bwt, birthwt$race, mean)
tapply(birthwt$bwt, birthwt$race, sd)

# anova
a1 <- aov(birthwt$bwt ~ birthwt$race) 
summary(a1)
pairwise.t.test(birthwt$bwt, birthwt$race, p.adj = "none")

# bonferroni: divide original a-value/number of analyses on dependent variable
# for type-1 error (false positive; rejecting null hypothesis when you should not)
# adjustments leads to increased p-values "bonferroni correction"
# vulerable to type-2 error (false negative)
pairwise.t.test(birthwt$bwt, birthwt$race, p.adj = "bonf")
# holm
pairwise.t.test(birthwt$bwt, birthwt$race, p.adj = "holm")
# tukey (pairwise.t.test do not have Tukey)
Model=aov(ChickWeight$weight~ChickWeight$Diet)
TukeyHSD(Model)
T_result=TukeyHSD(Model)
plot(T_result, las=1 , col="red") #plot to show the situation
# reflect the 21 intervals
# title - 95% family-wise confidence interval

# tukey vs bonferroni
# tukey preferred when all pair-wise comparisons needed
# bonferroni ideal when objective is to compare certain "pairs"
# "Bonferroni has more power when the number of comparisons is small (conservative), 
# whereas Tukey is more powerful when testing large numbers of means."
# tukey needs parametric assumption; anova analysis - 1 result