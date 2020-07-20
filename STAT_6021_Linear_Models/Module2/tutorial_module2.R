## store data file with the variable name data
data<-read.table("purity.txt", header=TRUE ,sep="")

##make data the default data frame
attach(data)

##Fit a regression model
lm(purity~hydro)
result<-lm(purity~hydro)
summary(result)

##to obtain t multiplier for a 95% CI with df=18
t_multiplier <- qt(0.975,18)
hydro_SD <- summary(result)$coefficients[2,1]
hydro_SE <- summary(result)$coefficients[2,2]
hydro_SD - t_multiplier*hydro_SE
hydro_SD + t_multiplier*hydro_SE



##to obtain p-value from a 2-sided test
2*(1-pt(3.386,18))

##to produce 95% CIs for all regression coefficients
confint(result,level = 0.95)

##to produce 95% CI for the mean response when x=1.2, and the 95% PI for the response of an observation when x=1.2
newdata<-data.frame(hydro=1.2)
predict.lm(result,newdata,level=0.95, interval="confidence")
predict.lm(result,newdata,level=0.95, interval="prediction")

##see what components we can extract from lm
names(result)

##extract the residuals from lm
result$coefficients

detach(data)
###############################################################################
#CLASSWORK 7/15

data <- read.table("BP.txt", header = TRUE ,sep = "")
attach(data)
conf_lvl = 0.95
#It has been suggested that if the predicted systolic blood pressure increases 
#by more than 0.35 mmHg when weight increases by one pound, there is an 
#increased risk of heart disease.
test_val <- 0.35

alpha = 1-conf_lvl
plot(BP,weight,xlab = "Blood Pressure", 
     ylab = "Bodyweight", 
     main = "Plot of Blood pressure against weight")
result <- lm(BP~weight)
sumres <- summary(result)
print(sumres)
cor.test(BP, weight, method = "pearson")
CI <- confint(result,level = 0.95)
print(CI)
print("average of CI values for beta1 == slope estimate: ")
print(mean(CI[2,]))

#computing the t statistic: 
(0.42-0.35)/0.07015
#beta hat1 - beta zero (null hypothesis value) / standard error of beta hat 1
estSlope <- sumres$coefficients[2,][1]
estSE <- sumres$coefficients[2,][2]

1 - pt( 0.98,24)
qt(.95,24) # 1.710882 is what I did
