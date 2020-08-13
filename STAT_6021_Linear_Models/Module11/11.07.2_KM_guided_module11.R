data<-read.table("nfl.txt", header=TRUE,sep="\t")

attach(data)

result<-lm(y~x2+x7+x8, data=data)

##check regression assumptions on transformed variables
##residual plot
plot(result$fitted.values,result$residuals, main="Plot of Residuals against Fitted Values")
abline(h=0,col="red")

##acf plot of residuals
acf(result$residuals)

##qq plot of residuals
qqnorm(result$residuals)
qqline(result$residuals, col="red")




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
glm.fit <- glm(y~x2+x7+x8, data=data)
cv.err <- cv.glm(data, glm.fit)
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





res<-result$residuals

##PACF plot of residuals
pacf(res, main="PACF of Residuals")

##fit an AR(1) model for residuals
ar.1<-arima(res,order = c(1,0,0), include.mean = FALSE)
ar.1

##transform response and predictor
shift<-ar.1$coef
y<-cbind(as.ts(data$y),lag(data$y))
yprime<-y[,2] - shift*y[,1]
x<-cbind(as.ts(x2+x7+x8),lag(x2+x7+x8))
xprime<-x[,2] - shift*x[,1]

##perform regression on transformed variables
result.prime<-lm(yprime~xprime)
summary(result.prime)

##check regression assumptions on transformed variables
##residual plot
plot(result.prime$fitted.values,result.prime$residuals, main="Plot of Residuals against Fitted Values")
abline(h=0,col="red")

##acf plot of residuals
acf(result.prime$residuals)

##qq plot of residuals
qqnorm(result.prime$residuals)
qqline(result.prime$residuals, col="red")
