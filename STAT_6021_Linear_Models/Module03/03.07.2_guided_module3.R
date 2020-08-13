data<-read.table("defects.txt", header=TRUE, sep="")
attach(data)

result<-lm(defects~weeks)

##############
##Question 1##
##############

plot(weeks,defects, xlab="Weeks", ylab="# of Defects per 10,000", main="Defects against Weeks")
abline(result)

##############
##Question 2##
##############

plot(result$fitted.values,result$residuals, xlab="Fitted Values", ylab="Residuals", main="Residual Plot of Defects against Weeks")
abline(h=0)

##############
##Question 5##
##############

library(MASS)

boxcox(result)

##############
##Question 6##
##############

log.defects<-log(defects)

result.log<-lm(log.defects~weeks)

plot(result.log$fitted.values,result.log$residuals, xlab="Fitted Values", ylab="Residuals", main="Residual Plot of log Defects against Weeks")
abline(h=0)

boxcox(result.log, lambda = seq(-4, 4, 1/10))

##############
##Question 7##
##############

acf(result.log$residuals)

##############
##Question 8##
##############

qqnorm(result.log$residuals)
qqline(result.log$residuals)
