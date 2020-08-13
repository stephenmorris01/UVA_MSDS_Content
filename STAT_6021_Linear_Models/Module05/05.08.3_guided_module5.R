library(faraway) 
data(seatpos)
attach(seatpos)

##############
##Question 1##
##############

result<-lm(hipcenter~., data=seatpos) ##full model
summary(result)

##############
##Question 3##
##############

round(cor(seatpos),3) ##correlation matrix, rounded off to 3 decimals

##############
##Question 4##
##############

vif(result)

##############
##Question 5##
##############

round(cor(seatpos[,3:8]),3)

##############
##Question 7##
##############

reduced<-lm(hipcenter~Age+Weight+Ht) ##reduced model with Ht and other 2 predictors

vif(reduced) 

##############
##Question 8##
##############

anova(reduced,result)

##############
##Question 9##
##############

plot(reduced$fitted.values,reduced$residuals,main="Residual Plot of Reduced Model")
abline(h=0,col="red")

acf(reduced$residuals, main="ACF of Residuals from Reduced Model")

qqnorm(reduced$residuals)
qqline(reduced$residuals, col="red")

##Based on the residual plot, the assumptions for the multiple regression model appear to be satisfied. The residuals generally fall in a horizontal band around 0, have constant variance, and have no apparent curvature or pattern. There may be one residual that is fairly large in magnitude, but by and large, the assumptions are met. The ACF plot indicates the residuals are uncorrelated. The ACF is slightly significant at lag 11, but this could be due to sampling variation.

###############
##Question 10##
###############

summary(reduced)

##The R^2 for this model is 0.6562, which is only slightly less than the R^2 for the model with all predictors. The adjusted R^2 for this simplified model is 0.6258, which is higher than the adjusted R^2 for the full model, which is 0.6001. One thing to note is that adding predictors to a model never decreases the R^2, so the adjusted R^2 is a better way to compare models with different number of predictors.

###############
##Question 10##
###############

result.error<-lm(hipcenter+10*rnorm(38)~.,seatpos)
summary(result.error)

##Although the $R^2$ and standard error are very similar to the model with no measurement error, a number of the estimated coefficients are quite different, indicating their sensitivity to the accuracy in the measurement of the response variables. This sensitivity is another indication of multicollinearity.