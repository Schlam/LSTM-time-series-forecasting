# deep-hodl
Another attempt at making sense of madness (predicting cryptocurrency behavior) using bidirectional LSTM layers and convolutions (multi head self attention layer coming soon)

![forecast](/images/btc_forecast.png)

Unlike the model found [here](https://github.com/Schlam/LSTM-time-series-forecasting) this predicts behavior using the historical data alone. The performance benefit of synchronizing sentiment with stock trends in the multivariate analysis is nominal and certainly outweighed by the potential for adversarial attack (after inspecting the reddit data used, I noticed some agent was spamming "I love bitcoin :)" in intervals for reasons unknown.) The signal to noise ratio isn't what I'd hoped, but in almost any other context this problem is not as prevelant and seems to be mainly a bitoin thing.

![forecast](/images/btc_forecast2.png)

### Plug and Play
Unlike the previous rendition, this uses ```pandas_dataloader``` to grab historical data from Yahoo Finance, and is ready to be trained on any stock and certain cryptocurrencies

### Coming soon
The rise of Transformers and attention-based models in general has led text classification and language understanding to new heights, and researchers at Google have demonstrated their effectiveness in time series forecasting (link to the arxiv pdf [here](https://arxiv.org/pdf/2001.08317.pdf)).