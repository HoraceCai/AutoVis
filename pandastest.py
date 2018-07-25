import pandas as pd
from pandas_datareader import wb
import matplotlib.pyplot as plt



mathces = wb.search('gdp.*capita.*const')

dat = wb.download(indicator='NY.GDP.PCAP.KD', country='CN', start=2010, end=2017)

data = dat.stack()
print(data)
data.plot(kind ='line')
plt.show()