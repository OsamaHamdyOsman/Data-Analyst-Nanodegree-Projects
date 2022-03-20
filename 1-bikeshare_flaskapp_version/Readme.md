# Overview
This is a special version of a project that is part of the Data Analyst Nanodegree program of Udacity.

> In this project, making use of Python and Flask to create an app that explores data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. Writing code to import the data and answer interesting questions about it by computing descriptive statistics. I will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

![image](https://user-images.githubusercontent.com/49010338/159188263-232eb65d-2937-4bca-93b2-b365728d18b9.png)


## What Software Do I Need?
To complete this project, the following software requirements apply:

* You should have Python 3, Flask, NumPy, and pandas installed using Anaconda
* A text editor, like Sublime or Atom.
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).


# Project Details

## Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.


## Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:

Gender
Birth Year


## Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

###  Popular times of travel (i.e., occurs most often in the start time)

* most common month
* most common day of week
* most common hour of day

### Popular stations and trip

* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

### Trip duration

* total travel time
* average travel time

### User info

* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)


# An Interactive Experience

The bikeshare_app.py file is set up as a ***web application*** that takes in inputs to create an interactive experience that answers questions about the dataset. The experience is interactive because depending on a user's inputs about city, month and day to analyze the data accordingly and display informative statistics. 

# Implementation steps:

1. You need to have python and the required packages installed.
2. Open a terminal and run the `bikeshare_app.py` file by typing this command: 'python bikeshare_app.py`

![image](https://user-images.githubusercontent.com/49010338/159187980-12b4af59-0c80-4123-b75e-9ff2e0dd1fc8.png)

3. Then open the local host on any web browser like googl Chrome and start by selecting a city, month and day:

![image](https://user-images.githubusercontent.com/49010338/159188072-bec90d79-d53a-4573-9366-b609bbb53832.png)

4. Finally, you can check raw data or go back to the home bage by clicking on the links at the page bottom:

![image](https://user-images.githubusercontent.com/49010338/159188111-3b908b54-3e78-4d0e-8570-0296a6614b75.png)



# The data comprises three csv files:
    1. [Washington data](./washington.csv) 
    2. [Chicago data](./chicago.csv)
    3. [NYC data](./new_york_city.csv)
    


## Resources:
* https://newbedev.com/how-to-add-next-button-in-flask-code-example
* https://stackoverflow.com/questions/12681036/is-there-a-direct-approach-to-format-numbers-in-jinja2/12681178
* https://stackoverflow.com/questions/49741978/flask-and-pandas
* https://stackoverflow.com/questions/52644035/how-to-show-a-pandas-dataframe-into-a-existing-flask-html-table
* https://www.youtube.com/watch?v=mCy52I4exTU
