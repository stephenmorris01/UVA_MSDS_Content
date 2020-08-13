##############
##question 2##
##############

library(MASS)

attach(Boston)

###############
##question 2a##
###############

##initialize array to store the converted response variable
crime_level<-array(0,dim(Boston)[1])

##classify crime levels
for (i in 1:dim(Boston)[1])

{

  if (crim[i] < median(crim))

  {

    crime_level[i]<- "low"

  }

  if (crim[i] >= median(crim) && crim[i] < quantile(crim, 0.75))

  {

    crime_level[i]<- "medium"

  }

  if (crim[i] >= quantile(crim, 0.75))

  {

    crime_level[i]<- "high"

  } 


}

##make sure the response is viewed as a factor
crime_level<-factor(crime_level)

##check coding scheme. By default, the levels are arranged in alphabetical order and the first in order becomes the reference class. 
contrasts(crime_level)

###############
##question 2b##
###############

library(nnet)

##fit multinomial regression model

result<-multinom(crime_level ~ dis + ptratio)
summary(result)

##coefficients for variable dis are all positive
##coefficients for ptratio are all negative

###############
##question 2c##
###############

##compute Wald statistics
z<-summary(result)$coefficients/summary(result)$standard.errors
z

##compute corresponding p-values
p<-(1 - pnorm(abs(z)))*2
p

##all z statistics are large in magnitude, resulting in small p-values

