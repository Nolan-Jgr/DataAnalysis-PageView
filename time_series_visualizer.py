import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025))&
            (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16,6))
    ax = sns.lineplot(data=df, x ='date',y='value')
    ax.set(xlabel='Date', ylabel='Page Views',
           title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.reset_index()
    df_bar = df_bar.rename(columns={'value':'avg'})
    df_bar['Year'] = pd.DatetimeIndex(df['date']).year
    df_bar['Month'] = pd.DatetimeIndex(df['date']).month
    print(df_bar)
    df_bar = df_bar.groupby(['Year', 'Month'], as_index=False,sort=False)['avg'].mean()
    print(df_bar)

    
    monthNames=['January', 'February', 'March', 'April', 'May', 'June', 'July', 
             'August', 'September', 'October', 'November', 'December']
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15,10))
    ax = sns.barplot(data=df_bar,x='Year',y='avg',hue = 'Month',palette='tab10')
    ax.set(xlabel='Years',ylabel='Average Page Views')
    ax.legend(title='Months',labels=monthNames)

    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
