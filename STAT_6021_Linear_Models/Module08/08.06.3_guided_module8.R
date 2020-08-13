data<-read.table("nfl.txt", header=TRUE, sep="")
attach(data)

###############
##Question 1a##
###############

##Partial residual plot for x2

result.y.x2<-lm(y~x7+x8) ##fit y against other predictors
result.x2<-lm(x2~x7+x8) ##fit x2 against other predictors

res.y.x2<-result.y.x2$residuals ##store residuals. info in y not explained by x7 and x8
res.x2<-result.x2$residuals ##store residuals. info in x2 not explained by x7 and x8

##partial residual plot for x2
plot(res.x2,res.y.x2, main="Partial Residual Plot for x2")
abline(h=0, col="red") 

###############
##Question 1b##
###############
summary(lm(res.y.x2~res.x2))

##For partial residual plot, the intercept should be 0, and the slope will be equal to the coefficient for x2 in MLR with x2, x7, x8 as predictors

###############
##Question 1c##
###############
result<-lm(y~x2+x7+x8)

summary(result)

##Look at coefficient for x2. should be same as slope from question 1b

###############
##Question 1e##
###############

##Partial residual plot for x7

result.y.x7<-lm(y~x2+x8)
result.x7<-lm(x7~x2+x8)

res.y.x7<-result.y.x7$residuals
res.x7<-result.x7$residuals

plot(res.x7,res.y.x7, main="Partial Residual Plot for x7")
abline(h=0, col="red")

summary(lm(res.y.x7~res.x7))

##Partial residual plot for x8

result.y.x8<-lm(y~x2+x7)
result.x8<-lm(x8~x2+x7)

res.y.x8<-result.y.x8$residuals
res.x8<-result.x8$residuals

plot(res.x8,res.y.x8, main="Partial Residual Plot for x8")
abline(h=0, col="red")

summary(lm(res.y.x8~res.x8))

##notice the partial residual plots are all linear. So only linear terms are needed for the predictors, no need to transform them

##############
##Question 2##
##############

res<-result$residuals ##residuals

student.res<-rstandard(result) ##studentized residuals

ext.student.res<-rstudent(result) ##externally studentized residuals


##all the residual plots. They look the same (generally) but the scale for the ordinary residuals is different
par(mfrow=c(1,3))
plot(result$fitted.values,res,main="Residuals")
plot(result$fitted.values,student.res,main="Studentized Residuals")
plot(result$fitted.values,ext.student.res,main="Externally  Studentized Residuals")

##############
##Question 3##
##############

n<-length(y)
p<-4
qt(1-0.05/(2*n), n-p-1)

##this check which externally studentized residuals are greater than the critical value
ext.student.res[abs(ext.student.res)>qt(1-0.05/(2*n), n-p-1)]
##returns a null, so no observations are outlying in the response.

lev<-lm.influence(result)$hat ##leverages

2*p/n

lev[lev>2*p/n]
##Team 18 and 27 have leverages greater than 2p/n

##############
##Question 4##
##############

DFFITS<-dffits(result)

DFFITS[abs(DFFITS)>2*sqrt(p/n)]

##None of the observations have DFFITS greater than the threshold

DFBETAS<-dfbetas(result)
DFBETA1<-DFBETAS[,1]
DFBETA2<-DFBETAS[,2]
DFBETA3<-DFBETAS[,3]
DFBETA4<-DFBETAS[,4]

DFBETA1[abs(DFBETA1)>2/sqrt(n)]
DFBETA2[abs(DFBETA2)>2/sqrt(n)]
DFBETA3[abs(DFBETA3)>2/sqrt(n)]
##Team 21 influences the estimated value of beta 3
DFBETA4[abs(DFBETA4)>2/sqrt(n)]
##Team 10 influences the estimated value of beta 3

COOKS<-cooks.distance(result)
COOKS[COOKS>qf(0.5,p,n-p)]

##None of the observations have Cook's distance greater than the threshold