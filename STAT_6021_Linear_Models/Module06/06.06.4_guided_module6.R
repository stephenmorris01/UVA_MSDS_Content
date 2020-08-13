data<-read.table("cereals.txt", header=TRUE, sep="")
attach(data)

##use calories as response. mfr, sugars as predictors. G: Gen Mills, K: Kelloggs 

is.factor(mfr) ##check Region is factor 

levels(mfr) ##check name of levels for Region

##############
##Question 1##
##############

##split data by manufacturer type to produce different plots
a1<-subset(data,mfr=="other") 
a2<-subset(data,mfr=="G") 
a3<-subset(data,mfr=="K") 

##create separate regression lines for each manufacturer
reg1<-lm(calories~sugars,data=a1)
reg2<-lm(calories~sugars,data=a2)
reg3<-lm(calories~sugars,data=a3)

##create scatterplot with separate colors and symbols for each manufacturer
plot(sugars,calories, main="Calories against Sugars, by Manufacturer")
points(a2$sugars,a2$calories, pch=2, col="red") 
points(a3$sugars,a3$calories, pch=12, col="blue")
##overlay separate regression lines
abline(reg1,lty=1)
abline(reg2,lty=2, col="red") 
abline(reg3,lty=3, col="blue")
##add legend to plot
legend("topleft", c("other","Gen Mills","Kelloggs"), lty=c(1,2,3), pch=c(1,2,12), col=c("black","red","blue")) 

##############
##Question 2##
##############

##check coding scheme
contrasts(mfr)  

##Set "other" as reference class, based on question
mfr<-relevel(mfr, ref = "other")
##check reference class has been correctly set 
contrasts(mfr)

##regression with interaction
result<-lm(calories~sugars*mfr)
summary(result)

##############
##Question 3##
##############

##regression without interaction
reduced<-lm(calories~sugars+mfr)

##partial F test to see if interaction terms can be dropped
anova(reduced,result)
summary(reduced)

##############
##Question 4##
##############

##residual plot
plot(reduced$fitted.values,reduced$residuals,main="Residual plot")
abline(h=0,col="red")

##acf plot of residuals
acf(reduced$residuals)

##QQ plot of residuals
qqnorm(reduced$residuals)
qqline(reduced$residuals, col="red")

##test of equality of variances across classes
library(lawstat)
levene.test(calories,mfr)

library(MASS)
boxcox(reduced, lambda=seq(0,3,by=0.01))

##############
##Question 5##
##############

##carry out Tukey's multiple comparisons to assess if the average calories, for given sugars, differs between manufacturers

library(multcomp)
pairwise<-glht(reduced, linfct = mcp(mfr= "Tukey"))
summary(pairwise)





