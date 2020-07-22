data <- read.table("mileage.txt", header=TRUE ,sep="")
attach(data)
pairs(data)
result<-lm(y~x1+x2+x6+x10)
summary(result)
#see high F statistic and low p value, reject null 
#t test for x10, Vagal test, pretty large p value, insignificant
#   tells us x10 is not useful when we have the other 3 in the model 
#   multiple t tests are insignficant, but F is signficant, tells us collinearity
#   therefore partial F test comes in
#   we could fit reduced model and compare SSR between reduced and bigger model 


reduced<-lm(y~x1)
anova(reduced,result) # F value is F statistic, and shows p value for that statistic
# p value is greater than significance level, 
#     don't have evidence to support more complicated model, stick with simpler model
# null - slopes for 3 predictors are 0, alt is at least one has nonzero slope

# alternatively apply ANOVA with all predictors
anova(result)
# first Sum Sq is SSR for first predictor, 
# second sum sq is SSR for second, given that first is in model, etc.
# 

# SSR for predictors we want, divide by # predictors  
# div mean sq residuals for the model / degrees of freedom
((6.55+12.04+3.37)/3)/(259.86/27)

1-pf(0.7608,3,27)
qf(0.95,3,27)

preds<-cbind(x1,x2,x6,x10)

cor(preds)

library(faraway)

vif(result)

result2<-lm(x1~x2+x6+x10)
summary(result2)

1/(1-0.9496)