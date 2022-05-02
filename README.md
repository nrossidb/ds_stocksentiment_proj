# ds_stocksentiment_proj
Repo for the data science GME stock sentiment analysis project

Going to work on this in phases. Current phase is incredibly simple and just a proof of concept. Several things need to be changed/updated/added to make this a more viable project:

1. Currently pulls in a very limited amount of information. I purposefully set it to pull in a low number of tweets just to test the functionality and not go crazy with my API usage. I will need a much larger dataset for an accurate measurement.
2. I need to pull tweets over a specified time period. My goal is to observe the sentiment during key periods of time like before, during, and after earnings reports. Some recent earnings reports had resulted in a large increase in stock price and I want to see if there was any correleation in social sentiment and the stock price. It currently only pulls in several recent tweets and measures sentiment.
3. I need to pull in financial information for the stock and compare sentiment to stock performance over a specific timeframe. Need to pick which API to use and set up visualization
