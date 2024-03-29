# You can write code above the if-main block.
if __name__ == '__main__':
    # You should not modify this part, but additional arguments are allowed.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')

    parser.add_argument('--output',
                        default='submission.csv',
                        help='output file name')
    args = parser.parse_args()
    
    # The following part is an example.
    # You can modify it at will.
    import pandas as pd
    df_training = pd.read_csv(args.training)
    #model = Model()
    #model.train(df_training)
    #df_result = model.predict(n_step=7)
    #df_result.to_csv(args.output, index=0)

    # -*- coding: utf-8 -*-
    """datascience_hw1.ipynb

    Automatically generated by Colaboratory.

    Original file is located at
        https://colab.research.google.com/drive/12RbTWodnvuYtnWZW1CkcKHIdkeGF6Nsp
    """

    '''from google.colab import drive
    import os
    drive.mount('/content/drive')

    os.chdir('/content/drive/MyDrive/資料競程') #切換該目錄
    os.listdir() #確認目錄內容'''

    # Commented out IPython magic to ensure Python compatibility.
    import os
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    import seaborn as sns
    from fbprophet import Prophet
    from sklearn import metrics
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    from matplotlib import pyplot

    # %matplotlib inline
    df_train = df_training
    '''for dirname, _, filenames in os.walk('/content/drive/MyDrive/資料競程'):
        for filename in filenames:
            print(os.path.join(dirname, filename))'''

    '''df_energy_1 = pd.read_csv(
        '近三年每日尖峰備轉容量率.csv', 
    )
    df_energy_2 = pd.read_csv(
        '本年度每日尖峰備轉容量率.csv', 
    )'''

    '''df_concat = pd.concat([df_energy_1,df_energy_2],axis=0,ignore_index = True)
    df_concat.columns = ['日期','備轉容量(MW)','備轉容量率(%)']
    df_concat['備轉容量(MW)'] = df_concat['備轉容量(MW)']*10

    df_concat.head()

    df_concat.describe().round(2)

    df_concat.info()'''

    # The 'time' column, which we also want to function as the index of the observations in a time-series, has not been parsed correctly and is recognized as an object.
    # Convert time to datetime object and set it as index
    '''df_concat['日期'] = pd.to_datetime(df_concat['日期'], infer_datetime_format=True)'''
    #df_concat = df_concat.set_index('日期')

    # Find NaNs and duplicates in df_concat

    '''print('There are {} missing values or NaNs in df_concat.'
          .format(df_concat.isnull().values.sum()))

    temp_energy = df_concat.duplicated(keep='first').sum()

    print('There are {} duplicate rows in df_concat based on all columns.'
      .format(temp_energy))'''

    '''df_train = pd.DataFrame(columns=['日期',
                '備轉容量(MW)',
                '備轉容量率(%)'])
    for i in df_concat.index:
        if df_concat.loc[i]['日期'].month == 1 or df_concat.loc[i]['日期'].month == 2 or df_concat.loc[i]['日期'].month == 3 or df_concat.loc[i]['日期'].month == 4:
            df_train = df_train.append(df_concat.loc[i],ignore_index = True)
    print(df_train)'''

    # Define a function to plot different types of time-series
    '''df_concat = df_concat.set_index('日期')
    def plot_series(df=None, column=None, series=pd.Series([]), 
                label=None, ylabel=None, title=None, start=0, end=None):
        """
    Plots a certain time-series which has either been loaded in a dataframe
    and which constitutes one of its columns or it a custom pandas series 
    created by the user. The user can define either the 'df' and the 'column' 
    or the 'series' and additionally, can also define the 'label', the 
    'ylabel', the 'title', the 'start' and the 'end' of the plot.
    """
        sns.set()
        fig, ax = plt.subplots(figsize=(30, 12))
        ax.set_xlabel('Time', fontsize=16)
        if column:
            ax.plot(df[column][start:end], label=label)
            ax.set_ylabel(ylabel, fontsize=16)
        if series.any():
            ax.plot(series, label=label)
            ax.set_ylabel(ylabel, fontsize=16)
        if label:
            ax.legend(fontsize=16)
        if title:
            ax.set_title(title, fontsize=24)
        ax.grid(True)
        return ax
    ax = plot_series(df=df_concat, column='備轉容量(MW)', ylabel='operating reserve (MW)',
                 title='operating reserve curve', end=1183)
    plt.show()'''

    #new_df_train = df_train.drop(df_train.index[-14:])
    new_df_train = df_train

    print(new_df_train.tail())

    new_df_train = new_df_train.set_index('日期')
    new_df_train = pd.DataFrame(new_df_train['備轉容量(MW)']).reset_index().rename(columns={'日期':'ds', '備轉容量(MW)':'y'})
    new_df_train.head()

    # 定義模型
    model = Prophet(daily_seasonality=True)

    # 訓練模型
    model.fit(new_df_train)

    # 建構預測集
    future = model.make_future_dataframe(periods=16) #forecasting for 1 year from now.

    # 進行預測
    forecast = model.predict(future)

    #forecast.head()

    forecast.tail(15)

    figure=model.plot(forecast)

    '''date=[]
    date.append(pd.DatetimeIndex(forecast['ds'].tail(16)).date)
    energy=[]
    energy.append(forecast['yhat'].tail(16).values)
    print("date,operating_reserve(MV)")'''
    '''for i in range(1,16):
     print('{date},{energy}'.format(date=date[0][i], energy=energy[0][i]))'''
    output = pd.DataFrame(columns=['ds','yhat'])
    output = forecast[['ds','yhat']].tail(15)
    output.columns = ['date','operating_reserve(MV)']
    print(output)
    output.to_csv("submission.csv", index=False)

    '''y_true = df_train['備轉容量(MW)'][-14:].values
    y_pred = forecast['yhat'].tail(14).values
    rmse = sqrt(mean_squared_error(y_true, y_pred))
    print('RMSE: %.3f' % rmse)'''

    '''pyplot.plot(y_true, label='Actual')
    pyplot.plot(y_pred, label='Predicted')
    pyplot.legend()
    pyplot.show()'''

    #!pip freeze > requirement.txt

