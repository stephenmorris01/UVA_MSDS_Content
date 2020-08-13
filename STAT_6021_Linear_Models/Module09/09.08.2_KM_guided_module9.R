
### QUESTION 1 ###
##################
data<-read.csv("wcgs.csv", header=TRUE, sep=",")
attach(data)
summary(data)

#data$chd69 <- as.logical(data$chd69)

par(mfrow = c(2, 2))
boxplot(age~chd69) #higher risk with age
boxplot(sbp~chd69) #only slightly higher risk with sbp
boxplot(dbp~chd69) #also only slightly higher risk with dpb
boxplot(ncigs~chd69) #much higher risk w more cigarettes per day



### QUESTION 2 ###
##################

#generalized linear model        could use for LRM, "gaussian" as family
#lm() uses least squares
model <- glm(chd69 ~ age + sbp + dbp + ncigs, family = binomial("logit"))
summary(model)

coef <- model$coefficients
(eqn <- paste("y =", paste(round(coef[1],4), paste(round(coef[-1],4), names(coef[-1]), sep=" ", collapse=") + ("), sep=" + ("), ") + e"))

#dbp not significant, sbp significant but not highly
#age and moreso cigs are highly sig
#z value of dbp is less than 2, so along w p can throw it out

# Is model useful?
1-pchisq(model$null.deviance-model$deviance,3)
    #0 --  p-value is highly significant, not surprising w 2 sig. predictors

#AIC == estimator of out-of-sample prediction error and thereby relative quality of statistical models for a given set of data. Way to select a good model. 
#AIC estimates the "relative amount of information lost by a given model", the less information a model loses, the higher the quality.
#
#Z value == test-statistic for the Wald-test that the parameter is 0
#   parameter / SE. If null hypothesis is true (parameter==0), z statistic of many random samples would form normal distribution
#   if the z value is too big, indicates true regression coefficient is not 0, and corresponding chi variable matters
#   general cutoff of 2 -- approximates 2-sided hyp. test w 0.05 alpha
#   if z value less than 2, not enough evidence that variable matters


### QUESTION 3 ###
##################

#In context ncigs is highly significant, both by p value, and by z value
#coefficient for ncigs means:
#   all others being equal, in this sample, on average
#   1 extra cig per day --> 2.419% increased risk of developing coronary heart disease
exp(0.024193)
#predicted odds increase by a multiplication of 1.024488

### QUESTION 4 ###
##################
case_df <- data.frame(age=45,sbp=110,dbp=70, ncigs=0)
pred_case <- predict(model, case_df, interval="predict") 

case2_df <- c(1, 45,110,70, 0) #prediction entries, first is 1 for intercept
case2_result <- sum(coef(model)*case2_df) #sum of first * coefficients -> estimate
      #same as predict(model, case_df, interval="predict") 
      #-3.430695   #model prediction (betas multiplication)

raisedval <- exp(case2_result) #exp of estimate
# raisedval == exp(-9.119553453 + (0.066601727 * 45) + (0.019464179*110) + (0.007867445*70) + (0.024192858 *0))
#     0.03236444  ##odds

est_pi_success = raisedval / (1+raisedval)
print(est_pi_success) #0.03134982 -- est. probability

odds_success <- (est_pi_success / (1-est_pi_success))
print(odds_success) #0.03236444 -- est. odds


### QUESTION 5 ###
##################
reduced<-glm(chd69 ~ ncigs, family = "binomial")
summary(reduced)

#Null == full model not better, betas == 0, can remove
#alt == tested betas != 0, must not remove

#is full model better than reduced?
#delta g squared
1-pchisq(reduced$deviance-model$deviance,2)
    # p-value highly significant, have to reject null and keep tested betas



### QUESTION 6 ###
##################
library(aod)
#null == variable impact on model = 0

#################################
##### No formula needed, just p-value for coefficient in original glm####
#################################
wald.test(b = coef(model), Sigma = vcov(model), Terms = 4) #dbp
  # Chi-squared test:
  # X2 = 0.61, df = 1, P(> X2) = 0.43
  # not significant, fail to reject null, remove variable

wald.test(b = coef(model), Sigma = vcov(model), Terms = 2) #age
  # Chi-squared test:
  # X2 = 32.2, df = 1, P(> X2) = 1.4e-08
  #   highly significant

wald.test(b = coef(model), Sigma = vcov(model), Terms = 5) #cigs
# Chi-squared test:
# X2 = 34.2, df = 1, P(> X2) = 4.9e-09
#     highly significant


### QUESTION 7 ###
##################
model_nobp <-glm(chd69 ~ age + ncigs, family = binomial("logit"))
summary(model_nobp)

#is full model better than reduced?
#delta g squared
1-pchisq(model_nobp$deviance-model$deviance,2)
# 1.645085e-08
# p-value highly significant, have to reject null and keep tested betas



### QUESTION 8 ###
##################
# keep age, ncigs, and sbp -- leave out dbp
