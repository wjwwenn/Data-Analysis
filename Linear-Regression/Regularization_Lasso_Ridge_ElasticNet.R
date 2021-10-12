# regularization to control regression coefficients
# reduce variance, decrease sample error
# using GLMNET; other packages include caret and h20

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

# Elastic Net
lasso    <- glmnet(ames_train_x, ames_train_y, alpha = 1) 
elastic1 <- glmnet(ames_train_x, ames_train_y, alpha = 0.25) 
elastic2 <- glmnet(ames_train_x, ames_train_y, alpha = 0.75) 
ridge    <- glmnet(ames_train_x, ames_train_y, alpha = 0)

# maintain the same folds across all models
fold_id <- sample(1:10, size = length(ames_train_y), replace=TRUE)

# search across a range of alphas
tuning_grid <- tibble::tibble(
  alpha      = seq(0, 1, by = .1),
  mse_min    = NA,
  mse_1se    = NA,
  lambda_min = NA,
  lambda_1se = NA
)

for(i in seq_along(tuning_grid$alpha)) {
  # fit CV model for each alpha value
  fit <- cv.glmnet(ames_train_x, ames_train_y, alpha = tuning_grid$alpha[i], foldid = fold_id)
  
  # extract MSE and lambda values
  tuning_grid$mse_min[i]    <- fit$cvm[fit$lambda == fit$lambda.min]
  tuning_grid$mse_1se[i]    <- fit$cvm[fit$lambda == fit$lambda.1se]
  tuning_grid$lambda_min[i] <- fit$lambda.min
  tuning_grid$lambda_1se[i] <- fit$lambda.1se
}

tuning_grid

tuning_grid %>%
  mutate(se = mse_1se - mse_min) %>%
  ggplot(aes(alpha, mse_min)) +
  geom_line(size = 2) +
  geom_ribbon(aes(ymax = mse_min + se, ymin = mse_min - se), alpha = .25) +
  ggtitle("MSE ± one standard error")

# using lasso as the best model
cv_lasso   <- cv.glmnet(ames_train_x, ames_train_y, alpha = 1.0)
min(cv_lasso$cvm)

# predict
pred <- predict(cv_lasso, s = cv_lasso$lambda.min, ames_test_x)
mean((ames_test_y - pred)^2)
