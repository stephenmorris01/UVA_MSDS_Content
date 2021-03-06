# Question 1

data<-read.table("nfl.txt", header=TRUE, sep="")
attach(data)
#question 1
result.y.passing <- lm(y~x7+x8)
result.passing <- lm(x2~x7+x8)
#part a
res.y.passing <- result.y.passing$residuals
res.passing <- result.passing$residuals
plot(res.y.passing~res.passing, main="passing partial regression plot")
#part b
model.passing <- lm(res.y.passing~res.passing)
abline(model.passing, col="blue")
summary(model.passing)
#part c
model <- lm(y~x2+x7+x8)
summary(model)
#part e
#x7
result.y.per.rushing <- lm(y~x2+x8)
result.per.rushing <- lm(x7~x2+x8)
res.y.per.rushing <- result.y.per.rushing$residuals
res.per.rushing <- result.per.rushing$residuals
plot(res.y.per.rushing~res.per.rushing, main="percent rushing partial regression plot")
model.per.rushing <- lm(res.y.per.rushing~res.per.rushing)
abline(model.per.rushing, col="blue")
summary(model.per.rushing)
#x8
result.y.opp.rushing <- lm(y~x2+x7)
result.opp.rushing <- lm(x8~x2+x7)
res.y.opp.rushing <- result.y.opp.rushing$residuals
res.opp.rushing <- result.opp.rushing$residuals
plot(res.y.opp.rushing~res.opp.rushing, main="opponent rushing partial regression plot")
model.opp.rushing <- lm(res.y.opp.rushing~res.opp.rushing)
abline(model.opp.rushing, col="blue")
summary(model.opp.rushing)


###############################################################################
# Question 2

##residuals
res<-result$residuals 

##studentized residuals
student.res<-rstandard(result) # ????

##externally studentized residuals
ext.student.res<-rstudent(result) 

par(mfrow=c(1,3))
plot(result$fitted.values,res,main="Residuals")
plot(result$fitted.values,student.res,main="Studentized Residuals")
plot(result$fitted.values,ext.student.res,main="Externally  Studentized Residuals")

n<-length(data)
p<-length(result$coefficients)

##critical value using Bonferroni procedure
qt(1-0.05/(2*n), n-p-1)

sort(ext.student.res)

par(mfrow=c(1,1))
plot(ext.student.res,main="Externally Studentized Residuals", ylim=c(-4,4))
abline(h=qt(1-0.05/(2*n), n-p-1), col="red")
abline(h=-qt(1-0.05/(2*n), n-p-1), col="red")

ext.student.res[abs(ext.student.res)>qt(1-0.05/(2*n), n-p-1)]


sort(lev)
2*p/n

plot(lev, main="Leverages", ylim=c(0,0.4))
abline(h=2*p/n, col="red")

##identify data points on plot
identify(lev)



###############################################################################
# Question 3

levthing <- lev[lev>2*p/n]
print(levthing)

#3 look at diagonals of - outliers in x variable
#diagonals of hat matrix are leverages
#influential datapoints tend to be outlying + unusual combination of x and y
#18 and 27 are two highest leverage points



##leverages
lev<-lm.influence(result)$hat 



###############################################################################
#question 4

##influential observations
DFFITS <- dffits(result)
DFFITS[abs(DFFITS) > 2*sqrt(p/n)]

DFBETAS <- dfbetas(result)
DFBETAS[abs(DFBETAS) > 2/sqrt(n)]

COOKS <- cooks.distance(result)
COOKS[COOKS > qf(0.5,p,n - p)]

#sample size is 28, not 24
#n, not n-p 
#
#studentized and externally studentized versions look the exact same 
#diff bet them is one uses means of residuals , other looks at means of resid with datapoint removed
#the are pretty similar, if they look the same you don't have influential datapoints in model
#other possibility is if you have a large datapoint, a single datapoint might have so little influence


# studentized shows standard deviation y axis, 
#   gives sense of scale of outliers, within 2, not a big deal
#
#in result of dffits if named numeric(0) == none
#two results in DFBETAS - only two 
#

#
#if slopes change, also changes prediction 
#