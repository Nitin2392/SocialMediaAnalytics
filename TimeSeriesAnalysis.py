import sys
import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import pickle

if __name__ == '__main__':
    fname = "Twitter_data_userlevel.jsonl"
    with open(fname,"r") as fi:
        all_dates = []
        for line in fi:
            tweet = json.loads(line)
            all_dates.append(tweet.get('created_at'))
        idx = pd.DatetimeIndex(all_dates)
        ones = np.ones(len(all_dates))

        # Below is the actual series
        my_series = pd.Series(ones, index=idx)

        # Resampling into 1 minute buckets
        per_minute = my_series.resample('1Min').sum().fillna(0)

        # Plotting
        fig, ax = plt.subplots()
        ax.grid = True
        ax.set_title("Tweet Frequencies")
        hours = mdates.MinuteLocator(interval=20)
        date_formatter = mdates.DateFormatter("%H:%M")

        datemin = datetime(2018, 4, 24, 14, 30)
        datemax = datetime(2018, 4, 24, 18, 30)

        ax.xaxis.set_major_locator(hours)
        ax.xaxis.set_major_formatter(date_formatter)
        ax.set_xlim(datemin, datemax)
        max_freq = per_minute.max()
        ax.set_ylim(0, max_freq)
        ax.plot(per_minute.index, per_minute)
        plt.savefig("Twitter_Time_series.png")





