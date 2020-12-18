import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.options.display.width = 0

class Covid():
    def __init__(self):
        pass

    def plot_data(self, par1, par2, par3, par4, par5):
        self.df1 = yf.Ticker(par1)
        self.df2 = yf.Ticker(par2)
        self.df3 = yf.Ticker(par3)
        self.df4 = yf.Ticker(par4)
        self.df5 = yf.Ticker(par5)
        # print(self.msft.info)

        self.df1 = self.df1.history(start='2019-01-01', end='2021-01-01')
        self.df2 = self.df2.history(start='2019-01-01', end='2021-01-01')
        self.df3 = self.df3.history(start='2019-01-01', end='2021-01-01')
        self.df4 = self.df4.history(start='2019-01-01', end='2021-01-01')
        self.df5 = self.df5.history(start='2019-01-01', end='2021-01-01')

        sns.lineplot(x=self.df1.index, y='Open', data=self.df1, label=par1)
        sns.lineplot(x=self.df2.index, y='Open', data=self.df2, label=par2)
        sns.lineplot(x=self.df3.index, y='Open', data=self.df3, label=par3)
        sns.lineplot(x=self.df4.index, y='Open', data=self.df4, label=par4)
        sns.lineplot(x=self.df5.index, y='Open', data=self.df5, label=par5)

        plt.show()

if __name__ == '__main__':
    covid = Covid()
    covid.plot_data('MSFT',"AAPL","GOOGL","AMZN","FB")
    covid.plot_data("PFE","MRK","JNJ",'ABBV','BMY')
    covid.plot_data("NFLX",'DIS',"SNE","CMCSA","ZM")
    covid.plot_data('UBER','IMAX','HLT','MCD','RCL')
    covid.plot_data('UAL','JBLU','RYAAY','SKYW','AAL')
    covid.plot_data('XOM','RDS-A','CVX','TOT','PTR')
    # covid.test()

