#1
data <- read.table("nfl.txt",header=TRUE)
attach(data)
pairs(data)

#2
result <- lm(y~x2+x7+x8)
summary(result)
sprintf( "y = %.3f + %.3f*x2 + %.3f*x7 + %.3f*x8",
         result$coefficients[1],
         result$coefficients[2],
         result$coefficients[3],
         result$coefficients[4])

#3
result$coefficients[3]

#4 x2 - 2000 yards , x7 = 48% , x8 = 2350 yards
newdata <- data.frame(x2=2000, x7 = 48, x8= 2350)
predict.lm(result,newdata,level=0.95,interval="prediction")
predict.lm(result,newdata,level=0.95,interval="confidence")
# y = 0.003598*2000 - 0.004816*2350 +0.193960*48 = 5.188479999999998
  
anova(result)

#5 
summary(result)
# P values are small -> reject null hypothesis. Regression model 
#is useful for predicting the number of wins in the 1976 season
# Ho = b1 =b2 =b3 = 0
# Ha: atleast one Bn value is not zero
# t-values: x2 (5.177), x7 (2.198). x8(3.771)
qt(0.975,24) #-> critical t-value = 2.06, reject Ho


# 6
# Ho : B1 = 0
# Ha: B2 != 0
#t - value for x7 = 2.198
tstat <- 0.19396 / 0.088233 # = 2.198
qt(0.975,24) # = 2.063
# critical t-value = 2.06 -> reject Ho -> x7 is significant with other predictors


#7
plot(result$fitted.values,result$residuals,xlab= "fitted values",ylab="residuals")
abline(h=0,col="red")
#mean seems ~ 0 and equal variance
acf(result$residuals, main="ACF of Residuals")
# initial lag that decreases with further data points -> some autocorrelation
# between the y points but not significant
# can be said that errors are not correlated

qqnorm(result$residuals)
qqline(result$residuals,col="red")
# some deviation from normality but reasonable


#8 
result <- lm(y~x1+ x2+x7+x8)
summary(result)
qt(0.975,23) # -> critical t-value = 2.068
# x1 and x7 can be dropped in the presence of the other predictors but CAN STILL BE 
# linearly correlated to the response variable