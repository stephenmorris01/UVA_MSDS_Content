data <- read.table("bp.txt", header=TRUE ,sep="")

attach(data)

##############
##Question 1##
##############

plot(weight,BP, main="Plot for Blood Pressure against Weight")

result<-lm(BP~weight)
summary(result)

##The estimated regression equation is Predicted BP = 69.104 + 0.419weight

##############
##Question 2##
##############

cor(weight,BP)

##Correlation is 0.773. 

##############
##Question 3##
##############

summary(result)

confint(result, level=0.95)

##The predicted blood pressure increases by 0.4194mmHg when weight increases by one pound. The corresponding 95% confidence interval for the change in blood pressure for a one pound increase in weight is (0.2746, 0.5642).

##############
##Question 4##
##############

##H_0: \beta_1 = 0, H_a: \beta_1 \neq 0. 
##The t statistic is 5.979 with a p-value less than 0.05, so we reject the null hypothesis. Our data support the claim that blood pressure and weight are linearly related. 
##Note: The ANOVA F statistic of 35.74 is the squared of this t statistic, with the same p-value. This is the case in SLR with 1 predictor.

##############
##Question 5##
##############

##Yes the results are consistent, since we rejected the null hypothesis and 0 lies outside the 95% CI for the slope.
##Note: A (1-alpha)x100% CI is consistent with a two-sided hypothesis test at significance level alpha.

##############
##Question 6##
##############

newdata <- data.frame(weight=200)
predict.lm(result, newdata, level=0.95, interval="confidence")

##The estimated mean BP for young males who weigh 200 pounds is 152.9874. This value can also be found by pluggin in weight=200 in your SLR equation.
##The 95% CI for the mean BP for young males who weigh 200 pounds is (148.649, 157.326)

##############
##Question 7##
##############

predict.lm(result, newdata, level=0.95, interval="prediction")

##The 95% PI for the BP for a young male who weigh 200 pounds is (134.553, 171.422)

##############
##Question 8##
##############

##Please see slides from live session.


