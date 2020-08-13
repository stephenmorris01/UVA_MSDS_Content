data<-read.table("bp.txt", header=TRUE, sep="")
attach(data)

result<-lm(BP~weight)

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

n<-length(BP)
p<-2

##critical value using Bonferroni procedure
qt(1-0.05/(2*n), n-p-1)

sort(ext.student.res)

par(mfrow=c(1,1))
plot(ext.student.res,main="Externally Studentized Residuals", ylim=c(-4,4))
abline(h=qt(1-0.05/(2*n), n-p-1), col="red")
abline(h=-qt(1-0.05/(2*n), n-p-1), col="red")

ext.student.res[abs(ext.student.res)>qt(1-0.05/(2*n), n-p-1)]

##leverages
lev<-lm.influence(result)$hat 

sort(lev)
2*p/n

plot(lev, main="Leverages", ylim=c(0,0.4))
abline(h=2*p/n, col="red")

##identify data points on plot
identify(lev)

lev[lev>2*p/n]

##influential observations
DFFITS<-dffits(result)
DFFITS[abs(DFFITS)>2*sqrt(p/n)]

DFBETAS<-dfbetas(result)
DFBETAS[abs(DFBETAS)>2/sqrt(n)]

COOKS<-cooks.distance(result)
COOKS[COOKS>qf(0.5,p,n-p)]