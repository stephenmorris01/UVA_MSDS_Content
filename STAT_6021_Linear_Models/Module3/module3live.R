
setwd("C:/Users/joony/Documents/R")


library("tidyverse")

data <- read.table(file="defects.txt",header=T, stringsAsFactors =F, sep="")
attach(data)


# 1. Plot defects, the average number of defects per 10,000 bottles, against weeks, the
# number of weeks since the last furnace overhaul. Comment on the appearance of
# the plot. Do any assumptions or conditions for simple linear regression appear to be
# violated? If so, which ones?
  
title = "Defects VS. Weeks"
xlab = "weeks"
ylab ="defects"
x = weeks
y = defects

# Produce a plot. 
plot(x, y, main=title, xlab=xlab, ylab=ylab)
# Yes, first one. The plot is not linear 





# 2. Create a residual plot. Describe the appearance of the graph of residuals versus fitted
# values, and comment if assumptions are not met for simple linear regression.
lmod <- lm(defects~weeks)
plot(lmod$fitted.values,lmod$residuals, main="Plot of Residuals against Fitted Values")
abline(h=0,col="red")
# The error terms does not have constant varince? (3)
# we can see the non linear relationship in this graph also







# 3. Based on your answers to parts 1 and 2, do we need to transform at least one of the
# variables?

# yes



# 4. One of your classmates says that since she is not sure if the variance is constant, she
# should use the Box-Cox method to see if the response variable should be transformed
# first. Do you agree with her idea? Briefly explain.

# not sure because I would like to see the residuals plot after we use correct linear relationship





# 5.  Regardless of your answer to part 4, use R to produce a plot of the profile log-likelihoods
# for the parameter, λ, of the Box-Cox power transformation. What transformation, if
# any, would you apply to the response variable? Briefly explain.
# install.packages("MASS")
library(MASS)
boxcox(lmod)
boxcox(lmod, lambda = seq(-1, 1, 0.01))
lam <- -0.2
# it seems that reducing the response power to -0.2 would be appropriate



# 6.  Apply the transformation you specified in part 5. Then fit another simple linear regression model and produce the residual plot to assess if the assumptions are met.
fixedY <- y^lam
lmod <- lm(fixedY~weeks)
plot(lmod$fitted.values,lmod$residuals, main="Plot of Residuals against Fitted Values")
abline(h=0,col="red")
# the variance looks more constant 








# 7.  Create an ACF plot of the residuals. Comment if assumptions are not met for simple
# linear regression.
acf(lmod$residuals, main="ACF of Residuals")
# assumptions are met for SLR






# 8. Create a QQ plot of the residuals. Comment if assumptions are not met for simple
# linear regression.
qqnorm(lmod$residuals)
qqline(lmod$residuals, col="red")
# the errors do not follow a Normal distribution towards the each end
