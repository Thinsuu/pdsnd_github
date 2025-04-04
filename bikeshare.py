import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_input(value_name, allowed_values):
    while True:
        value = input(f"Enter a {value_name} ({allowed_values}): ").lower()
        if value in allowed_values:
            break
        else:
            print(f"Invalid {value_name}. Please try again")
    return value


def get_filters():
    city_names = list(CITY_DATA.keys())
    city = get_input('city name', city_names)
    month = get_input('month', ['all', 'january', 'february', 'march', 'april', 'may', 'june'])
    day = get_input('day of the week', ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])

    print('Hello! Let\'s explore some US bikeshare data!')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["hour"] = df["Start Time"].dt.hour
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
       
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month.lower()) + 1
        df = df[df["month"] == month]
    
    if day != "all":
        df = df[df["day_of_week"].str.lower() == day.lower()]
     
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    popular_month = df["month"].mode()[0]
    popular_day_of_week = df["day_of_week"].mode()[0]
    popular_hour = df["hour"].mode()[0]
    
    print("Most popular month:", popular_month)
    print("Most popular day of week:", popular_day_of_week)
    print("Most popular start hour:", popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_start_station = df["Start Station"].mode()[0]
    popular_end_station = df["End Station"].mode()[0]
    total_trip = df["Start Station"] + " -> " + df["End Station"]
    frequent_combo_start_end = total_trip.mode()[0]
    print("The popular start station: ", popular_start_station)
    print("The most popular end station: ", popular_end_station)
    print("The most frequent start and end station: ", frequent_combo_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_time = df["Trip Duration"].sum()
    total_mean_time = df["Trip Duration"].mean()
    print("Total trip duration in seconds is:", total_time)
    print("Total average time in seconds is:", total_mean_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types_count = df["User Type"].value_counts()
    print("User Type Count is: \n", user_types_count)
    
    if "Gender" in df.columns:
        gender_count = df["Gender"].value_counts()
        print("Gender counts:\n", gender_count)
    else:
        print("Gender data is not available for this city.")
        
        
    if "Birth Year" in df.columns:
        earliest_birth = df["Birth Year"].min()
        recent_birth = df["Birth Year"].max()
        popular_birth = df["Birth Year"].mode()[0]
        print("Earliest of the birth year: ", earliest_birth)
        print("Most recent birth: ", recent_birth)
        print("Most common birth year: ", popular_birth)
    else:
        print("Birth year data is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Continuous promt the user and display 5 lines at a time until the user says 'no' or the data is run out"""
    row_index = 0
    while True:
        display_line_data = input("\nWould you like to see 5 lines of raw data? Enter yes or no\n").lower()
        if display_line_data == 'yes':
            print(df.iloc[row_index : row_index + 5])
            row_index += 5
            if row_index >= len(df):
                print("There is no data left to show")
                break
        else:
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
