import numpy as np
import pandas as pd
import seaborn as sns
from scipy.optimize import minimize
import scipy.stats as stats
import statsmodels.api as sm

# 1. Define likelihood 
# 2. Natural log to sum function
# 3. Maximise/(minimise the negative) of function

# generate data
N = 120
# return evenly spaced numbers
x = np.linspace(0,30,N)
# np.random.normal - draw raw random samples from normal distribution
# loc = mean, scale = sd
ϵ = np.random.normal(scale = 10, size = N)
y = 3*x + ϵ
df = pd.DataFrame({"y":y, "x":x})
df[["constant"]] = 1
    
# plot
sns.regplot(df.x, df.y);

X = df[["constant", "x"]]
# fit model and summarize; OLE Regression Results
sm.OLS(y,X).fit().summary()

# define maximum likelihood
# why minimise? equivalent to maximising the log-likelihood/likelihood itself
# monotonic function
# log transform of the likelihood function makes it easier to handle (multiplication becomes sum)
# as magnitude of the likelihood can be very small
def MLE_Regression(para):
 intercept, beta, sd = para[0], para[1], para[2]
 y_hat = intercept + (beta*x) # prediction
 negative_log_likelihood = -np.sum(stats.norm.logpdf(y, loc=y_hat, scale=sd)) # PDF 
# return negative LL
 return(negative_log_likelihood)

guess = np.array([12,12,2])
# nelder-mead: simple search (minmize) of a function of a few variables
# not for use to find gradient
results = minimize(MLE_Regression, guess, method = "Nelder-Mead")
results

# probability - possible results
# likelihood - attached to hypothesis
