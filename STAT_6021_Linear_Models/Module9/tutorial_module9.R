##Example 1

data<-read.table("titanic.txt", header=TRUE, sep="")
attach(data)
        #generalized linear model        could use for LRM, "gaussian" as family
        #lm() uses least squares
result<-glm(Survived ~ Fare, family = "binomial")

summary(result)

#
confint(result, level=0.95)

#null deviance is residual sum of squares, 
#degrees of freedom is n-1
#Residual deviance - SSres for particular model (smaller the better)

#perform test to see if coefficient is 0 or not
#consider fitting full model with all 3 predictors

full<-glm(Survived ~ Fare + Sex + Age, family = "binomial")
summary(full)
#sex sign, not age
#residual deviance went down
#null deviance is the same
#see if slope of coefficients is zero or not

####Delta G squared test statistic####
#looks at diff btw res dev and null dev
#DF is 3, diff btw df of null and res dev

# p-chi squared test statistic
#area to left so subtracted from 1
#null == slope of coefficients are all 0
#alt == at least one is not 0

#1-pchisq(full$deviance,703) # HE DIDN'T TALK ABOUT THIS LINE, not sure what it means
  # goodness of fit test - whether

        #SSres of intercept    ##SSres of model being investigated
1-pchisq(full$null.deviance-full$deviance,3)
# p-value is highly significant, not surprising w 2 sig. predictors


#to test if a subset of coefficients are 0 or not
#   to remove the last two, finding different between full deviance of 2 separate models
#   null is both coefficients are 0
#   reject null so we should go with more complicated model b/c improves prediction
1-pchisq(result$deviance-full$deviance,2)






##Example 2

data2<-read.table("dose.txt", header=T)
attach(data2)

#grouped data
#each row is a separate group
#the way we use R will be a bit different

data2$prop<-died/size
#why didn't you just attach the new column to the dataset? use a marker to say was added

plot(logdose, log(prop/(1-prop)), xlab= "Log Dose", ylab="sample log odds")
# not exactly a linear relationship on plot

#                                           have to add weights, sample size
result2<-glm(prop~logdose, family="binomial", weights=size)
summary(result2)
#coefficients are significantly far from 0
#however, plot is not straight line, may not truly fit well


# pearson's chi squared and goodness of fit test
#   just need residuals of model
#   test statistic is sum of sq pearson resid
pearson<-residuals(result2,type="pearson")
X2<-sum(pearson^2)
X2
# results of 28.5
#   WHAT IS THIS TELLING US

1-pchisq(X2,9-2)
# number of groups we have - 2 (1 for intercept, 1 for slope)
# reject null, tells us that data doesn't fit the model well
# agrees with our eyes
# 
# 
# deviance goodness of fit test - compare with above
1-pchisq(result2$deviance,7)
# test statistics are really close, asymptotically similar to each other
# tesll us that our usual regression model doesn't fit well with this particular dataset