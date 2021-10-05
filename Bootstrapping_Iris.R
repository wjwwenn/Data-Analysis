# bootstrap - a method of inference about a population
# sampling with replacement
# estimate standard error, collect confidence interval (CI)
# iris: four measurements for 150 flowers of 3 species
head(iris)

B = 10000
x_bar_d = numeric(B)
sepal = iris$Sepal.Width
petal = iris$Petal.Width

# calculate sample mean (x_bar_d)
sepal_n = length(iris$Sepal.Width)
petal_n = length(iris$Petal.Width)
for (i in 1:B){
  sepal = mean(sample(sepal_n, replace=TRUE))
  petal = mean(sample(sepal_n, replace=TRUE))
  x_bar_d[i]=sepal-petal
}

# install.packages("moments")
hist(x_bar_d)
sd(x_bar_d)
moments::skewness(x_bar_d)
# negative skew = longer left tail
mean(x_bar_d)-(mean(sepal_n))-(mean(petal_n))
quantile(x_bar_d, c(0.025, 0.975))

# Evaluate bias of sample median
all_data=c(sepal, petal)
all_length=length(all_data)
B=10000
x_median=numeric(B)
for(i in 1:B){
  x_median[i]=median(sample(all_data, all_length, replace=TRUE))
}
bias = mean(x_median)-median(all_data)
# positive bias = sample median could be an overestimate 
# blue line is further right than the red line

hist(x_median)
abline(v=median(all_data),col="red", lty=2)
abline(v=mean(x_median), col="blue", lty=3)
text(x=12, y=3000, labels="avg. boostrap median", col="blue")
text(x=5, y=2500, labels="sample median", col="red")