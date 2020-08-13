
library(plot.matrix)
library(corrplot)

#insert data
smoking.vs.fitness <- matrix(cbind(c(113,119,77,181),c(113,135,91,152),c(110,172,86,124), c(159,190,65,73)), nrow = 4)
rownames(smoking.vs.fitness) <- c("Never smoked", "Former smoker", "1-9 cig/day", "10+ cig/day")
colnames(smoking.vs.fitness) <- c("low fitness","med-low fitness", "med-hi fitness", "hi fitness")

#basic heatmap of values in table
par(mar=c(5.1, 4.1, 4.1, 4.1)) # adapt margins
plot(smoking.vs.fitness, col=rev(heat.colors(7)))

# Null hypothesis (H0): the row and the column variables of the contingency table are independent.
# Alternative hypothesis (H1): row and column variables are dependent
chisq <- chisq.test(smoking.vs.fitness)
chisq
round(chisq$residuals, 3)

#plot the correlations between values based on residuals
par(mar=c(5.1, 4.1, 4.1, 5.1))
corrplot(chisq$residuals, is.cor = FALSE, title="Correlations Between Smoking and Fitness Levels")