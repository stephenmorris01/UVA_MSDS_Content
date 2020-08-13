data<-read.table("nfl.txt", header=TRUE, sep="")
attach(data)

library(leaps)

# #Delete half at random
# data <- data[-sample(1:nrow(data), nrow(data) / 2), ]

##perform all possible regressions (1st order)
allreg <- regsubsets(y ~., data=data, nbest=9)

##create a "data frame" that stores the predictors in the various models considered as well as their various criteria
best <- as.data.frame(summary(allreg)$outmat) #gets rid of quotes
best$p <- as.numeric(substr(rownames(best),1,1))+1 #extra columns giving number of coefficients, etc etc
best$r2 <- summary(allreg)$rsq
best$adjr2 <- summary(allreg)$adjr2
best$mse <- (summary(allreg)$rss)/(dim(data)[1]-best$p)
best$cp <- summary(allreg)$cp
best$bic <- summary(allreg)$bic
best #Woo thinks they sort by bic (what is that?)

##sort by various criteria
best[order(best$r2),]
best[order(best$adjr2),]
best[order(best$mse),] #want smallest
best[order(best$cp),] #want smallest
best[order(best$bic),]

#automated search procedures

##intercept only model
regnull <- lm(y~1, data=data)
##model with all predictors
regfull <- lm(y~., data=data)

##forward selection, backward elimination, and stepwise regression
##
### what's the upper and lower bounds of the model I consider
step(regnull, scope=list(lower=regnull, upper=regfull), direction="forward") 
# starting from intercept only model, then consider adding each of these first 
# lastly these are the best predictors using forward prediction

# AUTOMATED SEARCH PROCEDURES DON'T ALWAYS AGREE

step(regfull, scope=list(lower=regnull, upper=regfull), direction="backward")

step(regnull, scope=list(lower=regnull, upper=regfull), direction="both") #lm(formula = y ~ x8 + x2 + x7 + x9, data = data)

# when create model that definitely includes .... -> expert knowledge
final_lm <- lm(formula = y ~ x8 + x2 + x7 + x9, data = data)
print(summary(final_lm)) 
# Residual standard error: 1.681 on 23 degrees of freedom
# Multiple R-squared:  0.8012,	Adjusted R-squared:  0.7666 


#https://stevencarlislewalker.wordpress.com/2013/06/18/calculating-the-press-statistic-in-r/

PRESS_val <- function(lm_input) {
  pr <- resid(lm_input)/(1 - lm.influence(lm_input)$hat)
  return (sum(pr^2))
}
lm_PRESS <- PRESS_val(final_lm)
print(lm_PRESS) #[1] 87.65965


press_calc2 <- function(model){
  hat<- lm.influence(model)$hat
  sum<- 0
  for (i in 1:length(hat)) {
    sum <- sum + (model$residuals[i] / (hat[i]))^2
  }
}

press_calc3 <- function(model1){
  (sum((model1$residuals/(1-lm.influence(model = model1)$hat))^2))
}

#https://stats.stackexchange.com/questions/174861/calculating-regression-sum-of-square-in-r

SSTotal <- var( data$y ) * (nrow(data)-1)
# SSE     <- sum( final_lm$resid^2 )
# SSreg   <- SSTotal - SSE
predr2 <- 1-(lm_PRESS / SSTotal)   #-- should be  / SST instead of SSreg
print(predr2) #[1] 0.66537      0.7325?


#REMOVED HALF VALUES
#lm(formula = y ~ x8 + x2 + x7 + x9, data = data)
#PRESS [1] 63.8088
#pred R2 [1] 0.6205463
#Residual standard error: 1.872 on 9 degrees of freedom
#Multiple R-squared:  0.842,	Adjusted R-squared:  0.7718 
myvars = c('x8', 'x2', 'x7', 'x9')
pred <- predict(final_lm, data[myvars], interval="prediction")

df3 = merge(data, pred, by.x=0, by.y=y) #maybe can just output differences?

print(pred)

#cross validation is you'll leave part of dataset out at a time, use that subset as a test
#k-fold cross validation, divide dataset into k pieces, first 4/5 will be training set, last k testing
#cycle that through, eventually testing on every k piece
#
#leave one out cross validation is where n-1
#if prediction is really far off from training, how well do you do with just predicting on training data
#if really different, you know model is overfit to training data, not generalizeable
#