import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("kindly specify a city by typing 'ch' for chicago or 'ny' for new york or 'w' for washington: \n\n ").lower()
        # Vaildate user input for city
        if city in CITY_DATA.keys():
            break
        else:
            print("That's invalid input...")

    # TO DO: get user input for month (all, january, february, ... , june)
    # get user input for month (all, january, february, ... , june
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
    while True:
        month = input('\n\nTo filter data by a particular month, please type the month or all for not filtering by month: (Jan, Feb, Mar, Apr, May, Jun) \n\n:').lower()
        # Validate user input for month
        if month in months:
            break
        else:
            print("That's invalid choice, please type a valid month name or all.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sat', 'sun', 'mon', 'tues', 'wed', 'thru', 'fri', 'all']
    while True:
        day = input("\n\n To filter data by a particular day, kindly type the abbreviated day name such as (Sat, Sun, Mon, Tues, Wed, Thru, Fri) or all for not filtering by day: \n\n").lower()
        if day in days:
            break
        else:
            print('That\'s invalid choice, please type a valid day name or all')


    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    # read data file into a dataframe and parse the Start Time column as datetime object
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'].str.startswith(month.title())]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.startswith(day.title())]


    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    if month == 'all':
        # find the most popular month
        popular_month = df['month'].mode()[0]
        print('Most Popular Start Month:', popular_month)
    else:
        print("You have already specified {} as your month of choice".format(month))

    # display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].mode()[0]
        print('Most Popular Start day:', popular_day)
    else:
        print("You have already specified {} as your day of choice".format(day))

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].value_counts().index.tolist()[0]
    print('\nMost commonly used end station: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_route = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count').sort_values('count',ascending=False).head(1).reset_index()[['Start Station', 'End Station', 'count']]
    print('\nMost frequent combination of start station and end station trip:\n ',most_frequent_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def seconds_format(time_in_seconds):
    """
    Converts total time in seconds to its
    corresponding 'day:hour:minute:second' format
    """
    day = time_in_seconds // (24 * 3600)
    time_in_seconds = time_in_seconds % (24 * 3600)
    hour = time_in_seconds // 3600
    time_in_seconds %= 3600
    minutes = time_in_seconds // 60
    time_in_seconds %= 60
    seconds = time_in_seconds

    return day,hour,minutes,seconds

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    seconds_total = df['Trip Duration'].sum()
    total_time = seconds_format(int(seconds_total))
    #Display the result
    print('Total travel time (d:h:m:s): ', "{:d}:{:2d}:{:2d}:{:2d}".format(*total_time))

    # display mean travel time
    seconds_mean = df['Trip Duration'].mean()
    avg_time = seconds_format(int(seconds_mean))
    print('Average travel time (d:h:m:s): ', "{:d}:{:0>2d}:{:0>2d}:{:0>2d}".format(*avg_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts().to_string()
    print('\nUser types:\n',user_count  )

    try:
        # Display counts of gender
        gender_count = df['Gender'].value_counts().to_string()
        print('\nBike riders gender split: \n', gender_count)

        # Display earliest, most recent, and most common year of birth
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        print('\n Earliest birth year :  ',int(earliest_yob))
        print('\n Most recent birth year :  ',int(most_recent_yob))
        print('\n Most common birth year :  ',int(most_common_yob))

    except KeyError:
        print('\n\nSorry, there\'s no gender or birth year data for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    """
        The fuction takes the name of the city produced by
        the get_filters fuction as input and returns the raw data of that city
        as chunks of 5 rows based upon user input.
    """
    df = pd.read_csv(CITY_DATA[city])
    print('\nRaw data is available to check... \n')
    start_loc = 0
    while True:
        display_opt = input('To View the availbale raw data in chuncks of 5 rows type: Yes \n').lower()
        if display_opt not in ['yes', 'no']:
            print('That\'s invalid choice, pleas type yes or no')

        elif display_opt == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5

        elif display_opt == 'no':
            print('\nExiting...')
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
