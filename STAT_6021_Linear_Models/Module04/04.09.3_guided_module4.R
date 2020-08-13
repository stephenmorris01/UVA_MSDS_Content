data<-read.table("nfl.txt", header=TRUE, sep="")
attach(data)

##############
##Question 1##
##############

##scatterplot matrix
pairs(data, lower.panel = NULL, main="Scatterplot of Quantitative Variables")

##pairwise correlations
cor(data)
round(cor(data),3)

##############
##Question 2##
##############

result<-lm(y~x2+x7+x8)

summary(result)

##############
##Question 4##
##############

##predict y for specific values of predictors
newdata<-data.frame(x2=2000,x7=48,x8=2350)
##want PI instead of CI since we want an interval for the wins of a single team, not the average wins for teams
predict.lm(result,newdata,interval="prediction")

##############
##Question 7##
##############

##residual plot
plot(result$fitted.values, result$residuals, xlab="Fitted Values", ylab="Residuals", main="Residual Plot")
abline(h=0)

##acf plot of residuals
acf(result$residuals)

##QQ plot of residuals
qqnorm(result$residuals)
qqline(result$residuals)


##############
##Question 8##
##############

##consider a model with x1, rushing yards added

result2<-lm(y~x2+x7+x8+x1)
summary(result2)

#################################
##Extra comments for question 8##
#################################


##need SLR to address classmate's statement

result3<-lm(y~x1)
summary(result3)

plot(y~x1)
abline(result3)

cor(cbind(x1,x2,x7,x8))

##Notice on its own x1 is linearly related to the response. 
##It is not needed in a model with x2, x7, x8 as it doesn't improve the predictions significantly as it is highly correlated with a number of other predictors. So x1 doesn't provide much additional insight to the prediction.



