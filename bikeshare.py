import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


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
    city = input("Type the city that you want to check the statistics from: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("We do not have such information. Please try with Chicago, Washington or New York City:").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("type the month you want to search from the selected city and check the general information (january to june): ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        month = input("We do not have such information. Please type a month from january to june:").lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Type any day of the week to watch the general information from the selected city (monday, tuesday, wednesday, thursday, friday, saturday or sunday): ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("We do not have such information, please type a day of the week: ").lower()
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv("{}.csv".format(city))

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month,:]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day,:]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month for using bikes in this city is: {}".format(str(df['month'].mode().values[0])))

    # TO DO display the most common day of week
    print("The most common day of the week for using bikes in this city is: {}".format(str(df['day_of_week'].mode().values[0])))

    # TO DO display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour for using bikes in this city is: {}".format(str(df['start_hour'].mode().values[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station in the selected city is: {}.".format(df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print("The most popular end station is: {}.".format(df['End Station'].mode().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = " from " + df['Start Station'] + " to " + df['End Station']
    print("The most popular trip is: {}.".format(df['routes'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    print("The total travel time in the selected city is: {}".format(str(df['duration'].sum())))

    # TO DO: display mean travel time
    print("The mean of the travel time in the selected city is: {}".format(str(df['duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Here is the information about the Here are the types of user, except for the city of Washington:")
    print(df['User Type'].value_counts())

    if city != 'washington':
    # TO DO: Display counts of gender
        print("Here are the counts of gender:")
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birth year is: {}".format(str(int(df['Birth Year'].min()))))
        print("The latest birth year is: {}".format(str(int(df['Birth Year'].max()))))
        print("The most common birth year is: {}".format(str(int(df['Birth Year'].mode().values[0]))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    s_loc = 0
    e_loc = 5

    rawdat = input("Would you like to see the raw data? yes/no: ").lower()

    if rawdat == 'yes':
        while e_loc <= df.shape[0] - 1:

            print(df.iloc[s_loc:e_loc,:])
            s_loc += 5
            e_loc += 5

            more_raw = input("Would you like to continue?: ").lower()
            if more_raw == 'no':
                break
    
def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thank you for visiting us!")
            break


if __name__ == "__main__":
	main()