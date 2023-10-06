from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
from io import BytesIO
import base64
plt.switch_backend('Agg')
csv_path = "weathers/data/austin_weather.csv"

def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df' : df,
    }
    return render(request, "problem1.html", context)



def problem2(request):
    df = pd.read_csv(csv_path)
    df_Date = df.Date
    df_TempHighF = df.TempHighF
    df_TempAvgF = df.TempAvgF
    df_TempLowF = df.TempLowF

    
    plt.clf()
    plt.figure(figsize=(10,7))
    plt.plot(df_Date, df_TempHighF, label="High Temperature")
    ax = plt.gca()
    ax.xaxis.set_major_locator(dates.MonthLocator(interval=6))
    plt.legend()
    plt.plot(df_Date, df_TempAvgF, label="Average Temperature" )
    ax = plt.gca()
    ax.xaxis.set_major_locator(dates.MonthLocator(interval=6))
    plt.legend()
    plt.plot(df_Date, df_TempLowF, label="Low Temperature" )
    ax = plt.gca()
    ax.xaxis.set_major_locator(dates.MonthLocator(interval=6))
    plt.legend()
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.grid(True)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, "problem2.html", context)



def problem3(request):
    dataframe = pd.read_csv(csv_path)
    dataframe = dataframe[['Date','TempHighF','TempAvgF','TempLowF']]
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    dataframe['TempHighF'] = pd.to_numeric(dataframe['TempHighF'])
    dataframe['TempAvgF'] = pd.to_numeric(dataframe['TempAvgF'])
    dataframe['TempLowF'] = pd.to_numeric(dataframe['TempLowF'])
    print(dataframe)

    monthly_data = dataframe.groupby(dataframe['Date'].dt.to_period('M')).mean()
    # dataframe['Month'] = dataframe['Date'].dt.month
    monthly_avg_max_temp = monthly_data['TempHighF']
    monthly_avg_avg_temp = monthly_data['TempAvgF']
    monthly_avg_low_temp = monthly_data['TempLowF']
    plt.clf()

    
    plt.figure(figsize=(12, 6))    
    plt.title('Temperature Variation')
    plt.plot(monthly_data['Date'], monthly_avg_max_temp, label='High Temperature')
    plt.plot(monthly_data['Date'], monthly_avg_avg_temp, label='Average Temperature')
    plt.plot(monthly_data['Date'], monthly_avg_low_temp, label='Low Temperature')
    plt.xlabel('Month')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend()
    plt.grid(True)
    ax = plt.gca()
    ax.xaxis.set_major_locator(dates.MonthLocator(interval=6))

    buffer = BytesIO()

    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart': f'data:image/png;base64,{image_base64}',
    }
    return render(request, "problem3.html", context)

def problem4(request):
    dataframe = pd.read_csv(csv_path)
    df = dataframe['Events']

    weathers = {}
    weathers['No Events'] = 0
    for i in range(len(df)):
        if df[i] == ' ':
            weathers['No Events'] += 1
        else:
            tmp_lst = df[i].split(" , ")
            for tmp in tmp_lst:
                if tmp != ' ':
                    if tmp not in weathers:
                        weathers[tmp] = 1
                    else:
                        weathers[tmp] += 1
    weather_status = list(weathers.keys())
    weather_count = list(weathers.values())
    plt.bar(weather_status,weather_count)
    plt.grid(True)
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.title('Event Counts')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    
    context = {
        'chart' : f'data:image/png;base64, {image_base64}',
    }
    plt.switch_backend('Agg')

    return render(request, "problem4.html",context)