## Read in the data
data <- read.table("bp.txt", header=TRUE ,sep="")

attach(data)

##############
##Question 1##
##############

## Plot the data
plot(BP~weight, xlab="Weight", ylab="Blood Pressure", main="Blood Pressure against Weight")

## This one is a bit ambiguous, an argument can be made that the relationship is linear or curved. Can be difficult especially with a small data set. 

##############
##Question 2##
##############

## Run the linear regression
bp.lm <- lm(BP~weight)

## View the model and estimated coefficients
bp.lm

## Slope is 0.4194. The predicted blood pressure increases by 0.4194 mmHg per 1 pound increase in weight, for males between 25 and 30 years old..
## Intercept is 69.1044. The predicted blood pressure is 69.1044 for a 25 to 30 year old male who weighs 0 pounds. This value is an extrapolotion since no one weighs 0 pounds. 

##############
##Question 3##
##############

##Use R as a calculator to predict the response when weight is 200 pounds
coef(bp.lm)[1] + 200 * coef(bp.lm)[2]

##another way to do the prediction using R. I will provide a tutorial on this for module 2. 
newdata <- data.frame(weight=200)
predict.lm(bp.lm, newdata)

## Predicted BP for this person who weighs 200 pounds is 152.9875 mmHg

##Find the residual. Actual blood pressure minus the predicted blood pressure for this individual
148 - (coef(bp.lm)[1] + 200 * coef(bp.lm)[2])

## Residual is -4.9874

##############
##Question 4##
##############

## View ANOVA table
anova(bp.lm)

##############
##Question 5##
##############

## R-squared is 0.5983 from summary(bp.lm). It is found by SS Reg / (SS Residual + SS Reg). About 60% of the variance in blood pressure can be explained by weight.

##############
##Question 6##
##############

## The estimated standard deviation of the error is the residual standard error found from summary(bp.lm), which is 8.681. This is also the squareroot of the MS Residual.

##############
##Question 7##
##############

## Null hypothesis for ANOVA F test is \beta_1 = 0, alternative hypothesis is \beta_1 is not 0. 

##############
##Question 8##
##############

## The F-statistic is equal to MS Regression divided by MS Residual from the ANOVA table.

##############
##Quesiton 9##
##############

## Since the p-value from the F test is so small, we reject the null hypothesis. The data support the claim that weight and blood pressure have a linear relationship.

#######################
##Additional comments##
#######################

#####################################
##From the output of summary(bp.lm)##
#####################################

## Note the t-statistic for the slope and the F-statistic at the bottom. Square the t-statistic and you get the F-statistic!
## Note the p-values for the t-stat for the slope and the F-stat are the same!
## In simple linear regression (one predictor), the t-test for the slope and the ANOVA F test are the same.
## Null hypothesis is \beta_1 = 0, alternative hypothesis is \beta_1 is not 0. 

##How to find p-value from F-statistic
1-pf(35.74,1,24)

##How to find critical value for F statistic
qf(0.95,1,24)


