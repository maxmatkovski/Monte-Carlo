'''
Implementation of Monte Carlo method to simulate stock portfolio
'''


import pandas_datareader as pdr

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


# import data

def get_data(stocks, start, end):
    stockData = pdr.get_data_yahoo(stocks, start, end)
    stockData = stockData ['Data']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

stockList = ['CBA','BHP','TLS','NAB','WBC','STO']
stocks = [stock + '.AX' for stock in stockList]

# parameter very important for covariance matrix which will affect monte carlo simulation. 
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

print(meanReturns)


# https://www.youtube.com/watch?v=6-dhdMDiYWQ&t=377s&ab_channel=QuantPy