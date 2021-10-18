# bootstrapping (1000 iterations) to simulate thesampling distribution of sample medians
# set seed value as 13
set.seed(13)
x = c(47, 47, 50, 47, 52, 45, 50, 53, 56, 49, 47, 43, 51)
n = length(x)
boot = numeric(1000)
for (i in 1:1000){
  bs = sample(x, n, replace=T)
  boot[i]=median(bs)
}
mean(boot)

# or
set.seed(13)
B = 1000
x_bar_d = numeric(B)
x = c(47, 47, 50, 47, 52, 45, 50, 53, 56, 49, 47, 43, 51)
x_n = length(x)
# calculate sample median (x_bar_d)
for (i in 1:B){
  calc = median(sample(x, replace=TRUE))
  x_bar_d[i]=calc
}
mean(x_bar_d) #mean of the sampling distribution

# misc calculations
hist(x_bar_d)
sd(x_bar_d)
moments::skewness(x_bar_d)
quantile(x_bar_d, c(0.025, 0.975))
