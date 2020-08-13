data<-read.csv("wcgs.csv", header=TRUE)
attach(data)

##############
##Question 1##
##############

par(mfrow=c(1,4))
boxplot(age~chd69, main="Age by Disease")
boxplot(sbp~chd69, main="SBP by Disease")
boxplot(dbp~chd69, main="DBP by Disease")
boxplot(ncigs~chd69, main="Cigs by Disease")

##############
##Question 1##
##############

result<-glm(chd69 ~ age + sbp + dbp + ncigs, family="binomial")
summary(result)

##############
##Question 4##
##############

##make prediction for log odds
newdata<-data.frame(age=45, sbp=110, dbp=70, ncigs=0)
predict(result,newdata)
odds<-exp(predict(result,newdata)) ##note predict gives the log odds, need to exponentiate to get odds
odds

##convert odds to probability
prob<-odds/(1+odds)
prob

predict(result,newdata, type="response") ##need to add type="response" for probability instead of log odds

##############
##Question 5##
##############

deltaG2<-result$null.deviance-result$deviance ##take difference between the null and residual deviance for our model
1-pchisq(deltaG2,4) ##df is 4 since our model has 4 additional parameters other than the intercept

##############
##Question 7##
##############

reduced<-glm(chd69 ~ age + ncigs, family="binomial")
summary(reduced)
deltaG2_partial<-reduced$deviance-result$deviance ##take difference in residual deviances between the two models
deltaG2_partial
1-pchisq(deltaG2_partial,2) ##df is 2 since we have 2 additional parameters in the bigger model