import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fbprophet import Prophet

pd.options.display.width = 0
class Covid():
    def __init__(self):
        pass
    def get_data(self, path):
        self.df = pd.read_csv(path)
        print(self.df.head())
        self.cols = []
        for i in list(self.df):
            if i.startswith('1'):
                self.cols.append(i)
        print(self.cols)
        self.df = self.df.melt(id_vars=['Province/State','Country/Region','Lat','Long'], value_vars=self.cols)
        self.df =  self.df.groupby('variable').agg({'value':'sum'}).reset_index()
        self.df['date'] = pd.to_datetime(self.df['variable'], infer_datetime_format=True)
        self.df = self.df.drop(['variable'],axis=1).sort_values(by='date',ascending=True)
        print(self.df.head(20))
        print(self.df.tail(20))

        print(self.df.shape)
        return self.df

    def prophet(self, df):
        df = df.rename(columns = {'value':'y','date':'ds'})
        # df['cap'] = 100000
        print(df.head())
        self.m = Prophet(yearly_seasonality = True, seasonality_prior_scale=0.1)
        self.m.fit(df)

        self.future = self.m.make_future_dataframe(periods=500)
        self.future.tail()
        # self.future['cap'] = 100000
        self.forecast = self.m.predict(df[['ds']])
        self.m.plot_components(self.forecast)
        # self.m.plot(self.forecast)
        plt.show()

if __name__ == '__main__':
    covid = Covid()
    confirmed = 'data/confirmed.csv'
    deaths = 'data/deaths.csv'
    recovered = 'data/recovered.csv'
    df = covid.get_data(recovered)
    covid.prophet(df)


    # covid.deaths()