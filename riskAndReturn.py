# David Crawford - Risk and Return calculation

# The expected return of an asset is the sum of the probability of each state occurring
# times the rate of return if that state occurs
def _expectedReturnPortfolio(probability_times_rate_of_return):
    expected_return_portfolio = 0
    for pTr in probability_times_rate_of_return:
        beta_sub_portfolio += pTr
    return beta_sub_portfolio

def _probabilityTimesRateOfReturn(probability, rate_of_return):
    return probability*rate_of_return

def _variance(probability, rate_of_return, expected_return):
    return probability*((rate_of_return - expected_return)**2)

def _standardDeviation(total_variance):
    return total_variance**(0.5)

def _weightTimesBeta(weight, beta):
    return weight*beta

# The beta of a portfolio is the sum of the weight of each asset times the beta of each asset
def _betaSubPortfolio(betas):
    beta_sub_portfolio = 0
    for wTb in betas:
        beta_sub_portfolio += wTb
    return beta_sub_portfolio

# CAPM
def _expectedReturnCAPM(risk_free_rate, beta, expected_return_market):
    return risk_free_rate + (beta*(expected_return_market-risk_free_rate))

def _betaCAPM(expected_return, risk_free_rate, expected_return_market):
    return (expected_return - risk_free_rate)/(risk_free_rate - expected_return_market)

def _expectedReturnMarketCAPM(expected_return, risk_free_rate, beta):
    return ((expected_return - risk_free_rate)/beta) + risk_free_rate

def _riskFreeRateCAPM(expectedReturn, beta, expected_return_market):
    return (expectedReturn - (expected_return_market*beta))/(1 - beta)
