##############
##question 1##
##############

data<-read.csv("wcgs.csv", header=TRUE)
attach(data)

set.seed(199)

##split data into two equal parts
sample<-sample.int(nrow(data), floor(.50*nrow(data)), replace = F)
train<-data[sample, ]
test<-data[-sample, ]

###############
##question 1a##
###############

##fit model using training data
model_train<-glm(chd69 ~ age + sbp + ncigs, family="binomial", data=train)

###############
##question 1b##
###############

##generate ROC curve
library(ROCR)
preds<-predict(model_train,newdata=test, type="response")
rates<-prediction(preds, test$chd69)
roc_result<-performance(rates,measure="tpr", x.measure="fpr")
plot(roc_result, main="ROC Curve for WCGS Data Set")
lines(x = c(0,1), y = c(0,1), col="red")

###############
##question 1c##
###############

auc<-performance(rates, measure = "auc")
auc

###############
##question 1d##
###############

##cutoff of 0.5
table(test$chd69, preds>0.5)

##cutoff of 0.1
table(test$chd69, preds>0.1)

##counts for test data
table(test$chd69)

##In our test data, we have 1440 negatives and 137 positives.

##histogram of predicted probabilities
hist(preds)

##Looking at the distribution of estimated probabilities for each subject, a lot of their probabilities are small; none are greater than 0.5.




