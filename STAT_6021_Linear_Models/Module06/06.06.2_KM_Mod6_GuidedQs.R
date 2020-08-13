data <- read.table("cereals.txt", header=TRUE ,sep="")
attach(data)

is.numeric(data$mfr)

mfr<-factor(data$mfr)

contrasts(mfr)

levels(mfr) <- c("General Mills", "Kellogg's", 'Other')
contrasts(mfr)

#could set diff ref class, but not this one
mfr<- relevel(mfr, ref = "General Mills")

#let each category be a subset
m1<-subset(data,mfr=="G")
m2<-subset(data,mfr=="K")
m3<-subset(data,mfr=="other")

#fit 3 sep regressions, one for each mfr
reg1<-lm(calories~sugars, data=m1)
reg2<-lm(calories~sugars, data=m2)
reg3<-lm(calories~sugars, data=m3)

# (1) 
par(mfrow = c(1, 1))
plot(sugars,calories, main="Calories against Sugar")
points(m2$sugars,m2$calories, pch=2, col="red")
points(m3$sugars, m3$calories, pch=12, col="blue")
abline(reg1, lty=1)
abline(reg2, lty=2, col="red")
abline(reg3, lty=3, col="blue")
legend("topleft", c("General Mills", "Kellogg's", 'Other'), lty=c(1,2,3), pch=c(1,2,12), col=c("black", "red", "blue"))

# difference in slopes could be due to random sampling, not to a true difference in population


# (2)
#if slopes look different, maybe interaction between predictors
#to fit interaction, use multiply instead of plus
result<- lm(calories~sugars*mfr)
summary(result) # interaction terms look insignificant, maybe drop?


# (3)
reduced<- lm(calories~sugars+mfr)
summary(reduced)
anova(reduced, result)
#f statistic and p value pretty big, don't need interaction terms. Consider simpler model without interactions


# (4) checking assumptions with graphs and Levine
#now fit reduced model with no interaction

par(mfrow = c(2, 2))
plot(reduced$fitted.values, reduced$residuals,main="Residual Plot") #looks good
abline(h=0,col="red")
acf(reduced$residuals) #mostly looks good, but there are some lag correlations, worth considering
qqnorm(reduced$residuals)
qqline(reduced$residuals,col="red") #looks "good enough", though with some tail end variation
#also check if variance of response same for every class of categorical predictor
boxplot(calories~mfr,main="Boxplot") #is variance of response same for each class? NO
#Inappropriate to use a model that incorporates the interaction effects
#ideally range would look pretty similar - just graphical summary, won't be perfect


##levene's test (hypothesis test) of equality of variances
library(lawstat)
levene.test(calories,mfr)
# Modified robust Brown-Forsythe Levene-type test based on the absolute deviations from the median
# 
# data:  calories
# Test Statistic = 2.6938, p-value = 0.07425
# variance presumed to b e the same?

#p-value only just too big, equality of variances might not be fine

summary(reduced)
#Kellogg's and Other cannot be compared to General Mills, when controlled for calories



#(5)

library(multcomp)
pairwise <- glht(reduced, linfct = mcp(mfr = "Tukey")) #Tukey is procedure that is done
summary(pairwise)

# Testing if difference in estimates of mean response are big enough to say they're different
# We might expect that GM has very different slope, but insignificant difference

# Be sure to contextually interpret the results of these hypothesis tests 
# to someone who doesn't know statistics.
# 
# We see slopes, suspect interactions, tested that and rejected null. 
# We can contribute variation in slopes to randomness, epsilon error term. 
# Avg y (calories) across manufacturers not that different, holding sugar equal. 
# Estimate is difference based on sample. 
# 
# Fail to reject: no evidence they are different.Probably due to randomness.
# 
# Tukey's test can only be done without interactions. 
# 
# Levine's test is to see if variance in mean response (holding extra factor constant) 
# is different across categories. Even if interaction.