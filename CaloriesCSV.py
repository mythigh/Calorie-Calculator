import csv
import datetime
# r is to read the file
# cal_csv is the name of the var storing the csv
from mealcsv import Meal
from workoutcsv import Workout

# meal class with the sum calories for each day
m_cal = Meal()
meals = m_cal.mealcal()

# workout class with the sum calories for each day
w_cal = Workout()
workouts = w_cal.workcal()

# new csv file to write the overal calories on each day
file = open('week.csv','w')
# separating each element with a comma
write = csv.writer(file, delimiter = ',')

# fields for the new csv file
write.writerow(['Date','Daliy Calorie Intake','Daily Calorie Outtake','Total'])

# calander to store all the days
calender = []
food = open('meals.csv','r')
reader = csv.reader(food)
header = next(reader)

# appending days into calender
for line in reader:
    calender.append(line[0])

# setting the day as an offical date
day = calender[0].split('/')
date = datetime.date(int(day[2]),int(day[1]),int(day[0]))

# for loop to write into new csv file
for i in range(0,len(workouts)):
    total = meals[i] - workouts[i]
    # dt increments each day by 1
    dt = datetime.timedelta(1)
    date += dt
    # update minuses a date so we add the first date
    update = date - dt
    formatted_date = update.strftime('%d/%m/%Y')
    write.writerow([formatted_date,meals[i], workouts[i],total])
