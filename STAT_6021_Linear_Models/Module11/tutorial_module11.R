data<-read.table("company.txt", header=FALSE,sep="")
colnames(data)<-c("company","industry")
attach(data)

result<-lm(company~industry)

res<-result$residuals

##PACF plot of residuals
pacf(res, main="PACF of Residuals")

##fit an AR(1) model for residuals
ar.1<-arima(res,order = c(1,0,0), include.mean = FALSE)
ar.1

##transform response and predictor
shift<-ar.1$coef
y<-cbind(as.ts(company),lag(company))
yprime<-y[,2] - shift*y[,1]
x<-cbind(as.ts(industry),lag(industry))
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
