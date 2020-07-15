
calculate_sampledist_zscore_AUC <- function(chart_title, title_text, original_SD, sample_mean, sample_size, lower_bound, upper_bound) {
  
  #calculate sampling distribution (sample standard deviation?) for the sample mean given sample size
  ssd = original_SD / sqrt(sample_size)
  #SD = how far away from the mean are all the values
  print(paste("sampling distribution for sample mean: ", ssd, "   (unclear if used as standard deviation in calcs)"))
  
  #get z score - exact quantity of sample standard deviations from the sample mean (or pop SD from pop avg)
  zscore = (upper_bound - sample_mean)/ssd
  print(paste("zscore: ", zscore))
  
  #use pnorm to calculate area under curve, given a Z score
  #pnorm(0.233)
  curve <- pnorm(upper_bound, mean=sample_mean, sd=ssd) - pnorm(lower_bound, sample_mean, ssd)
  print(paste("area under the curve: ", curve))
  
  #add a fancy graph as well
  x <- seq(-4, 4, length=200)*ssd + sample_mean #generate sequence of numbers around given mean multiplied by SD
  hx <- dnorm(x, sample_mean, ssd) #normal distribution line based on sequence above
  plot(x, hx, type="n", ylab="frequency", xlab=chart_title, main = "Normal Distribution", axes=FALSE) #plot line sequence created above, w titles
  
  lines(x, hx) #add lines for original sequence and norm dist
  i <- x >= lower_bound & x <= upper_bound #generate boolean sequence based on bounds
  upperlineseq <- c(lower_bound,x[i],upper_bound) #using boolean sequence, filter sequence of numbers generated above, append bounds
  lowerlineseq <- c(0,hx[i],0) #using boolean sequence, filter norm dist line vals, append bounds
  polygon(upperlineseq, lowerlineseq, col="black") #add polygon to plot, with specified color
  
  area <- pnorm(upper_bound, sample_mean, ssd) - pnorm(lower_bound, sample_mean, ssd) #calculate area under the curve, as above
  result <- paste("P(",lower_bound,"< ",title_text," <",upper_bound,") =", signif(area, digits=3)) #generate text to title_textribe upper_bound point
  mtext(result,1)  #Write Text Into The Margins Of A Plot; on which side of the plot (1=bottom, 2=left, 3=top, 4=right)
  axis(side=1, at=seq(40, 160, 20), pos=0) #add axis; side=as above, at=the points at which tick-marks are to be drawn
  print('')
}
                            #original_SD, sample_mean, sample_size, lower_bound, upper_bound
chart_title <- "Meta-analysis of Textbook Cost Sample Means"
single_sample_name <- "Textbook cost Sample Mean"
#calculate_sampledist_zscore_AUC(chart_title, single_sample_name, 210.58, 405.17, 25, 0, 415)
calculate_sampledist_zscore_AUC("cherry tomato machine", "cherry tomato pack", 1.5, 226.5, 40, 0, 227)
#calculate_sampledist_zscore_AUC(title, 210.58, 405.17, 50, 400, 1000)




####Estimate Population Mean####

#confidence intervals: estimate range of plausible values of unknown parameter due to uncertainty
#estimate +- margin of error, 1 - alpha (significance level), 0.95 considered standard

confidence_intervals <- function(alpha=0.05, sample_SD, sample_size) {
  multiplier = (1-(alpha / 2))
  print(paste("multiplier:   ",multiplier))
  print(paste("AKA ",(multiplier * 100), "th percentile value in normal distribution", sep=""))
  SD_of_estimate = sample_SD/(sqrt(sample_size))
  margin_of_error = multiplier * SD_of_estimate
  print(paste("margin of error:   ", margin_of_error))
  zscore <- qnorm(multiplier)
  print(paste("zscore for curr alpha/multiplier:  ", zscore))
}

confidence_intervals(0.05, 226.5, 40)

confidence_intervals(0.1, 210.58, 25)
confidence_intervals(0.02, 210.58, 25)
confidence_intervals(0.01, 210.58, 25)


################################################################################

library(datasets)
library(pastecs)

smean <- mean.default(Loblolly$height, na.rm = TRUE)
data <- transform(Loblolly, dist_from_mean = (Loblolly$height - smean) ^ 2)
n <- nrow(Loblolly) 
degrees_of_freedom <- n - 1 #K, describes t distribution
  #t distribution is like normal curve but too few samples, wider spread, as degrees of freedom increase -> more like normal curve
st_dev <- sd(data$height)
sample_variance <- sum(data$dist_from_mean) / degrees_of_freedom
standard_error_of_sample_mean <- st_dev / sqrt(n)

stat.desc(Loblolly$height)

library(distributions3)

t.test(Loblolly$height, conf.level = 0.95)

t_multiplier <- function(pct_confidence) {
  alpha <- 1 - pct_confidence
  t_multiplier <- 1 - (alpha / 2)
  print(paste("t multiplier: ", t_multiplier))
  return(t_multiplier)
}
qt(t_multiplier(0.90), 10)
qt(t_multiplier(0.92), 35)
qt(t_multiplier(0.98), 50)

# we use s to estimate σ when it is unknown 

n <- 40
sample_mean <- 226.5
sample_SD <- 1.5
confidence_int <- 0.95 
test_val <- 227
#hypothesis statement: is the population mean (μ) for the distribution of weights of cherry tomato packages different from 227g?
#Null hypothesis H0: μ = 227g ### statement of "no effect/relationship" or "no difference"
#Alt hypothesis Ha: μ ≠ 227g  (two sided test, used if trying to simply check factuality)
#Alt hypothesis Ha: μ < 227g  (one sided test, used if trying to prove insufficiency) 
#Alt hypothesis Ha: μ > 227g  (one sided test, used if trying to prove overshooting)

deg_free <- n - 1
qt(t_multiplier(confidence_int), n)
bound_lower <- sample_mean - (qt(confidence_int, deg_free) * (sample_SD / sqrt(n)))
bound_upper <- sample_mean + (qt(confidence_int, deg_free) * (sample_SD / sqrt(n)))
print(paste("we're ",confidence_int,"% sure the pop mean is between ", signif(bound_lower, 4), " and ", signif(bound_upper, 4)))
if( bound_lower <=  test_val & test_val <= bound_upper ) {
  print(paste("test value ",test_val," is within the bounds"))
} else {
  print(paste("test value ",test_val," is outside the bounds"))
}

#probability that patterns are a real feature and not due to chance 

alpha <- 0.1 
deg_free <- 10
crit_val <- qt(alpha, deg_free) #quantile function, one sided
crit_val_2s <- abs(qt(alpha/2, deg_free)) #two sided

###
  
