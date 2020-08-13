data<-read.table("nfl.txt", header=TRUE, sep="")
attach(data)

##############
##Question 1##
##############

##fit linear model with predictors
result<-lm(y~x2+x7+x8)

##############
##Question 2##
##############

PRESS <- function(linear.model) {
  ## get the residuals from the linear.model. extract hat from lm.influence to obtain the leverages
  pr <- residuals(linear.model)/(1-lm.influence(linear.model)$hat)
  ## calculate the PRESS by squaring each term and adding them up
  PRESS <- sum(pr^2)
  
  return(PRESS)
}

##############
##Question 3##
##############

PRESS(result)

##PRESS statistic is 87.46123

anova_result<-anova(result)

##Find SST
SST<-sum(anova_result$"Sum Sq")

Rsq_pred<-1-PRESS(result)/SST

Rsq_pred

##R-squared prediction is 0.7325. The model might be able to explain 73.25% of the variability in the number of wins (the response variable) in new observations.
##The R-squared is 0.8425. Both values are fairly high, so the model has good predictive ability.

##############
##Question 4##
##############

##randomly split the data into two parts
halfout <- data[sample(nrow(data), (nrow(data)/2)), ]

##fit model with just the estimation data
result2 <- lm(y ~ x2 + x7 + x8, data = halfout)

anova_result2<-anova(result2)

##Find SST
SST2<-sum(anova_result2$"Sum Sq")

Rsq_pred2<-1-PRESS(result2)/SST2

Rsq_pred2

##R-squared prediction is smaller with less observations.

##############
##Question 5##
##############

summary(result)

summary(result2)

##Standard errors of the coefficients for the model built on all observations are smaller, indicating more precision in the estimates.

##############
##Question 6##
##############

##Find yhat for all observations using the model built on all observations
result$fitted

##Find yhat for all observations using the model built on half the data points
predict(result2, newdata=data)

##Put the yhats from both models side by side for easier comparison
cbind(y,result$fitted,predict(result2, newdata=data))

##Find SS residuals for both
res1<-result$res

res2<-y-predict(result2, newdata=data)

sum(res1^2)

sum(res2^2)

##SS res for model built on all observations should be smaller






