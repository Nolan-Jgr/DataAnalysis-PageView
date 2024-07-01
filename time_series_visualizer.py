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
    ax = sns.lineplot(data=df, x ='date',y='value',color='#901cd4')
    ax.set(xlabel='Date', ylabel='Page Views',
           title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().reset_index()
    df_bar.date = pd.to_datetime(df_bar.date)
    monthNames=['January', 'February', 'March', 'April', 'May', 'June', 'July', 
             'August', 'September', 'October', 'November', 'December']
    df_bar['Month'] = pd.Categorical(df_bar.date.dt.strftime('%B'), categories=monthNames, ordered=True)
    df_bar = pd.pivot_table(data=df_bar, index=df_bar.date.dt.year, columns='Month', values='value',aggfunc='mean',observed=False)
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15,10))
    ax = df_bar.plot(ax=ax,kind='bar')
    ax.set(xlabel='Years',ylabel='Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    # df_box['year'] = [d.year for d in df_box.date]
    # df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['Year'] = pd.DatetimeIndex(df['date']).year
    df_box['Month'] = pd.DatetimeIndex(df['date']).month



    # Draw box plots (using Seaborn)
    fig, (f1,f2) = plt.subplots(1,2,figsize=(16,10))

    f1.set_title("Year-wise Box Plot (Trend)")
    f1 = sns.boxplot(ax=f1,x='Year',y='value',data=df_box,hue='Year',palette='Set1',legend=False)
    f1.set_xlabel("Year")
    f1.set_ylabel("Page Views")

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    f2.set_title("Month-wise Box Plot (Seasonality)")
    f2 = sns.boxplot(ax=f2,x='Month',y="value",data=df_box,hue='Month',palette='Set1',legend=False)
    f2.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    f2.set_xticklabels(month_order)
    f2.set_xlabel("Month")
    f2.set_ylabel("Page Views")





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
