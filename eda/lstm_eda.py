from sklearn.preprocessing import MinMaxScaler
from matplotlib.gridspec import GridSpec as GS
from matplotlib import pyplot as plt
from datetime import datetime

import tensorflow as tf
import pandas as pd
import numpy as np
import csv
import os

STOCK_DATA = 'TSLA.csv'
SENTIMENT_DATA = 'tesla_sentiment.csv'
CSV_DIR = '/Users/sb/Documents/"Csv Files"/'
STOCK_FEATURES = ['Date','Open','High','Low','Close','Adj_Close','Volume']
SENTIMENT_FEATURES = ['Date', 'freq', 'pos', 'neg', 'neu', 'comp']


# Read stock data from csv
data, dates = {}, []
with open('/Users/sb/Documents/Csv Files/TSLA.csv', 'r') as f:
    csvreader = csv.reader(f)
    
    # Skip header
    next(csvreader)
    for i, row in enumerate(csvreader):

        #Store date seperately
        date = str(row[0])
        dates.append(date)
        data[date] = [float(item) for i, item in enumerate(row[1:])] 
        
    f.close()
        
# Read sentiment data from csv
with open('/Users/sb/Documents/Csv Files/tesla_sentiment.csv', 'r') as f:
    csvreader = csv.reader(f)
    for i, row in enumerate(csvreader):
        date = str(row[0])
        
        if date in dates:
            data[date] += [float(item) for i, item in enumerate(row[1:])] 
    f.close()


features = STOCK_FEATURES + SENTIMENT_FEATURES
# Function for visual analysis
def inspect_correlation(index):
  plt.figure(figsize = (24,8))
  gs = GS(nrows = 5, ncols = 2, width_ratios = [2,1])
  gs.update(hspace = 0.0, wspace = 0.01)
  for i in range(9):
    if i < 5:
      ax = plt.subplot(gs[i,0])
      ax.set_ylim(0,1)
      ax.plot(data[:, i], label = "Price / {}".format(features[i]), alpha = 0.3, c='k')
      ax.plot(data[:, -1], alpha = 0.7, c='k')
    else:
      ax=plt.subplot(gs[:,1])
      alph = 0.1 if i!=index else 0.8
      ax.scatter(data[:, -1], data[:, i-5], label = "Closing price vs {}".format(cols[i-5]), alpha=alph)
      ax.axis([0,1,0,1])
    plt.legend(loc=3, fontsize=8 )
    plt.grid()
# Using, 5, 6, 7, or 8 as an input, this function highlights the relationship between our various features and closing price
inspect_correlation(6)