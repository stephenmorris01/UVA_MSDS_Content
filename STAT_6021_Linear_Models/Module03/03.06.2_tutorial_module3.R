data <- read.table("defects.txt", header=TRUE ,sep="")
attach(data)

result<-lm(weeks~defects)
summary(result)

##scatterplot of data, with least squares line overlayed
plot(wind, output, main="Plot of DC Output against Wind Velocity")
abline(result,col="red")

##residual plot
plot(result$fitted.values,result$residuals, main="Plot of Residuals against Fitted Values")
abline(h=0,col="red")
####looks like a sine wave, residuals are just variation from regression formula predictions
####what are fitted values?
####are residuals scattered across sides, no - consider transformation

##ACF plot of residuals
acf(result$residuals, main="ACF of Residuals")
####check independence of error terms 
####for all lags 1 or greater should be insignificant, blue line represents correlation between lags
####all uncorrelated, this assumption is fine

##Normal probability or QQ plot of residuals
qqnorm(result$residuals)
qqline(result$residuals, col = "red")
####if residuals follow normal distribution, points directly on the plot 
####definitely no


####linearity assumption not met, so consider transforming x
####maybe use inverse function, raise power to -1


all_plots <- function(modelx, modely) {
  #'ALL THE LM DIAGNOSTIC PLOTS, also print the LM summary
  result<-lm(modely ~ modelx)
  print(summary(result))
  # print("Coefficients of LRM: ")
  # print(coef(result))
  print("#############  Residuals vs values:  #################")
  print(summary(lm(result$residuals ~ result$fitted.values)))
  
  par(mfrow=c(2,2))
  plot(modelx,modely, main="Scatterplot")
  abline(result,col="red")
  plot(result$fitted.values,result$residuals, main="Plot of residuals against fits")
  abline(h=0,col="red")
  acf(result$residuals, main="Auto-Correlation Function of Residuals")
      #ACF: can you predict a residual based on previous residuals? assumption #3 independence
  qqnorm(result$residuals)
  qqline(result$residuals, col="red")
      #Quantile-Quantile plot
  return(result)
}
##Data in, plots out
result <- all_plots(data$wind, data$output)
result<-lm(output~wind)
library(MASS)
boxcox(result )


more_plots <- function(lm_version){
  #'ALL THE LM DIAGNOSTIC PLOTS, also print the LM summary
  library(MASS)
  print(summary(lm_version))
  par(mfrow = c(3, 2))
  plot(result$model, main = "Basic Data Scatterplot")
  abline(result,col = "red")
  plot(lm_version)
  boxcox(lm_version)
}

result<-lm(defects~weeks)
summary(result)
more_plots(result)
acf(result$residuals, main="Auto-Correlation Function of Residuals")

data$fittedDefects <- data$defects^(-0.2)
result<-lm(data$fittedDefects~data$weeks)
summary(result)
more_plots(result)
acf(result$residuals, main="Auto-Correlation Function of Residuals")




data <- read.table("defects.txt", header=TRUE ,sep="")
# result<-lm(data$defects~data$weeks)
# plot(data$weeks,data$defects, main = "Scatterplot")
# abline(result, col = "red")
# plot(result$fitted.values,result$residuals, main="Plot of residuals against fits")
# abline(h = 0, col = "red")


data$fittedDefects <- data$defects^(-0.2)
result<-lm(data$fittedDefects~data$weeks)
par(mfrow = c(1,2))
plot(data$weeks,data$fittedDefects, main = "Scatterplot")
abline(result, col = "red")
plot(result$fitted.values,result$residuals, main="Plot of residuals against fits")
abline(h = 0, col = "red")




##Data in, plots out
result <-lm(output~wind)
more_plots(result)

##Transform as in tutorial, then run all plots again
data$inv.wind<-1/data$wind
result.inv <-lm(output~inv.wind, data = data)
more_plots(result.inv)

summary(result.inv)

##boxcox function found in MASS package. Need to install MASS package first

library(MASS)
##for doing y transformations
boxcox(result.inv, lambda = seq(0.6, 1.6, 0.01))
                               #val range, increment
#is 1 inside the interval?, if raising y to power of one, not changing it. 



