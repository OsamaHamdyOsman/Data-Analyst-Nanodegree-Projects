from flask import Flask, redirect, url_for, render_template, flash, request
from forms import Inputs, RawData
import numpy as np
import pandas as pd


app = Flask(__name__)


app.config['SECRET_KEY'] = 'efb289fc026885ba1e7f36d3ef61dd7b5d3fd92af69495b025fe794f6794322d'

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


@app.route('/', methods=("POST", "GET"))
@app.route('/home', methods=("POST", "GET"))
def home():
    form = Inputs()
    if request.method == 'POST' and form.submit():
        flash(f'You have selected {form.city.data} and specified month to be {form.month.data} and day to be {form.day.data}!', 'success')
        city = form.city.data
        month = form.month.data
        day = form.day.data
        print(city, month, day)
        return redirect(url_for('load_data',city=city, month=month, day=day))

    return render_template('home.html', title='get_filters', form=form)

def seconds_format(time_in_seconds):
    day = time_in_seconds // (24 * 3600)
    time_in_seconds = time_in_seconds % (24 * 3600)
    hour = time_in_seconds // 3600
    time_in_seconds %= 3600
    minutes = time_in_seconds // 60
    time_in_seconds %= 60
    seconds = time_in_seconds

    return day,hour,minutes,seconds

@app.route('/Loading_data/<string:city>/<string:month>/<string:day>', methods=("POST", "GET"))
def load_data(city, month, day):
    # read data file into a dataframe
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'], index_col= 'Unnamed: 0')
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'All':
        # filter by month to create the new dataframe
        df = df[df['month'].str.startswith(month.title())]
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.startswith(day.title())]

    popular_month = df['month'].mode()[0]
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    popular_hour = df['hour'].mode()[0]
    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    # display most commonly used start station
    popular_end_station = df['End Station'].mode()[0]
    # popular common route
    df['route'] = df['Start Station'] + " - " + df['End Station']
    popular_route= df['route'].mode()[0]

    # display total travel time
    seconds_total = df['Trip Duration'].sum()
    # converting seconds_total to day: hour: minutes: seconds format
    total_duration = seconds_format(seconds_total)

    # display mean travel time
    seconds_mean = df['Trip Duration'].mean()
    # converting seconds_mean to day: hour: minutes: seconds format
    mean_duration = seconds_format(seconds_mean)

    # Display counts of user types
    user_count = df['User Type'].value_counts().to_frame().reset_index().rename(columns={'index':'Rider Type', "User Type": "Count"})
    user_count_hds = user_count.columns.values
    user_count_rows = tuple(zip(*list(zip(*user_count.values))))

    # Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts().to_frame().reset_index().rename(columns={'index':'Gender', "Gender": "Count"})
        gender_count_hds = gender_count.columns.values
        gender_count_rows = tuple(zip(*list(zip(*gender_count.values))))
    else:
        gender_count, gender_count_hds, gender_count_rows =None, None, None

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
    else:
        earliest_yob, most_recent_yob, most_common_yob = None, None, None

    #test = df.head().to_html()
    #html=test
    return render_template('city_data.html', city=city,
     pop_month=popular_month, pop_day=popular_day,
     pop_hour=popular_hour, pop_st_st=popular_start_station,
     pop_e_st=popular_end_station, pop_route = popular_route,
     tot_dur=total_duration, avg_dur=mean_duration,
     u_ct_h=user_count_hds, u_ct_r=user_count_rows,
     g_ct=gender_count, g_ct_h=gender_count_hds, g_ct_r=gender_count_rows,
     earliest_yob=earliest_yob, most_recent_yob=most_recent_yob,
     most_common_yob=most_common_yob)

@app.route('/raw_data/<string:city>/<int:start_loc>', methods=("POST", "GET"))
def display_raw_data(city, start_loc):

    #print('\nRaw data is available to check... \n')
    if request.method == 'POST':
        df= pd.read_csv(CITY_DATA[city]).rename(columns={'Unnamed: 0': 'Trip_id'})
        if request.form.get('submit_a'):
            chunk = df.iloc[start_loc:start_loc+5]
            chunk_hds = chunk.columns.values
            chunk_rows = tuple(zip(*list(zip(*chunk.values))))
            start_loc+=5
            return render_template('raw_data.html', city=city,
            start_loc=start_loc, chunk_hds=chunk_hds, chunk_rows=chunk_rows)

    return render_template('raw_data.html',city=city,
    start_loc=start_loc)


if __name__ == '__main__':
   app.run(debug = True)
