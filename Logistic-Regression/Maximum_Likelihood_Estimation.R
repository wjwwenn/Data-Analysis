# Maximum Likelihood Estimation (MLE)
library(ggplot2)
ICU <- read.csv(file.choose(),header=T)
Y <- week9_ICU$ICU
X <- week9_ICU$Age
N <- 40
p_vec <- c(0, 1)
par(las = 1, cex.lab = 1.2)
plot(X, y = dbinom(Y, prob = p_vec[1], size = N), type = "n", xlab = "Age of individual in ICU", ylab = "Probability", ylim = c(0, 1.0))
for (i in 1:length(p_vec)){
  points(X, y = dbinom(Y, prob = p_vec[i], size = N), col = i, type = "b",
         pch = 19, lty = 2)
}
Y <- ICU$ICU 
X <- ICU$Age 
LL= function(parameters){
  -sum(log((pnorm(parameters[1]+parameters[2]*X)^Y)*((1-pnorm(parameters[1]+parameters[2]*X))^(1-Y))))
}
library("DEoptim")
DEoptim::DEoptim(LL, lower = c(-100, -200), upper=c(100, 200),control = DEoptim.control(trace = FALSE))$optim

x = c()
y = c()
for (i in 25:100){ #between age 25 and 100
  x[i]=i
  y[i]=pnorm(-6.5390039+0.10157*i)
} 
x <- data.frame(x)
y <- data.frame(y)
df <- data.frame(c(x, y))
ggplot(df, aes(x, y)) +
  geom_point(na.rm=TRUE) + 
  ggtitle("Logit Model - Correlating Age with ICU Probability") + 
  xlab("Age")+ 
  ylab("Probability")
