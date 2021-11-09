# Linear Regression of price against demand and price elasticity
# Monthly data between 2015-2021 for Japan, India, Malaysia
# Proven inelasticity of gasoline demand

# JAPAN 
# unit: KL 
data=read.csv(file.choose(),header=T)
demand_lm = lm(data$Gasoline~data$Gasoline.Price, data=data)
summary(demand_lm)

library(ggplot2)
ggplot(data = data, aes(y = data$Gasoline, x = data$Gasoline.Price)) + 
  geom_point(col = 'blue') + geom_smooth(method = 'lm', col = 'red', size = 0.5) # fitted regression line
#### as price increases 1 unit, quantity demand decreases by 7118 unit

# data$Gasoline estimate * (avg price/avg demand)
elasticity = -7118*(139.6482/4182401.9) # -0.237

# INDIA
# Unit: KBD
data=read.csv(file.choose(),header=T)
demand_lm = lm(data$Gasoline~data$Gasoline.Price, data=data) 
# 0.057213
summary(demand_lm)

library(ggplot2)
ggplot(data = data, aes(y = data$Gasoline, x = data$Gasoline.Price)) + 
  geom_point(col = 'blue') + geom_smooth(method = 'lm', col = 'red', size = 0.5) # fitted regression line
##### as price increases one unit, quantity demand increases by 5.8243 unit
elasticity = 5.8243*(77.58304/611.715) # 0.73868

# MALAYSIA
# Unit: KBD
data=read.csv(file.choose(),header=T)
demand_lm = lm(data$Gasoline~data$Gasoline.Price, data=data)
summary(demand_lm)

library(ggplot2)
ggplot(data = data, aes(y = data$Gasoline, x = data$Gasoline.Price)) + 
  geom_point(col = 'blue') + geom_smooth(method = 'lm', col = 'red', size = 0.5) # fitted regression line
# as price increase 1 unit, quantity demanded increases by 48.27 unit
elasticity = 48.27*(1.98/223.2743) # 0.4280
