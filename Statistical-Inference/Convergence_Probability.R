# CONVERGENCE IN PROBABILITY (with scatter plot)
# Population distribution = N(0, 1)
e=0.1 
n=1500 #sample size: 1:1500
# points for each sample size: 100

# form a matrix to have n as 1500 columns and 100 rows of sample values for each n
y=matrix(, nrow = 100, ncol = 1500) # Matrix[row,col]

set.seed(123)
for(i in 1:n){
  for(j in 1:100){
    sample=mean(qnorm(runif(i),0,1))
    y[j,i]=sample
  }
}

# convert matrix to dataframe, to plot with ggplot
install.packages("reshape2")
library(reshape2)
library(ggplot2)

long <- melt(y)
head(long)
plot(x=long$Var2,y=long$value, col = ifelse(long$value <0.1 & long$value >-0.1,'black','red'), xlab = "sample_size", ylab = "sample_means")
# Black shade is the threshold of [-0.1,0.1].
# As n increases, the red area becomes smaller because more points fall within the threshold

# test convergence by counting the number of data that exceeds 0 (parameter) with threshold of 0.1
# as the sample size increase, the number of error count decreases, hence probability should tend to 0 as n increases
prob=c()
for (i in 1:1500) {
  err_count=0
  
  for(j in 1:100) {
    if(abs(y[j,i])-0>e) {
      err_count=err_count+1
    }
  }
  prob[i]=err_count/100
}
plot(prob)
