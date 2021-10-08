# Best OLS defined by minimizing the sum of squared residuals
# E(MSE) = sum of Variances, Squared bias, Irreducible errors

# GLOSSARY
# Glmnet: fits generalized linear and similar models via penalized maximum likelihood. 
# cv.glmnet: main function to do cross-validation
# alpha: elastic net mixing parameter, 𝛼∈[0,1]
# a = 1: lasso, a=0: ridge

# LASSO - Least Absolute Shrinkage and Selection Operator
# Shrinks the regression coefficients toward 0 by penalizing the regression model
# with a penalty term called L1-norm, which is the sum of the absolute coefficients

# RIDGE
# Shrinks the regression coefficients, so that variables, 
# with minor contribution to the outcome, have their coefficients close to zero
# with a penalty term called L2-norm, which is the sum of squared coefficients
# amt of penalty fine-tuned using constant called lambda.

# ELASTIC NET
# penalized with both L1-norm and L2-norm
# shrink coefficients (like ridge) and set coefficients to zero (like lasso)
# a hyperparameter “alpha” is provided to assign how much weight 
# is given to each of the L1 and L2 penalties.

install.packages("fastDummies")

# for reproducible results, if not lambda.min changes
set.seed(1) 

# used latin1 instead of UTF-8 encoding to load, if not file does not work
library(glmnet)
library(fastDummies)
sample1=read.csv("/Users/jingwen/Desktop/AN6005 Foundation of Statistical Analysis/PPT's and data files/Week 10-Regression analysis 1/Week 10 mini-lecture files/week10_credit.csv", header=TRUE, stringsAsFactors=FALSE, fileEncoding="latin1")

# create dummy variables for categorical variables
x=dummy_cols(subset(sample1,select=-c(Balance)), # subset to exclude Balance column
             select_columns = c("Gender","Student","Married", "Ethnicity"), 
                                remove_first_dummy = TRUE)
y=sample1[,"Balance"] # dependent variable

# removing categorical variables
x=subset(x,select = -c(Gender))
x=subset(x,select = -c(Student))
x=subset(x,select = -c(Married))
x=subset(x,select = -c(Ethnicity))

# cv.glmnet can fit ridge and LASSO regression, by selection the “alpha” value
# alpha = 1, 0; cv.glmnet is a general method (elastic net method)
lasso=cv.glmnet(as.matrix(x),y,alpha=1)
ridge=cv.glmnet(as.matrix(x),y,alpha=0)
cv1 <- lasso
cv0 <- ridge

lasso$cvm # y-axis 
lasso$lambda # horizontal axis x scale, not log transformed yet; lambda parameter, at which value is the best predicted value
lasso$lambda.min

# Extract the coefficients from lasso$glmnet.fit$beta, 
# based on the lambda value that gives the lowest MSE in the cv test (==lasso$lambda.min)
lasso$glmnet.fit$beta[,lasso$glmnet.fit$lambda==lasso$lambda.min]
ridge$glmnet.fit$beta[,ridge$glmnet.fit$lambda==ridge$lambda.min]

# (3) Plot and compare with $cvm and $lambda
# Cramér–von Mises criterion is a criterion used for judging the goodness of fit 
# of a cumulative distribution function 
# compared to a given empirical distribution function
par(mfrow = c(2,2))
plot(cv1); plot(cv0)
plot(log(cv1$lambda), cv1$cvm , pch = 19, col = "red",
     xlab = "log(Lambda)", ylab = cv1$name)
points(log(cv0$lambda) , cv0$cvm , pch = 19, col = "blue")
legend("topleft", legend = c("alpha = 1", "alpha = 0"),
       pch = 19, col = c("red","blue"))

# (4) Prediction
# fitted values for the first 10 observations at 𝜆=min
# lambda.min = lambda.min is the value of 𝜆 that gives minimum mean cross-validated error
predict(cv1, as.matrix(x[1:10,]), s = "lambda.min")
# lambda.1se is the value of 𝜆 that gives the most regularized model 
# such that the cross-validated error is within one standard error of the minimum.
predict(cv1, as.matrix(x[1:10,]), s = "lambda.1se")
