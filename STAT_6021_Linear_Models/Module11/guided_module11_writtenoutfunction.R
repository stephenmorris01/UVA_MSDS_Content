data<-read.table("nfl.txt", header=TRUE,sep="\t")
attach(data)

#use nrow to get the number of rows in the data
n_obs = nrow(data)

#initialize the list of leave one out MSEs
mse_loocv = c()

for (i in seq(1, n_obs)){
  #get the training data by dropping the ith row of the data
  data_train <- data[-i,]
  
  #fit the model on the training data
  model_looc <- lm(y ~ x2+x7+x8, data = data_train)
  
  #get the testing data by keeping only ith row of the data
  data_test <- data[i,]
  
  #extract actual y from the test data
  y = data_test$y 
  
  #get predicted y using the trained model
  y_pred = predict.lm(model_looc, data_test)
  
  #calculate mse for obs i
  mse_i <- (y-y_pred)** 2
    
  #append mse for abs i to the list
  mse_loocv <- c(mse_loocv, mse_i)
  
}

mean(mse_loocv)

library(boot)

#Leave One Cross-Validation have to write
glm.fit<-glm(y~x2+x7+x8, data=data)
cv.err<-cv.glm(data, glm.fit)
cv.err$delta[1] ##the output for the LOOCV should match your own
#gives us the answer automatically


#estimate of mse on test data
#we can always make error on training data small, but not a guarantee on the test data
#that's overfitting
#estimate test MSE, then compare to training set MSE
#if there's a big difference, it's overfitted 
#
#avg sq difference from truth

#prefer to have larger mse which is similar between train and test
#depends on context