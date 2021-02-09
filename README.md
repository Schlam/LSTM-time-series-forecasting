# Forecast bitcoin with deep learning

![forecast](/images/btc_forecast.png)
________________________________________________________________________________

## What the model does

Unlike previous renditions of this project, this model predicts behavior using the
historical data alone. The performance benefit of synchronizing sentiment with
stock trends in the multivariate analysis was found to be nominal relative to the
cost in data complexity, and far outweighed by the potential for adversarial
attack.

**Why historical data only?**

After inspecting the reddit data used, it became clear that some agent was
spamming "I love bitcoin :)" in a way that was clearly inorganic. The signal to
noise ratio in the sentiment data is unclear, but there are ways to combat this
problem.

## Update: Portability

Unlike the previous rendition, this uses ```pandas_datareader``` to pull
historical data from Yahoo Finance, allowing this project to be modified and
trained on any stock/cryptocurrency.

## Results

![forecast](/images/btc_forecast2.png)

It seems the model is not overfitting, and capturing the general trend quite well.

## Reflections

Perhaps a discriminator could be trained to identify posts which are
likely not created by authentic human users.
