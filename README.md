# Portfolio & Investment Analysis with Python

## Return Analysis:
There is has been enough evidence that stock returns and hedge fund indices are not normally distributed. Thus,the Gaussian model cannot be applied without considering for the skewness and kurtosis.							
Module covers extraction of returns from a csv file, and then computation of volitality,the skewness and kurtoisis of the returns for each fund.
$$ S(R)= \frac{E[ R-E(R)^3 ]}{\sigma_R^3} $$
Kurtotic - A statistical measure that defines how heavily the tails of a distribution differ from the tails of a normal distribution							
Implication: positive excess kurtosis and the negative skewness suggest that large losses are likely


## Risk analysis:
The modules assesses and analyzes risk of respective funds by the computating  maximum drawndown and VaR analysis.

  ### Maximum Drawndown Analysis:
  Maximum Drawdown is the maximum loss from the previous high to the subsequent low.Alternatively, drawdown can be also measured in terms of the longest period the secuirty has gone between two peak prices.A4

  ### Value at risk modelling:
  Value at risk (VaR) is a measure of the risk of loss for investments. It estimates how much a set of investments might lose (with a given probability), given normal market conditions, in a set time period such as a day.
  The value at risk can be assessed with four approaches:
  #### Historic (Non-parametric)
  #### Parametric Gaussian Model
  #### Cornish-Fisher (Semi-Parametric)

  

