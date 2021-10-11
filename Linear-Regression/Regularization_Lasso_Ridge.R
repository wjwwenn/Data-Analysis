# regularization to control regression coefficients
# reduce variance, decrease sample error

# install.packages('rsample')
# install.packages('AmesHousing')
# install.packages('tidyverse')
library(rsample)  # data splitting 
library(glmnet)   # regularized regression
library(dplyr)    # basic data manipulation
library(ggplot2)  # plotting
library(tidyverse)
library(AmesHousing)

# training (70%) and test (30%) sets
set.seed(123)
ames_split <- initial_split(AmesHousing::make_ames(), prop = .7, strata = "Sale_Price")
ames_train <- training(ames_split)
ames_test  <- testing(ames_split)

# fitting separately due to multicollinearity
lm(Sale_Price ~ Gr_Liv_Area, data = ames_train)
lm(Sale_Price ~ TotRms_AbvGrd, data = ames_train)

# target - dependent
# feature - independent
# log transform to reduce skewness
ames_train_x <- model.matrix(Sale_Price ~ ., ames_train)[, -1]
ames_train_y <- log(ames_train$Sale_Price)

ames_test_x <- model.matrix(Sale_Price ~ ., ames_test)[, -1]
ames_test_y <- log(ames_test$Sale_Price)

# dimension of feature (independent) matrix
dim(ames_train_x)

# Ridge regression
ames_ridge <- cv.glmnet(
  x = ames_train_x,
  y = ames_train_y,
  alpha = 0
)

plot(ames_ridge)
min(ames_ridge$cvm)       # minimum MSE
ames_ridge$lambda.min     # lambda for this min MSE

# lambdas applied to penalty parameter
ames_ridge$lambda %>% head()

# plot
coef(ames_ridge, s = "lambda.1se") %>%
  tidy() %>%
  filter(row != "(Intercept)") %>%
  top_n(25, wt = abs(value)) %>%
  ggplot(aes(value, reorder(row, value))) +
  geom_point() +
  ggtitle("Top influential variables") +
  xlab("Coefficient") +
  ylab(NULL)

# Lasso regression
ames_lasso <- cv.glmnet(
  x = ames_train_x,
  y = ames_train_y,
  alpha = 1
)
plot(ames_lasso)
min(ames_lasso$cvm)       # minimum MSE
ames_lasso$lambda.min     # lambda for this min MSE

# plot
coef(ames_lasso, s = "lambda.1se") %>%
  tidy() %>%
  filter(row != "(Intercept)") %>%
  ggplot(aes(value, reorder(row, value), color = value > 0)) +
  geom_point(show.legend = FALSE) +
  ggtitle("Influential variables") +
  xlab("Coefficient") +
  ylab(NULL)