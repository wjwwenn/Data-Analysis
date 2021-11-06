######################### MOCK QUIZ 2020 ######################################
# Q1
# three fair dice rolled. at most one six appear
# ANS: 0.9259

# Q2
# F A B
# substance abuse. 
# what are the potential selection bias?
# average health of those people with recent substance abuse (F)
# - (A)
# the average health of those people without recent substance abuse history (B)

# Q3
# skewness coefficient = -0.074
# kurtosis coefficient = 3.499
# thin tails

# Q4 - evaluate independent/dependent statements 
# BBAB


# Q5
# qnorm(runif(1000),10,1) inverse transform algorithm?
# rnorm(1000,10,1)

# Q6
# variance of portfolio price = 0.5X1 + 0.5X2
# X1 and X2 - daily closing price

# (1)
price <- read.csv(file.choose(),header=T)
colnames(price)
price_a_w <- price[, -3]
price_a_m <- price[, -2]
price_w_m <- price[, -1]

# (2) risk
#apple and walmart
0.5^2*(var(price$apple) + var(price$walmart))
# apple and ms 
0.5^2*(var(price$apple) + var(price$microsoft))
# walmart and ms
0.5^2*(var(price$walmart) + var(price$microsoft))

# (3) expected closing price
0.5*mean(price$walmart) + mean(price$microsoft)

# Q7
# A - incorrect, B - correct
# Evaluate the following statements on RV
# B - a function that assigns numerical value to each outcome in sample space
# A - process that determines which outcome will be observed
# B - it has probability distribution that tells us about its values and corresponding prob
# A - diff outcomes cannot be assigned to same numerical value 

# Q8 Population vs Sample variance
# A - incorrect, B - correct
# B - makes the average sample variance = popn variance
# A - unbiasness of sample var as an estimator...
# A - when the sample size n is larger, high probability closer to mean...
# B - when the sample size larger, high probability closer to true value


# Q9
#f(x) = 0.1 for 5 <= x <= 10
#f(x)~N(10,0.9^2) for x >10
# inverse transform algorithm to estimate var X with 1000 observation
# N(a,b) normal distribution with mean a and var b
fx <- function (x){x*0.1}
integrate (fx, lower=5, upper=10)

n=1000
output=rep(0,n)

for(i in 1:n){
  spin=runif(1)
  if(spin<0.5){
    output[i]=qunif(spin, 5, 10)
  }
  else {
    output[i]=qnorm(spin, mean=10, sd=0.9)
  }
}

var(output)

# Q10
# E(X) = 750

# Q11 Kurtosis/Skew
# BJSales

# Q12 
# Pr(two girls // at least 1 girl)
(0.5/choose(4,2)*choose(4,1))

# Q13 
# Purpose of using counting method is to count total no. of events in sample space

# Q14
# Var[x] = E[X^2] - E[X^2]
# = 250 - 10^2 
#  = 150 

# Q15
# 4 fair coins flipped. Pr(2heads 2tails)
# Ans: 0.375

# Q16
choose(5,2)*(1/9)^2*(8/9)^3
# Ans: 0.0867

# Q17
var = 1

# Q19 You and 9 other students join a draw...
# Ans: 0.167

# Q20
# E(x) > E(x|y<60)
# E(x) < E(x|y>60) 


######################### MOCK QUIZ 2021 ######################################
# Q1
1/9*1/9*(8/9)^3*(choose(5,2   ))

(91/216)/2

choose(40,8)^5
choose(40,8) * choose(32,8) * choose(24,8) *choose(16,8)* choose(8,8)

# Q2
choose(5,2)*(1/9)^2*(8/9)^3

# Q3
6^3
choose(6,1)
6/216

# Q4
1/10/1/10
0.167*10

# Q7 - kurtosis and skewness
install.packages("moments")
library(moments)
BJsales
plot(density(BJsales))
hist(BJsales)
skewness(BJsales)
kurtosis(BJsales)

# Q9 
qnorm(runif(1000),10,1) 

# Q10
fx <- function(x){(exp(-x))}
integrate(fx, lower=0, upper=Inf)
var(1)

################################ CLONE QUESTIONS ##############################
################################  WEEK 1 ######################################
# 4 people tosses a coin
# If HT/TH, game ends
1-(0.5*0.5*0.5*0.5+0.5*0.5*0.5*0.5)

# 4 people tosses a coin
# If HT/TH, game ends
# If Pr(H) = 0.25
1-(0.25*0.25*0.25*0.25+0.75*0.75*0.75*0.75)

################################  WEEK 2 ######################################
#Q1: Class with 17, 24, 15 students; select 1 student in ? ways
17*24*15

#Q2: 20 members, select president and secretary
choose(20,1)*choose(19,1)

#Q3: 4 dice, Pr(at least 2 same numbers)
#Probability all 4 numbers are different
# First 2 dice: (6/6 * 1/6) = 1/6
(6/6) * (1/6) * (1/6) * (1/6) 
#Ans: 0.00462963

#Q4: 5 dice, Pr(5 diff no appear exactly once)
(6/6)*(5/6)*(4/6)*(3/6)*(2/6)
# Also able to: 6*5*4*3*2/6^5

#Q5: 4 passengers, 8 floors
#Probability that all four passengers get off at diff floors
8*7*6*5/8^4
# Also able to: 8/8 * 7/8 * 6/8 * 5/8 

#Q6: Committee of 8 people selected from a group of 10
#No. of diff group?
factorial(10)/(factorial(8)*factorial(2))
#OR
choose(10,8)

#Q7: 24 light bulbs, 2 defects
choose(24, 2)
# Probability(2 defects)=1/276

#Q8: Coin tossed 8 times. Pr(3 tails)
choose(8, 3)/2^8
# P(event) = No. of favorable outcomes/total no. of possible outcomes

#Q9: Coin tossed 8 times. Pr(<= 2 tails)
(choose(8, 0)+choose(8, 1)+choose(8, 2))/2^8

#Q10: 50 students divided into 5 class. 
# 10 students each.
# Award given to 5 students.
(choose(10,1))^5/choose(50,5)

#Q11/12
#A = draw with 1, 3, 5, 8, 12, 14
#B = one number drawn = 4 
#C = 1st no. drawn < 5
#ALL POSSIBLE SEQUENCES OF THE 6 NUMBERS

#No. of outcomes
factorial(20)/factorial((20-6))

#Pr(A)
factorial(6)/2790700

#Pr(B)
# P(19,5)/P(20,6)*6
(factorial(19)/factorial(5))/(factorial(20)/factorial(6))

#Pr(C)
# P19,5/P20,6*4=0.2
(factorial(19)/factorial(5))/(factorial(20)/factorial(6))

#Q11/12
#A = draw with 1, 3, 5, 8, 12, 14
#B = one number drawn = 4 
#C = 1st no. drawn < 5
#DIFFERENT COMBINATIONS OF 6 NUMBERS DRAWN FROM 20 NUMBERS

#No. of outcomes
choose(20,6)

#Pr(A)
1/choose(20,6)

#Pr(B)
choose(19,5)/choose(20,6)

#Q13/14
#Pr(stocks): 0.6
#Pr(bonds): 0.35
#Pr(own bonds if own stocks): 0.2
#Pr(own both securities) = 0.6*0.35 = 0.12
0.6*0.35

#Pr(own stocks // given that own bonds)
0.12/0.35
#(P(A intersect B))/P(B)

# Pr(late for work) = (40% x 5%) + (20% x 10%) + (30% x 45%) + (10% x 20%) = 0.195
# Pr(on time) = (0.4*0.95)+(0.2*0.9)+(0.3*0.55)+(0.1*0.8) = 0.805
# 0.2*0.1/0.195=0.1026
# Pr(late condition on using bicycle) = 0.2x0.1/p(A) 
# Pr(takes metro and arrive on time) = 0.1*0.8/0.805 
# (0.8)*0.1/0.1=0.8

################################  WEEK 3 ######################################
# Q1
# f(x)=  2/3 if x=0, f(x)=  1/3 if x=1, and f(x)=0 otherwise

# Q2
# f(x)=1/2 if x=0, f(x)=1/10 if x=1, f(x)=1/5 if x=2, f(x)=1/10 if x=3, f(x)=1/10 if x=3.5 and f(x)=0 otherwise.

# Q3 
# coin with probability 0.6 heads
dbinom(0:3,3,0.6)
barplot(dbinom(x,3,0.2), names.arg = x)

# Q4
# f(x) = cx, o for x = 1,... 3, otherwise
# 1/6

# Q5 20% defective. n sample. X=0 if non-defect.
# 5.	f(x)=0.2 if x=1, f(x)=0.8 if x=0, and f(x)=0 otherwise.

# Q6 Five coins flipped. Pr(2 heads, 3 tails)
dbinom(2,5,0.5)
dbinom(3,5,0.5)

# Q7 0.3 defective. Pr(3 items // at most 2 defect)
sum(dbinom(0:2,3,0.3))
dbinom(1,3,0.7)

# Q8(1) 50 people. 0.7 success. Pr(40 happy face)
dbinom(40,50,0.7)
# Ans: 0.039
# Q8(2) Pr(happy face btwn 40 and 45)
sum(dbinom(40:45,50,0.7))
# Ans: 0.079

# Q9(1) March 9 and March 29, Continuous UNIF
# Pr(tree does not bloom until 24 March)
1-punif(24,min=9,max=29)=0.25

# Q9(2) 
# Pr(tree will bloom by 20 March)
punif(20, 9, 29)

# Q9(3)
pnorm(0.09, 0.082, 0.053)-pnorm(0.05,0.082,0.053)

# Q10(1) 80% stocks, 20% bonds. 
# expected return: 8.2%, sd: 5.3%
# Pr(fund will generate return between 5% and 9%)
pnorm(0.09,0.082,0.053)-pnorm(0.05,0.082,0.053)
# Ans: 0.287

# Q10(2)
# lowest return of the fund for top 20% (80th percentile)
# of the distribution
qnorm(0.8,0.082,0.053)
# Ans: 0.1266

# Q11 deliveries between 1pm and 6pm daily
# Q11 (1) % deliveries after 3pm
1-punif(3, 1, 6)
# Q11 (2) % deliveries prior to 3.30pm
punif(3.5,1,6)
# Q11 (3) $ deliveries between 2pm and 2.30pm
punif(2.5,1,6)-punif(2,1,6)

# Q12 X follows standard normal distribution.
# Q12(1) Pr(-2<x<5)
pnorm(5, 0, 1)-pnorm(-2, 0, 1)
# Q12(2) Pr(x>1)
1-pnorm(1, 0, 1)

################################  WEEK 4 ######################################
# Q1 X Bernoulli. Pr(X=0)=q. E(x)?
# 0*q+1*(1-q)=1-q

# Q2 E(X)? X = sum of 2 fair dice roll 
x = c(2,3,4,5,6,7,8,9,10,11,12)
fx=c(1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36)
EX=sum(x*fx)
EX

# Q3 Appliance max lifetime 2 years. E(x)?
fx <- function(x){x*x/2}
integrate(fx, lower=0, upper=2)

# Q4 Product warranty 2 years. X = time which product fail
# Pr(x>=2)
fx1<- function(x){8/x^3}
integrate (fx1,2,Inf)$value

# Expected time to failure? E(x)?
fx2<- function(x){x*(8/x^3)}
integrate (fx2,2,Inf)$value

#OR
fx <- function(x){x*(8/x^3)}
integrate(fx, lower=2, upper=Inf)

# Q5 Integer 1-20 chosen at random, E(X)?
1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20
210/20

# Q6 E(x) = sum of (x * respective probabilities)
(18*10/50)+(19*20/50)+(20*10/50)+(21*5/50)+(25*5/50)

# Q7 E(X1) = E(X2) = E(X3) = 5
# E(3X1 - 2X2 + 4X3 - 5)?
3*5-2*5+4*5-5
# ANS: 20

# Q8
# (1) Var(X+Y)
5+4
# (2) Var(4X+2Y+5)
16*5 + 4*4

# Q9 RV with 5 values -1, 0, 1, 2, 5
# Var?
X = c(-1, 0, 1, 2, 5)
fx = rep(0.2, 5)
Xbar = sum(X*fx)
# var(X) #this gives sample variance, 
# NOT population variance
var_X = sum(fx*(X-Xbar)^2) # 4.24

# vector to store x
x <- c(-1,0,1,2,5)
# f(x) probability multiplied
z <- c(-1/5, 0, 1/5, 2/5, 1) 
# calculating mean
mean_z <- mean(z)

# (x - mean)^2
squared <- (z-(mean_z))^2
1/5*(squared)
sum(1/5*(squared))
1/5*sum(1/5*(squared))

mean(-1,2,3,6)
(-3.5+1)^2
1/6*36

# Q10(1) Pr(student gets B)
0.5-0.1

# Q10(2) Pr(student gets at least C)
1-0.1-0.1

# Q10(3) E(x) and SD
# E(x)=2.3, std=1.1
X = c(4, 3, 2, 1, 0)
Y = c(0.1, 0.4, 0.3, 0.1, 0.1)
EX = sum(X*Y)
var_X = sum(*(X-EX)^2)
var_X
EX
sqrt(var_X)

################################  WEEK 5 ######################################
Q1 <- read.csv(file.choose(),header=T)
View(Q1) 

# (1)	Pr(X=1)
sum(Q1$probabilities[Q1$x==1]) 
# Ans: 0.33

# (2)	Pr(Y≥2)
sum(Q1$probabilities[Q1$y>=2]) 
# Ans: 0.48

# (3)	Pr(X≤1 and Y≤1)
x <- sum(Q1$probabilities[Q1$x<=1])
y <- sum(Q1$probabilities[Q1$y<=1]) 
x*y
# Ans: 0.312

# (4)	Pr(X=Y)
sum(Q1$probabilities[Q1$x==Q1$y]) 
# Ans: 0.3

# (5)	Pr(X>Y)
sum(Q1$probabilities[Q1$x>Q1$y]) 
# Ans: 0.3

# Q2
Q2 <- read.csv(file.choose(),header=T)
View(Q2) 

# X = no. of members in household  
# Y = no. of cars owned by household 
Q2$probabilities = Q2$frequencies/200 
  
# (1)	What is the joint probability Pr(X=3,Y=0)?
sum(Q2$probabilities[Q2$x==3 & Q2$y==0]) 
# Ans: 0.015

# (2)	What is the marginal probability function f(X=3)?
sum(Q2$probabilities[Q2$x==3]) 
# Ans: 0.205

# (3)	What is the conditional probability function of Y given X=3?
P1=(Q2$probabilities[Q2$y==0 & Q2$x==3])/sum(Q2$probabilities[Q2$x==3]) 
P2=(Q2$probabilities[Q2$y==1 & Q2$x==3])/sum(Q2$probabilities[Q2$x==3]) 
P3=(Q2$probabilities[Q2$y==2 & Q2$x==3])/sum(Q2$probabilities[Q2$x==3]) 
P4=(Q2$probabilities[Q2$y==3 & Q2$x==3])/sum(Q2$probabilities[Q2$x==3]) 
#P1 = 0.0732
#P2 = 0.4878
#P3 = 0.3659
#P4 = 0.0732

# (4)	What is the conditional mean of Y given X=3?
#conditional expectation 
EY_X4=sum(c(0,1,2,3)*c(P1,P2,P3,P4)) 
EY_X4
# EY_X4 = 1.4390

# Q3 
# If X and Y are positively correlated, Var(X+Y) is larger than Var(X-Y)
# Var(X+Y) > Var(X-Y)

# Q4 
Covariance_x_y = 1*sqrt(10)*sqrt(5)
# Ans: 7.07
# Q4(1) Var(X+Y)
varX=10
varY=5
# ρ(X,Y)=1 >>> this means the correlation coefficient
# Q4(2) Var(3X-2Y+10)
(3^2)*10+(2^2)*5

9*10+4*5-12*7.07
# Ans: 25.16

# (Var X+Y)
15+(2*7.07)
# Ans: 29.14

# Var(3X-2Y+10) 
# formula: a^2 var(X) + b^2 var(y) + 2ab cov(x, y)
((3^2)*(varX) + (2^2)*(varY))-2(3)(2)(7.07)
# Ans = 25.16

# Q5 
# 10% took the test from school A
# average = 90
# 40% from school B 
# average = 85
# 50% from school C
# average = 75

ex = 0.1*90+0.4*85+0.5*75 
# Ans = 80.5 

########################## GROUP QUESTIONS ####################################
######### WEEK 3: GENERATING RV (INVERSE TRANSFORM METHOD) ####################
# Question 1
# Use R to implement the inverse transform algorithm to simulate
# for the distribution
# F(B) { 0, 1/3 , 1 for b < 0, 0<= b<1, 1<=b<Inf
v=list()
p=runif(1000,0,1)
for (i in p) {
  if (i>=0 & i<=1/3) {
    v=append(v,0)
  }
  else {
    v=append(v,1)
  }
}

# Question 2
# Use inverse transform algorithm to simulate a 
# standard normal distribution N(0,1)
v=list()
  p=runif(1000,0,1)
  for (i in p) {
    v <- append(v, qnorm(i))
  }
  
# Question 3
# Simulate f(x) = dnorm(x,0,1) if x < 0
# f(x) = 0.5 if 0 <= x <= 1, f(x) = 0 elsewhere
v=list()
  p=runif(1000,0,1)
  for (i in p) {
    if (i<=0.5) {
      v <- append(v, qnorm(i))
    }
    else {
      v <- append(v, qunif(2*(i-0.5)))
    }
  }
  
############ WEEK 4: PROPERTIES OF EXPECTATIONS [Kurtosis] ####################
# RANDOM SAMPLES, UNBIASED ESTIMATORS
# MEAN, VARIANCE, SKEWNESS, KURTOSIS
# Plot histograms for x and y in W4_Q1 
# (in the provided .R file) and 
# calculate their mean, std dev & skewness. 
# Compare the histograms and the statistics.
# Briefly comment on the differences between the two distributions 
# that can be explained by these statistics
hist(W4_Q1$x)
mean(W4_Q1$x)
sd(W4_Q1$x)
skewness(W4_Q1$x)
  
hist(W4_Q1$y)
mean(W4_Q1$y)
sd(W4_Q1$y)
skewness(W4_Q1$y)

# Plot the histograms for x and y in W4_Q2. 
# Which distribution do you think looks peakier?
# Q2) & Q3)

# Q2
hist(W4_Q2$x, col='red')
hist(W4_Q2$y, col='green')

# Q3
kurtosis(W4_Q2$x)
kurtosis(W4_Q2$y)
  
# Use kurtosis() to calculate the kurtosis of x and y. 
# Does kurtosis reflect your answer for 2)?  

# We can decompose the kurtosis into two terms: Peak and Tail (formula)
# Please complete this table below. 
# Calculate the “%” as (a)/kurtosis (or (b)/kurtosis).
# Examining the %. Which part (a) or (b) contribute more to kurtosis? 
# Use the results to conclude whether Kurtosis is a measure of tail or peak.

library(moments)
x_1=c() #creating empty vector for x peaks
x_2=c() #creating empty vector for x tails
y_1=c() #creating empty vector for y peaks
y_2=c() #creating empty vector for y tails

#sorting values of x into vectors
# if abs(x)<=1, sort into x_1 otherwise x_2
for (i in W4_Q2$x) {
  if (abs(i)<=1){
    x_1 <- c(x_1, i)
  } else { 
    x_2 <- c(x_2, i)
  }
}

# sorting values of y into vectors
# if abs(y)<=1, sort into y_1 otherwise y_2
for (i in W4_Q2$y) {
  if (abs(i)<=1){
    y_1 <- c(y_1, i)
  } else { 
    y_2 <- c(y_2, i)
  }
}

# Creating function for the kurtosis formula
my_kur_function <- function(i,ave,N,stddev){
  (sum((i-ave)^4)/N)/stddev^4
}

# x's Peak & %
avex=mean(W4_Q2$x)
Nx = ncol(t(W4_Q2$x))
sdx=sd(W4_Q2$x)
x_peak = my_kur_function(x_1,avex,Nx,sdx)
x_peak_pc = x_peak/kurtosis(W4_Q2$x)

# x's Tail & %
x_tail = my_kur_function(x_2,avex,Nx,sdx)
x_tail_pc = x_tail/kurtosis(W4_Q2$x)

# y's Peak & %
avey=mean(W4_Q2$y)
Ny = ncol(t(W4_Q2$y))
sdy=sd(W4_Q2$y)
y_peak = my_kur_function(y_1,avey,Ny,sdy)
y_peak_pc = y_peak/kurtosis(W4_Q2$y)

# y's Tail & %
y_tail = my_kur_function(y_2,avey,Ny,sdy)
y_tail_pc = y_tail/kurtosis(W4_Q2$y)

# Kurtosis a+b
x_a_b = x_peak + x_tail
y_a_b = y_peak + y_tail

############ WEEK 5: COUNTERFACTUALS AND CAUSAL EFFECTS #######################
set.seed(1000)

# Control Group
x1 = mean(rnorm(500,0,1))
Y0D0 = 10+x1
x2 = mean(rnorm(500,3,1))
Y1D0 = 10+x2

# Treatment
x3 = mean(rnorm(1000,0,1))
Y0D1 = 12+x3
x4 = mean(rnorm(1000,5,1))
Y1D1 = 12+x4

# Q2: 
Naive_Est = Y1D1 - Y0D0
ATT = Y1D1 - Y0D1
ATC = Y1D0 - Y0D0
ATE = (2/3)*ATT + (1/3)*ATC

# Q3:
Comparison = Naive_Est-ATE
# baseline bias - higher baseline for people in the treatment group 
# differential effect treatment bias 5 v.s. 3

ATE <- ATT1*2/3 + ATC1*1/3 #Calculate ATE as defined
ATE2 <- ATT2*2/3 + ATC*1/3
ATE1
ATE2
# We can obtain the same values from 2 different method. 

# Q4:
# This Naive estimate should be 4.1544, previously was 7+; this is much closer now
# Why is there still a bias? Since we used the method
# The naive estimate of 4.15422 changes after every experiment 
# as the sample changes

#Select 250 sample for Y0, considering that some might be under D1 distribution and some under D0 distribution
Y0=sample(c("D1","D0"), 250, replace=TRUE, prob = c(2/3, 1/3))
# Get random Y0 values based on the 250 samples generated above
Y0data=c()
for (i in 1:length(Y0)) {
  if (Y0[i] == "D0") {
    e = rnorm(1,0,1)
    x = 10+e
    Y0data[i] = x
  } else {
    e = rnorm(1,0,1)
    x = 12+e
    Y0data[i] = x
  }
}

#Select 250 sample for Y1, considering that some might be under D1 distribution and some under D0 distribution
Y1=sample(c("D1","D0"), 250, replace=TRUE, prob = c(2/3, 1/3))


# Get random Y1 values based on the 250 samples generated above
Y1data=c()
for (i in 1:length(Y1)) {
  if (Y1[i] == "D0") {
    e = rnorm(1,3,1)
    x = 10+e
    Y1data[i] = x
  } else {
    e = rnorm(1,5,1)
    x = 12+e
    Y1data[i] = x
  }
}

# Naive Estimate = EY1-EY0, assume base to be 0 since taken into account already
EY0=mean(Y0data)
EY1= mean(Y1data)
naive_est=EY1-EY0

######################## ONLINE STATISTICS TIPS ###############################
# ----- COMMON STATISTICS
# To find correlation between >= 2 variables
# cor(cbind(variable1, variable2,...variableX))
cor(cbind(chick$weight,chick$diet,chick$time))

# Median is used for descriptive purpose
# Stronger metric for central location, not affected by outliers
# For even number of samples, position of median = (n+1)/2
# e.g. [0, 1, 3, 7, 10, 15] Median position = 6+1/2 = 3.5
# 3.5th term = 7+3/2 = 5

# Mean is used for inference, statistical tractability
# Summation(X)/N
# Influenced by outlier data

# All statistical data are still statistics
# Different samples will give different values

# ----- BIVARIATE DISTRIBUTION
# If independent RV, f(x, y) = f(x)*f(y)
# Create probabilities column:
Cars$probabilities = cars$frequencies/100

# Plot marginal distribution
# (probability distribution of the variables contained in the subset)
Margin_x = rowsum(cars$probabilities, group = cars$x)

# ----- COVARIANCE AND CORRELATION
# Property 2: Var(ax+c) = a^2*Var(x)
# Property 3: Var(x1 + x2) = Var(x1) + Var(x2) if both independent (covariance = 0)
# P3.1: Var(x-y) = Var(x) + Var(y) - 2Cov(x,y)
# pXY meanX meanY = Cov(x, y)
#𝜌XY = Cov(X, Y)/(𝜎X*𝜎Y )

# Correlation does not tell why random variable changes
# Covariance of a random variable with itself
# Cov (X, X)=𝐸[(𝑋−𝜇𝑋 )(𝑋−𝜇𝑋 )]
# = Var(x) >= 0
# Must be positive, zero means that x has 1 entry only

# How to use Cor() and Cov()
# Cov(file name), Cor(file name)
# returns summary in table form
cor(trees)
cov(trees)
