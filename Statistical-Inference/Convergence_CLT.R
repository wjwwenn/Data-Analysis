# ILLUSTRATE CONVERGENCE IN DISTRIBUTION (CONVERGENCE IN PROBABILITY)
# CLT
# Generating sampling distribution of sample mean (100k obs per sample size)
for(sample.size in seq(2,40,2)){
  z=numeric(10000)
  for(i in 1:10000){
    x=rlnorm(sample.size) 
    z[i]=(mean(x)-exp(0.5))/sqrt((exp(1)-1)*exp(1))*sqrt(sample.size)    
  }
  # Plotting the empirical CDF and the normal CDF
  lnorm_cdf=ecdf(z)
  plot(lnorm_cdf, z,xlim=c(-5,5),ylim=c(0,1 ),xlab="Standarized sample means"
       ,main=paste("sample size=",sample.size),sub="CDF of the sample means")
  par(new=TRUE)
  title(main="")
  curve(pnorm(x), col="red",  from=-5, to=5,xlim=c(-5,5),ylim=c(0,1 ),
        ylab="cumulative probability",lwd = 2 ,add = TRUE)
  Sys.sleep(.5)
}


