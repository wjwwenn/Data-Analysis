# fixed and random effects models 
# correlation - or lack thereof
# fixed: capture the effects of all variables that don't change over time
# random: if two variables are not correlated 

# (In hierarchical (multilevel) modeling and econometrics, 
# the terms are defined quite differently: 
# fixed effects are estimated using least squares (or maximum likelihood) 
# random effects are estimated with shrinkage

import pandas as pd
# cross-sectional data, ignoring data with time/individual dimension
# panel/longitudinal/cross-sectional
from linearmodels import PanelOLS
from linearmodels import RandomEffects
from linearmodels.datasets import jobtraining
import statsmodels.tools.tools as sm
import statsmodels.formula.api as smf

data = jobtraining.load()
data
year = pd.Categorical(data.year)
data = data.set_index(['fcode', 'year'])
data['year'] = year
exog_variables = ['grant', 'sales']
exogenous = sm.add_constant(data[exog_variables])

# Random
mod = RandomEffects(data.clscrap, exogenous)
mod_fit = mod.fit()
print(mod_fit)

# Fixed - PanelOLS
# entity_effects: flag whether to include entity (fixed) effects in model
mod = PanelOLS(data.clscrap, exogenous, entity_effects=True)
mod_fit = mod.fit()
print(mod_fit)

# Mixed effects
# https://www.statsmodels.org/devel/mixed_linear.html
data = sm.datasets.get_rdataset("dietox", "geepack").data
data.head()
mixed = smf.mixedlm("Weight ~ Time", data, groups=data["Pig"]) 
mixed_fit = mixed.fit() 
mixed_fit.summary()