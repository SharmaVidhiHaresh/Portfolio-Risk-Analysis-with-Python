import pandas as pd
def drawdown(return_series: pd.Series): 
    wealth_index = 1000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index- previous_peaks)/ previous_peaks
    return pd.DataFrame({
        "Wealth" : wealth_index,
        "Peaks" : previous_peaks,
        "Drawdowns" : drawdowns
    })

def get_ffme_returns():
    me_m = pd.read_csv("Desktop/Portfolios_Formed_on_ME_monthly_EW.csv",
             header= 0, index_col = 0, na_values = -99.99)
    rets = me_m[['Lo 10', 'Hi 10']]
    rets.columns = ['SmallCap', 'LargeCap']
    rets = rets/100
    rets.index = pd.to_datetime(rets.index,format="%Y%m").to_period('M')
    return rets

def get_hfi_returns():
    hfi = pd.read_csv("Desktop/edhec-hedgefundindices.csv",
                     header=0,index_col=0,parse_dates=True)
    hfi = hfi/100
    hfi.index = hfi.index.to_period('M')
    return hfi

#Returns the semideviation aka negetive semideivation of r
#r must be  a series or a dataframe
def semideviation(r):
    is_negetive= r<0
    return r[is_negetive].std(ddof=0)

def skewness(r):
    demeaned_r = r - r.mean()
    #Use the population standard deviation, so set df= 0
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**3).mean()
    return exp/sigma_r**3

def kurtosis(r):
    demeaned_r = r - r.mean()
    #Use the population standard deviation, so set df= 0
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**4).mean()
    return exp/sigma_r**4

import scipy.stats
def is_normal(r,level =0.01):
    """
    Applies the Jarque-Bera test to determine if the series is normal or not
    Test is applied at the 1% level (p-value should be 1%) by default
    Returns True if the hypothesis of normality is accepted, False otherwise 
    """
    statistic, p_value = scipy.stats.jarque_bera(r)
    return p_value > level

def var_historic(r,level= 5):
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r, level)
    else:
        raise TypeError("Expected r to be a Series or Dateframe")

#Cornish Fisher assumptions are added to Gaussian model for Var analysis:
import numpy as 
from scipy.stats import norm
def var_gaussian(r, level=5, modified = False):
    """
    Returns the Parametric Gaussian VaR of a Series or Dataframe
    If "modified" is True,then the modified VaR is required,
    using the Cornish-Fisher modification
    """
    #Compute the Z score based on the observed skewness and kurtosis
    z = norm.ppf(level/100)
    if modified: 
        #Modify the Z score based on  observed skewness and kurtosis
        s = skewness(r)
        k = kurtosis(r)
        z = (z+
               (z**2-1)*s/6+
               (z**3-3*z)*(k-3)/24 -
               (2*z**3-5*z)*(s**2)/36
            )
    return -(r.mean() + z*r.std(ddof=0))
       
def cvar_historic(r,level=5):
    """
    Compute the Conditional VaR of Series or Dataframe
    """
    ifinstance(r,pd.Series):
        is_beyond= r<= -var.historic(r,level=level)
        return -r[is_beyond].mean()
    elif isinstance(r,pd.Dataframe):
        return r.aggregate(cvar_historic, level=level)
    else:
        raise TyperError("Expected r to be a Series or Dataframe")
    
    
    
    
    










