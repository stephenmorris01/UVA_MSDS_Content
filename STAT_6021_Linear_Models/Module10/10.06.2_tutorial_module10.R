##Part 1

data<-read.table("titanic.txt", header=TRUE, sep="")

##set the random number generator so same results can be reproduced
set.seed(111)

##choose the observations to be in the training. I am splitting the dataset into halves
sample<-sample.int(nrow(data), #count rows
                  floor(.50*nrow(data)), #round down middle row # in data
                  replace = F) #sample without replacement
train<-data[sample, ]
test<-data[-sample, ]

##use training data to fit logistic regression model with fare and gender as predictors
result<-glm(Survived ~ Fare + Sex, family=binomial, data=train)

library(ROCR)

##predicted survival rate for testing data based on training data
preds<-predict(result,newdata=test, type="response")
##produce the numbers associated with classification table
rates<-prediction(preds, test$Survived)

##store the true positive and false postive rates
roc_result<-performance(rates,measure="tpr", x.measure="fpr")

##plot ROC curve and overlay the diagonal line for random guessing
plot(roc_result, main="ROC Curve for Titanic")
lines(x = c(0,1), y = c(0,1), col="red")

##compute the AUC
auc<-performance(rates, measure = "auc")
print(auc@y.values)

##confusion matrix. Actual values in the rows, predicted classification in cols
confusion_matrix_outcomes <- function(true_values, predictions, threshold){
  cm1 <- table(true_values, predictions>threshold)
  print(cm1)
  output <- cat("\n",paste(" overall error rate: ",(cm1[1,2]+cm1[2,1] )/ sum(cm1)),"\n\n") +
    cat(paste("false positive rate: ",cm1[1,2] / sum(cm1[1,])), "\n") +
    cat(paste("        specificity: ",1- (cm1[1,2] / sum(cm1[1,]))), "\n\n") +
    cat(paste("false nevative rate: ",cm1[2,1] / sum(cm1[2,])), "\n") +
    cat(paste("        sensitivity: ",1- (cm1[2,1] / sum(cm1[2,]))))
  
}

confusion_matrix_outcomes(test$Survived, preds, 0.5)

confusion_matrix_outcomes(test$Survived, preds, 0.7)





####### Part 2

data<-read.table("contraceptive.txt", header=FALSE, sep="")

##give descriptive names to each column
colnames(data)<-c("wife_age", "wife_edu", "hus_edu", "children", "wife_rel", "wife_work", "hus_job", "sol", "media", "c_method")

attach(data)

##notice R treats this categorical variable as quantitative
is.numeric(wife_rel)

##tell R to treat this variable as categorical
wife_rel<-factor(wife_rel)

is.numeric(wife_rel)
is.factor(wife_rel)

##give descriptive names to the levels of this categorical variable
levels(wife_rel)
levels(wife_rel)<-c("non_Islam","Islam")

##tell R to treat contraceptive method as categorical and give descriptive names for each level
c_method<-factor(c_method)
levels(c_method)<-c("no", "long-term", "short-term")

library(nnet)

##fit multinomial logistic regression model
result<-multinom(c_method ~ children + wife_rel)
summary(result)

##compute test statistics 
z<-summary(result)$coefficients/summary(result)$standard.errors
z

#compute p-values for each coefficient
#absolute value of z above, pnorm is 1 tail test, *2 for 2 tail
p<-(1 - pnorm(abs(z)))*2 
p

