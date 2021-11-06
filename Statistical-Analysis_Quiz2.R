########################  WEEK 6: SAMPLING DISTRIBUTIONS ##################### 
# Q1
# IID - Random sample, sample same distribution as population 

# Q2
x<-c(50,64,65,80,49,63,57)
min(x)
max(x)
mean(x)
median(x)
sd(x)
quantile(x,p=0.75)-quantile(x,p=0.25)

# Q3
length(ChickWeight$weight[ChickWeight$weight<100])
median(ChickWeight$weight[ChickWeight$Diet==2])

# Q4
View(USPersonalExpenditure) 
USPersonalExpenditure["Personal Care","1950"] 
USPersonalExpenditure[,"1950"]

# Q5
# (1) 
mean=(150+70+120+80+100)/5
# (2) 
mean=(-2+300+10+20+15)/5
# (3)
# total return
x <- c(-2,300,10,20,15)
quantile(x,p=0.75)-quantile(x,p=0.25)=10
sd(x)= 129.614
# IQR=10, SD=129.614

# For market capitalization, IQR is more robust to potential outliers.
y <- c(150,70,120,80,100)
quantile(y,p=0.75)-quantile(y,p=0.25)=40
sd(y)=32.09
# IQR=40, SD=32.09

# Q6
# 1) Q1: 25% of the observations are less than 54
# Q3: 75% of the observations are less than 78.
# (2) IQR=78-54=24
# (3) No outliers. See part 4 of this question. T 4his is because the maximum value in the sample is below the upper threshold we calculated (Q_3+1.5IQR), and that the minimum value is above the lower threshold we calculated (Q_1-1.5IQR). If there were values above or below these two threshold values (respectively), they would be identified as the outliers in the boxplot (the “*”)
# (4) Lower Limit: the supposedly theoretical lower limit is 54-1.5*24=18. This value is greater than the minimum 34. Since the minimum value is greater than the threshold (i.e., no unusually low values in our sample), we know we do not have outliers on the lower end. We will also use the minimum as our lower limit. In R, we can check this by using LL=max(54-1.5*24,min(X)), where X is the sample in this question (where you can create when given the data).
# Upper limit: the supposedly upper limit is 78+1.5*24=114. Since the maximum value is lower than this threshold (no unusually high values in our sample), we know we do not have outliers on the high end. We will also use the maximum as our upper limit. In R, we can check this by using, min(78+1.5*24,max(X))= 98, where X is the sample in this question (which you have to create in R if data are available). 

# 7.	Which index has the highest median? FTSE
# Highest IQR? SMI
# Lowest upper limit? CAC
# Lowest maximum? CAC

# WEEK 7: CENTRAL LIMIT THEOREM
# (1) PR (X <= 1.5)
pnorm()
pnorm(1.5, 1, sqrt(0.25))
# Use sqrt because pnorm() accepts 3rd value as SD
# Ans: 0.841

# (2)
# (x-1)/sqrt(0.25) = Z
# when X = 1.5, Z = 1.5-1/sqrt(0.25) = 1 
# X = 1.5, has the same probability as Z = 1.0

# (3)
# Pr(Z <= 1)
pnorm(1, 0, sqrt(1))

# P(Z ≥ 0.67) 
1-pnorm(0.67,0,sqrt(1)) # 0.25

# 3.
# (1)
1-pnorm(-1.85,0,1) 
# OR
1-pnorm(16,18,7/sqrt(42))
# Ans ≈0.9680 
# (2)
pnorm(-2.03,0,1) 
# OR
pnorm(16,17.5,7/sqrt(90))
# ≈0.0211

# 4.
# 7788*7788=60652944, 
# so the middle four digits are 
# 6529 6529*6529=42627841
# so the middle four digits are 6278 6278*6278=39413284
# so the middle four digits are 4132 
# The three random numbers are 6529, 6278 and 4132.

# 5. 
#(a)
set.seed(200)
x = runif(6)
x

#(b)
set.seed(300)
x = runif(3, 10, 20)

#(c)
x = runif(6, 10, 20)

# Q6.
# (1) 
for (i in 1:5) { 
  x=i^2
  print(x)
} 

# (2)
# x as piggy bank that you keep adding values (i.e. i^2) for 100 times
x<-0
for (i in 1:100){
  x=x+i^2}
x

# OR
x=c(1:100) 
x=x^2
sum(x)

# Q7.
# (1)
x_bar_3=rep(0,1000)
set.seed(1)
for (idx in 1:1000) {
  x_bar_3 [idx] =mean(rbinom(3,10,0.3)) }
hist(x_bar_3)

# (2)
x_bar_3=rep(0,1000)
for (idx in 1:1000) {
  set.seed(idx)
  x_bar_3 [idx] =mean(rbinom(3,10,0.3)) }
hist(x_bar_3)

########################  WEEK 7: CENTRAL LIMIT THEOREM ####################### 
# QUESTION 1
# (1) Pr (𝑋 ≤ 1.5) is given by 
pnorm(1.5,1,sqrt(.25))

# (2) Pr (𝑍 ≤ 1) is given by 
pnorm(1,0,sqrt(1))

# QUESTION 2
# P(𝑋7 ≥ 4.26) can be obtained as 
1-pnorm(4.26,4.18,0.84/sqrt(50))
# 0.25

# QUESTION 3
# (1)
# Average > 16,
# Sample mean = 18
# Sample SD = 7
# N = 42
# 1-pnorm(16,18,7/sqrt(42))
1-pnorm(-1.85,0,1) 
# ≈0.9680

# (2)
# Average < 16
# Sample mean = 17.5, sample SD = 7
# N = 90
pnorm(16,17.5,7/sqrt(90))
# ≈0.0211

# QUESTION 4
# 7788*7788=60652944, 
# so the middle four digits are 6529 6529*6529=42627841, 
# so the middle four digits are 6278 6278*6278=39413284, 
# so the middle four digits are 4132 
# The three random numbers are 6529, 6278 and 4132.

# QUESTION 5
# (A)
set.seed(200) 
x=runif(6)
x

# (B)
set.seed(300)
x=runif(3,min=10,max=20)

# (C)
set.seed(300)
x=runif(6,min=10,max=20)

# QUESTION 6 
# (1)
for (i in 1:5) { 
  x=i^2 
  print(x) 
} 

# (2)
for (i in 1:100) { 
  x[i] = i^2 
  y=sum(x) }
print(y)

# QUESTION 7
# (1)
x_bar_3=rep(0,1000)
set.seed(1)
for (idx in 1:1000) {
  x_bar_3 [idx] =mean(rbinom(3,10,0.3)) }
hist(x_bar_3)

# (2)
x_bar_3=rep(0,1000)
for (idx in 1:1000) {
  set.seed(idx)
  x_bar_3 [idx] =mean(rbinom(3,10,0.3)) }
hist(x_bar_3)

########################  WEEK 8: CONFIDENCE INTERVAL ####################### 
# Q1. Sample Mean = 106, Population SD = 15, N = 22
# (1)  90% CI
Z_95=qnorm(0.95,0,1) 
LL=106-Z_95*(15/sqrt(22)) 
UL=106+Z_95*(15/sqrt(22))
c(LL,UL) 
# THE 90% CONFIDENCE INTERVAL IS : [100.7397, 111.2603]

# (2) 99% CI
Z_995=qnorm(0.995,0,1) 
LL=106-Z_995*(15/sqrt(22)) 
UL=106+Z_995*(15/sqrt(22)) 
c(LL,UL)
# THE 99% CONFIDENCE INTERVAL IS [97.76, 114.24]
# 99% CI is wider than 90% CI. 
# A higher probability of correctness (i.e. CI captures the mean) would call for a wider interval.

# Q2. Mean = 7790, SD = 500, N = 22
# 99% CI 
Z_995=qnorm(0.995,0,1) 
LL=7790-Z_995*(500/sqrt(100)) 
UL=7790+Z_995*(500/sqrt(100)) 
c(LL,UL)
# THE 99% CONFIDENCE INTERVAL IS [7661.209, 7918.791]

# Q3. Mean = 11.5, SD = 9.2, N = 18
# Population SD unknown so use qt(CI, n-1)
# 95% CI
LL=11.5-9.2/sqrt(18)* qt(0.975,17) 
UL=11.5+9.2/sqrt(18)* qt(0.975,17) 
c(LL,UL)
# The 95% confidence interval is [6.92,16.08]

# Q4. 
# (1)
n=length(ChickWeight$weight[ChickWeight$Time==10]) 
x_bar=mean(ChickWeight$weight[ChickWeight$ Time==10])
S=sd(ChickWeight$weight[ChickWeight$ Time==10]) 
x_bar-S/sqrt(n)*qt(0.95,n-1)
# Ans: 102.0893 
x_bar+S/sqrt(n)*qt(0.95,n-1)
# Ans: 113.5842
# The 90% CI is [102.0893, 113.5842] grams

# (2) Population SD unknown, so use qt(CI, n-1)
n=length(ChickWeight$weight[ChickWeight$Time==0]) 
x_bar=mean(ChickWeight$weight[ChickWeight$Time==0]) 
S=sd(ChickWeight$weight[ChickWeight$Time==0]) 
x_bar-S/sqrt(n)*qt(0.975,n-1)
# 40.73821
x_bar+S/sqrt(n)*qt(0.975,n-1)
# 41.38179
# The 95% CI is [40.73821, 41.38179] grams

# Q5. Paper
# Q6. Paper

# Q7.
# (1)
q7=read.csv(file.choose(),header=T)
# The sample size is 149, which you could use either the 
# length command or View to find out. 
# Thus, the 95% CI is:
mean(q7$score)+qt(.975,148)*sd(q7$score)/sqrt(149)
# Ans: 71.86808
mean(q7$score)-qt(.975,148)*sd(q7$score)/sqrt(149)
# Ans: 68.58427

# The 99% CI is:
mean(q7$score)+qt(.995,148)*sd(q7$score)/sqrt(149) 
# [1] 72.3943
mean(q7$score)-qt(.995,148)*sd(q7$score)/sqrt(149)
# [1] 68.05805

# Including sample size = lowering range of values
# Confidence interval becomes smaller with more samples
# Greater accuracy

##################### WEEK 9: HYPOTHESIS TESTING ############################## 
# (1) PAPER
# (2)
# (3) Calculate rejection 
# alpha = 1
qnorm(0.01, 100, sqrt(25/35))

# type 2 error
1-pnorm(98.03, 97, sqrt(25/35))

# Q4.
# (1) 
95-100/(10/sqrt(16))

# (2) as z<0, p value=P(Z≤z)=P(Z≤-2) 
2*pnorm(-2,0,1)
# Ans: 0.046

# (3) 
# We reject the null hypothesis since the p-value 0.046 is less than the significance level 0.10. 
# Thus, at the 10% significance level, we conclude that the population mean differs from 100

# Q5.
# (1) 𝐻0:𝜇≤45, 𝐻1:𝜇>45
# (2) Sample mean = 47, Population SD = 8.5, Sample size = 36
z = 47-45/8.5(sqrt(36))
# (3) as z>0, p-value=P(Z≥z) = P(Z≥1.41)
# (4) Do not reject null hypothesis since p-value 0.079 is greater than 0.05. 
# At the 5% significance level, we cannot conclude that the population mean is greater than 45.

# Q6.
# (1) We reject H0 based on the sample. 
t.test(ChickWeight$weight[ChickWeight$Time==0],ChickWeight$weight[ChickWeight$Time==2])
# (2) We reject H0 based on the sample.
t.test(ChickWeight$weight[ChickWeight$Time==0])


# Q7.
# (1)
t_29=(mean(EuStockMarkets[1:30,"DAX"])- 1620)/(sd(EuStockMarkets[1:30,"DAX"])/sqrt(30)) 2.059383
# Thus, the p-value is 2*(1-pt(t_29,29))= 0.04853575

# (2)
t.test(EuStockMarkets[1:30,"DAX"],EuStockMarkets[31:60,"DAX"])
# We do not reject the null hypothesis that the two periods have equal means because the p-value = 0.3487>10%

# Q8.
# (1)
set.seed(123)
t.test(rnorm(30,13,1),rnorm(30,15,2))

# (2)
n=c(30, 500, 1000, 3000 )
set.seed(456) 
t.test(rnorm(n[1],13,1),rnorm(n[1],12.95,1)) 
t.test(rnorm(n[2],13,1),rnorm(n[2],12.95,1)) 
t.test(rnorm(n[3],13,1),rnorm(n[3],12.95,1)) 
t.test(rnorm(n[4],13,1),rnorm(n[4],12.95,1))
# The p-values are 0.6326, 0.156, 0.004113, and 0.001986. 
# Thus, for n=30 and 500, we do not reject H0. When n=1000 and 3000, we reject H0.

######################  WEEK 10: REGRESSION ANALYSIS ########################## 
# QUESTION 1
# Explain what it means by 
# (1) Using Ordinary least square (OLS) for coefficient estimation, 
# (2) the OLS estimates are statistics, and 
# (3) the “Everything-else-being-equal” condition when interpreting the coefficient.   

# (1) OLS coefficents are obtained by minimizing the sum of squares of prediction errors
# (i.e. prediction of Y - observed values of Y)
# OLS – finding the coefficients by gauging the least squared total of the errors. 
# It helps determine the best fit line to measure the linear regression formula.  

# (2) coefficients are a function of the random sample and therefore would change from sample to sample
# (3) "Everything-else-being-equal" helps to isolate a single factor when measuring the statistical significance 
# in the measurement of the regression model.  

# QUESTION 4 
# Estimated coefficient of "female", t-score, p-value
data=read.csv("/Users/jingwen/Desktop/AN6005 Foundation of Statistical Analysis/PPT's and data files/Week 10-Regression analysis 1/week10_scores.csv", header=TRUE)
summary(lm(data$score~data$female))

# The above result shows that 
# 1) the sample mean of female is -0.3357 points lower than the 
# sample mean of male students. 
# 2) that b1 is not statistically different from 0 (p-value is 0.926). 
# This roughly says E(score|female=1) is statistically no different 
# from E(score|female=0)=b0, which is about 74.05. 
# As such, we can conclude that we don’t reject 
# H0: μ_male=μ_female that the male and female students have the 
# same mean test score.    

# QUESTION 5
# (1)
# Indus as base group
install.packages("wooldridge")
library(wooldridge)
ceosal1
reg.results<-lm(salary~sales+finance+consprod+utility,data=ceosal1)
summary(reg.results)

# Residual standard error: 1336 on 204 degrees of freedom
# Multiple R-squared:  0.07097,   Adjusted R-squared:  0.05275 
# F-statistic: 3.896 on 4 and 204 DF,  p-value: 0.004517

# (3)
# Finance as base group
# (3) Since we use finance as baseline, omit in X 
reg.results1<-lm(salary~sales+consprod+utility+indus,data=ceosal1)
summary(reg.results1)

# QUESTION 6
# (1)
reg.results <-lm(bwght ~ cigs, data= bwght)
summary(reg.results)

# Residual standard error: 20.13 on 1386 degrees of freedom
# Multiple R-squared:  0.02273,   Adjusted R-squared:  0.02202 
# F-statistic: 32.24 on 1 and 1386 DF,  p-value: 1.662e-08

# (2)
# When cigs=0, predicted birth weight is 119.77 ounces. 
# When cigs=20, it reduces to 109.57

# (3) 
# If we want a predicted bwght of 125, 
# then cigs=(125-119.77)/(-0.51)≈-10.25, or about 
# -10 cigarettes. Obviously, -10 hardly makes any sense. 

# QUESTION 7
library(wooldridge)
reg.results <-lm(colgpa ~ hsperc + sat, data=gpa2)
summary(reg.results)

# Residual standard error: 0.5615 on 4134 degrees of freedom
# Multiple R-squared:  0.2734,    Adjusted R-squared:  0.2731 
# F-statistic: 777.9 on 2 and 4134 DF,  p-value: < 2.2e-16

# (2) Just plug these values into the equation:
#  (colgpa) ̂=1.392-0.0135×20+0.0015×1050=2.697
# (3) The difference between A and B is simply 140 times 
# the coefficient on sat, because hsperc is the same for both students. 
# So A is predicted to have a score 0.0015×140≈ 0.21 higher. 

# QUESTION 8
library(wooldridge)
reg.results <-lm(educ ~ sibs + meduc + feduc, data=wage2)
summary(reg.results)

# QUESTION 9 
ChickWeight$Diet
lm(weight~Time+Diet,data=ChickWeight) 

# (4)
ChickWeight$Time_factor= factor(ChickWeight$Time)
lm(weight~ Time_factor +Diet,data=ChickWeight)
ChickWeight

# OR (HANDY TIP)
lm(weight~ factor(Time) +Diet,data=ChickWeight)

######################  WEEK 11: REGRESSION ANALYSIS II ######################
# QUESTION 1
# (1) a 1% increase in income will lead to a 0.5% increase in predicted food expenditure. 
# (2) a $1 increase in income will lead to 5% (=0.05*100 %) increase in predicted food expenditure.

# QUESTION 2
# 2(1) When it is a right-skewed distribution, 
# the right side of the distribution is closer to the median while pushing the left section of median away.  
# (3) R-square value is the squared correlation coefficient between the fitted and actual values of the DV. 
# Thus, a higher R-square value implies a higher correlation between the fitted and actual values of the DV.
# /R-squared can help determine the correlation between the IVs and the DV

# QUESTION 3
skewness(kielmc$price)
# (1) skewness coefficient 1.13, right-skewed. Log transformation considered
# (2) 𝛽! > 0, since larger distance should increase the value of the property.
# (3) 
library(wooldridge)
reg1<-lm(log(price)~log(dist),data=kielmc) 
summary(reg1)
# A 1% increase in distance from the incinerator is associated with a predicted price that
# is about 0.32% higher.

# (4)
reg2<-lm(log(price)~log(dist)+log(area)+log(land)+rooms,data=kielmc)
summary(reg2)
# When the variables log(area),log(land),rooms are included, the coefficient on log(dist)
# becomes about 0.08 (t value ≈1.71 and p-value≈0.09). The effect is much smaller now, and statistically insignificant.

# The adjusted 𝑅" in the second model (0.496) is larger than the adjusted 𝑅" in the first model (0.1172). 
# The second model provides a better fit.

# QUESTION 4
set.seed(1)
library(moments)
skewness(apple$ecolbs)
library(wooldridge) 
reg1<-lm(ecolbs~ecoprc+regprc,data=apple)
summary(reg1)

######################  WEEK 12: SIMULATION ANALYSIS ######################
# 1(a)
x= c(3,-1,5,-2,7,-2,-2,5,10)
if(mean(x)>0){print("the sample mean is positive")} else
{print("the sample mean is non positive")} 

# (b) 
if(runif(1,-.1,1)>0){print ("x is positive")}

# (c) 
x= c(3,-1,5,-2,7,-2,-2, 5, 10)
if(mean(x)>median(x)){Y=1 } else {Y=0}

# QUESTION 2
# (1)
set.seed(200)
value=rep(0,6) 
contribution=c(1000,0,0,0,0)
for (year in 1:5){
  return=runif(1,min=-.03,max=.07) value[year+1]=(value[year]+contribution[year])*(1+return) }
value[6] 1166.572

# (2)
set.seed(200)
total_value= rep(0,100) contribution=c(1000,0,0,0,0)
for (sample_size in 1:100) {
  value=rep(0,6)
  for (year in 1:5){
    return=runif(1,min=-.03,max=.07)
    value[year+1]= (value[year]+contribution[year])*(1+return) }
  total_value[sample_size]= value[6] }
mean(total_value)
# 1102.889

# (3)
set.seed(200)
value=rep(0,6) contribution=c(1000,1000,1000,1000,1000)
for (year in 1:5){
  return=runif(1,min=-.03,max=.07) value[year+1]<-(value[year]+contribution[year])*(1+return) }
value[6]
5528.971

# (4)
set.seed(200)
value=rep(0,6) contribution=c(1000,1000,1000,1000,1000)
for (year in 1:5){
  return=runif(1,min=-.03,max=.07) value[year+1]<-(value[year]+contribution[year])*(1+return) }
value[6]
5528.971

# QUESTION 5
set.seed(200) 
total_policyvalue=rep(0,100) 
total_voucher =rep(0,100)
for (sample_size in 1:100) { 
  contribution=c(1000,1000,1000,1000,1000) 
  voucher=0
  policy_value=rep(0,6)
  voucher_value= rep(0,6) 
  return=runif(5,min=-.03,max=.07)
for (year in 1:5){
  if (return[year]>0) { 
    voucher =
    (policy_value[year]+contribution[year])*return[year]} else { voucher = 0}
  policy_value[year+1] = (policy_value[year]+contribution[year])*(1+return[year])- voucher
  voucher_value[year+1] =( voucher_value [year]+ voucher)
}
total_policyvalue[sample_size]= policy_value[6] 
total_voucher[sample_size]= voucher_value [6] }
mean(total_policyvalue) # 4937.827 
mean(total_voucher) # 362.5303

# QUESTION 6
mean=mean(total_voucher) 
sd=sd(total_voucher) 
LL=mean-qt(.975,99)*(sd/sqrt(100)) 
UL=mean+ qt(.975,99)*(sd/sqrt(100)) 
c(LL,UL) # 329.3887 395.6719

# QUESTION 7
# (1)
set.seed(200) totalunsold=rep(0,1000)
for (sample_size in 1:1000) {
  # Generate the hourly sales
  x=runif(10,3,5)
  if(sum(x)<=50){ totalunsold[sample_size]= 50- sum(x) } else {totalunsold[sample_size]=0}
}
mean(totalunsold) # 9.974903

# (2)
set.seed(200)
Days_stock_out=0
for (days in 1:100) {
  # Generate the hourly sales
  x=rnorm(10,4.5,1.5)
  if(sum(x)>50) {Days_stock_out= Days_stock_out+1} }
Days_stock_out
# 13 (days)
# Namely, the stall has a 0.13 probability of stock out (i.e., 13 out of 100).

# QUESTION 8
set.seed(200)
totaltime=rep(0,1000)
for (sample_size in 1:1000) {
  X=runif(1,3,5)
  Y=runif(1,0,4) totaltime[sample_size]= min(X,Y)
} mean(totaltime) # 1.980547