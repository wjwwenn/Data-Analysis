# Price Elasticity (year-on-year % change in retail price against demand data)
# Using quarterly data (compared with yearly/monthly) as R2 calculated in excel is better.
# useful to determine the effect of inflationary pressure on demand

library(moments)
library(ggplot2)
################################ INDIA ##################################
# Asia Price Elasticity_Quarterly.csv
data=read.csv(file.choose(),header=T)
demand_lm = lm(data$India.Demand~data$India.Price, data=data)
summary(demand_lm)
## coefficient estimate * (avg price/avg demand)
elasticity = -0.31056*(76/534) # -0.04419

ggplot(data = data, aes(y = data$India.Demand, x = data$India.Price)) + 
  geom_point(col = 'blue') + geom_smooth(method = 'lm', col = 'red', size = 0.5)

# NORMALITY TEST
hist(data$India.Price)
res.aov <- aov(data$India.Price~data$India.Demand)
summary(res.aov)
qqnorm(res.aov$residuals)
qqline(res.aov$residuals)
# ANOVA will not work as it is not normally distributed. 
# RECAP ANOVA

# skewness and kurtosis, should be around 0 and 3
skewness(data$India.Price) #-0.3410
kurtosis(data$India.Price) #2.4153

################################ THAILAND ##################################
demand_lm = lm(data$Thailand.Demand~data$Thailand.Price, data=data)
summary(demand_lm)
elasticity = -0.04150*(30/173) # -0.007196

ggplot(data = data, aes(y = data$Thailand.Demand, x = data$Thailand.Price)) + 
  geom_point(col = 'blue') + geom_smooth(method = 'lm', col = 'red', size = 0.5)

# NORMALITY TEST
hist(data$Thailand.Price)
res.aov2 <- aov(data$Thailand.Price~data$Thailand.Demand)
summary(res.aov2)
qqnorm(res.aov2$residuals)
qqline(res.aov2$residuals)

# skewness and kurtosis, should be around 0 and 3
skewness(data$Thailand.Price) #0.04
kurtosis(data$Thailand.Price) #2.386

################################ KOREA #####################################
demand_lm = lm(data$Korea.Demand~data$Korea.Price, data=data) 
summary(demand_lm)
elasticity = -0.194402*(1620/212) # -1.48552

ggplot(data = data, aes(y = data$Korea.Demand, x = data$Korea.Price)) + 
  geom_point(col = 'blue') + geom_smooth(method = 'lm', col = 'red', size = 0.5)

# NORMALITY TEST
hist(data$Korea.Price)
res.aov3 <- aov(data$Korea.Price~data$Korea.Demand)
summary(res.aov3)
qqnorm(res.aov3$residuals)
qqline(res.aov3$residuals)

# skewness and kurtosis, should be around 0 and 3
skewness(data$Korea.Price) #-0.03
kurtosis(data$Korea.Price) #2.308
