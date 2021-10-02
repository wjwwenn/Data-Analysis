import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

# ordinary least squares (OLS/simple linear regression)
# set seed
np.random.seed(100)

n = 100
# evenly spaced numbers over interval
x = np.linspace(0, 10, 100)
#1D array to 2D array
X = np.column_stack((x, x ** 2))
beta = np.array([1, 0.1, 10])
e = np.random.normal(size=n)

# by default, statsmodels fitsa  line passing through the origin 
# i.e. does not fit an intercept
# add_constant to fit an intercept
X = sm.add_constant(X)
y = np.dot(X, beta) + e

model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

print("Parameters: ", results.params)
print("R2: ", results.rsquared)
print("Predicted values: ", results.predict())

# OLS with dummy variables
# modelling 3 groups using dummy variables
n = 50
groups = np.zeros(n, int)
groups[20:40] = 1
groups[40:] = 2

dummy = pd.get_dummies(groups).values
# evenly spaced numbers over interval
x = np.linspace(0, 20, n)
#1D array to 2D array
X = np.column_stack((x, dummy[:, 1:]))
# add_constant to fit an intercept
X = sm.add_constant(X, prepend=False)

beta = [1, 3, -3, 10]
# np.dot = product of vectors
y_true = np.dot(X, beta)
e = np.random.normal(size=n)
y = y_true + e

print(groups)
# 5 rows
print(dummy[:5, :])
results_dummy = sm.OLS(y, X).fit()
print(results_dummy.summary())

# plot
pred_ols2 = results_dummy.get_prediction()
independent_variable_lower = pred_ols2.summary_frame()["obs_ci_lower"]
independent_variable_upper = pred_ols2.summary_frame()["obs_ci_upper"]

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(x, y, "o", label="Data")
ax.plot(x, y_true, "b-", label="True")
ax.plot(x, results_dummy.fittedvalues, label="Predicted")
ax.plot(x, independent_variable_lower, "r--")
ax.plot(x, independent_variable_upper, "r--")
legend = ax.legend(loc="best")
