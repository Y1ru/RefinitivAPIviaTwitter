import eikon as ek
import asyncio as asyncio
from IPython.display import display
import pandas as pd
import twitter

print("Python will now attempt to submit tweets to twitter...")

print("Connecting to Twitter API")
#Twitter API https://github.com/bear/python-twitter
api = twitter.Api(consumer_key='HIDDEN',
                      consumer_secret='HIDDEN',
                      access_token_key='HIDDEN',
                      access_token_secret='HIDDEN')

print("Connecting to Refinitiv API")
ek.set_app_key('HIDDEN')

streaming_prices = ek.StreamingPrices(
    instruments = ['BTC=', '.SPX', 'SPY', 'VXX', 'TLT.O', 'GLD', 'SLV', 'BBY'],
    fields   = ['CF_LAST', 'CF_BID','CF_ASK','OPEN_PRC', 'CF_HIGH','CF_LOW', 'CF_CLOSE', 'TR.TSVWAP', 'OPINT_1', 'OPINTNC']
)

streaming_prices.open()

df = streaming_prices.get_snapshot(
    instruments = ['BTC=', '.SPX', 'SPY', 'VXX', 'BBY'],
    fields   = ['CF_LAST','OPINTNC','OPINT_1']
)

status = api.PostUpdate("{0}".format(df))

print("Tweets submitted successfully!")

streaming_prices.close()






