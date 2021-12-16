import yahoo_finance

yahoo = yahoo_finance.Share("YHOO")
print(yahoo.get_open())