
##(1a)
data<-read.csv("wcgs.csv", header=TRUE, sep=",")

##set the random number generator so same results can be reproduced
set.seed(199)

data$chd69<-factor(data$chd69)

##choose the observations to be in the training. I am splitting the dataset into halves
sample<-sample.int(nrow(data), #count rows
                  floor(.50*nrow(data)), #round down middle row # in data
                  replace = F) #sample without replacement
train<-data[sample, ]
test<-data[-sample, ]

##use training data to fit logistic regression model with fare and gender as predictors
result <-glm(chd69 ~ age + ncigs + sbp, family = binomial("logit"), data=train)
summary(result)

###(1b)


library(ROCR)

##predicted survival rate for testing data based on training data
preds<-predict(result,newdata=test, type="response")
##produce the numbers associated with classification table
rates<-prediction(preds, test$chd69)

##store the true positive and false postive rates
roc_result<-performance(rates,measure="tpr", x.measure="fpr")

##plot ROC curve and overlay the diagonal line for random guessing
plot(roc_result, main="ROC Curve for WCGS heart disease")
lines(x = c(0,1), y = c(0,1), col="red")

#ROC result is not good, pretty close to random chance


###(1c)


##compute the AUC
auc<-performance(rates, measure = "auc")
print(auc@y.values)
##AUC agrees with curve assessment
##0.6898849



###(1d)

##confusion matrix. Actual values in the rows, predicted classification in cols
confusion_matrix_outcomes <- function(true_values, predictions, threshold){
  cm1 <- table(true_values, predictions>threshold)
  print(cm1)
  type1 = cm1[1,2]
  type2 = cm1[2,1]
  true_neg = cm1[1,1]
  true_pos = cm1[2,2]
  output <- cat("\n",paste(" overall error rate: ",(type1+type2)/ sum(cm1)),"\n\n") +
    cat(paste("false positive rate: ",type1 / (type1+true_neg), "\n") +
    cat(paste("        specificity: ",1- (type1 / sum(cm1[1,]))), "\n\n") +
    cat(paste("false negative rate: ",cm1[2,1] / sum(cm1[2,])), "\n") +
    cat(paste("        sensitivity: ",1- (cm1[2,1] / sum(cm1[2,]))))
  
}
confusion_matrix_outcomes(test$chd69, preds, 0.5) 
#ALL FALSE ??

confusion_matrix_outcomes(test$chd69, preds, 0.1)
# true_values FALSE TRUE
#         0   1160  280
#         1    78   59
# 
# overall error rate:  0.227013316423589 
# 
# false positive rate:  0.194444444444444 
# specificity:  0.805555555555556 
# 
# false negative rate:  0.569343065693431 
# sensitivity:  0.430656934306569




####### Part 2
library(MASS)
data<-Boston

data$crim_cat <- cut(data$crim, breaks = quantile(data$crim, c(0,0.5, 0.75,1)), quantile = TRUE, labels = c("low", "medium", "high"))

library(nnet)

##fit multinomial logistic regression model
result<-multinom(data$crim_cat ~ data$dis + data$ptratio)
summary(result)

##compute test statistics 
z<-summary(result)$coefficients/summary(result)$standard.errors
z

#compute p-values for each coefficient
#absolute value of z above, pnorm is 1 tail test, *2 for 2 tail
p<-(1 - pnorm(abs(z)))*2 
p


library(aod)
wald.test(b = coef(result), Sigma = vcov(result), Terms = 1:2)
#??????????????
#
set.seed(1)
sample.int(100,5)