
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