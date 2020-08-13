data <- read.table("delivery.txt", header=TRUE ,sep="")
attach(data)

result<-lm(Delivery~Number+Distance)

summary(result)

## find the critical value for F distribution
##    1-siglvl,  # predictors, (# observations - # predictors - slope)
qf(0.95, 2, 22)
# if F critical value < F statistic, reject null

#find confidence interval
confint(result,level = 0.95)

# CI for mean response and PI for response for particular response
newdata<-data.frame(Number=20, Distance=200)

predict.lm(result, newdata, level=0.95, interval="confidence")
predict.lm(result, newdata, level=0.95, interval="prediction")



