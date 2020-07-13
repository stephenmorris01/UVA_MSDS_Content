dataset <- read.delim("D:\\Git\\UVA_MSDS_Content\\STAT_6021_Linear_Models\\bp.txt", 
                      header = TRUE, sep = "", na.strings ="", stringsAsFactors= F)

#1. Create a scatterplot for this data set.
plot(dataset$weight, dataset$BP, main="Weight vs Blood Pressure",
     xlab="weight", ylab="BP", pch=8)

#2. Perform a simple linear regression for systolic blood pressure against weight.
linearMod <- lm(BP~weight, data=dataset)  # build linear regression model on full data
print(linearMod)


#3. For a 30-year-old male whose weight is 200, what is his predicted systolic 
#  blood pressure? What is his residual?
pred_BP <- (200 * 0.4194) + 69.1044
pred_BP
#152.9844
coef(linearMod)
summary(linearMod)
#residual = ~4 NEGATIVE MINUS PREDICTTED

calc_residual <- function(df, value_of_interest){
  #' input must be two columns in order x, y. Will attempt to lookup example value, or else will calculate estimate. 
  library(dplyr)
  col1 <- colnames(df)[1]
  col2 <- colnames(df)[2]
  form_tilde <- colnames(df) %>% paste(.[1],"~",.[2],sep = "")
  linmod <- df %>%  lm(as.formula(form_tilde), .) #
  lkp <- as.numeric(filter_at(df, 1, all_vars(. == value_of_interest))[2])
  output <- lkp - (coef(linmod)[1] + value_of_interest * coef(linmod)[2])
  return(output)
}
calc_residual(dataset, 200)


#4. Produce the ANOVA table for this linear regression.
anova(linearMod)

#5. What is the value of R2?


# SD of errors >- sample SD of our residuals 
# * what are residuals = 8.681 how far datapoints are from regression
# 
# theta hat == S(sigma) 
# it's not a theta, it's Sigma 
# 
# beta 1 hat refers to slope 
# beta zero hat is the intercept 
