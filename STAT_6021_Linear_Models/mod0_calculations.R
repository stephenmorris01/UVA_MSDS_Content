#Basic value assumptions
descr = "Textbook cost"
originalSD = 210.58
smean = 405.17
samplesize = 25

#calculate sampling distribution (standard deviation?) for the sample mean given sample size
ssd = originalSD / sqrt(samplesize)
ssd

lb=0; ub = 415

#get z score
zscore = (ub - smean)/ssd
zscore

#use pnorm to calculate area under curve, given a Z score
#pnorm(0.233)
curve <- pnorm(ub, mean=smean, sd=ssd)
curve

#add a fancy graph as well
x <- seq(-4, 4, length=100)*ssd + smean
hx <- dnorm(x, smean, ssd)

plot(x, hx, type="n", xlab=descr, main = "Normal Distribution", axes=FALSE)

i <- x >= lb & x <= ub
lines(x, hx)
polygon(c(lb,x[i],ub), c(0,hx[i],0), col="red")

area <- pnorm(ub, smean, ssd) - pnorm(lb, smean, ssd)
result <- paste("P(",lb,"< ",descr," <",ub,") =", signif(area, digits=3))
mtext(result,3)
axis(1, at=seq(40, 160, 20), pos=0)
