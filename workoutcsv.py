import csv
# r is to read the file
# cal_csv is the name of the var storing the csv
class Workout:
    def workcal (self):
        workout = open('Workouts.csv','r')
        reader = csv.reader(workout)
        header = next(reader)

        day1 = []
        day2 = []
        day3 = []
        day4 = []
        day5 = []
        day6 = []
        day7 = []
        for line in reader:
            if line[0] == "10/04/2020":
                day1.append(int(line[2])*int(line[3]))
            elif line[0] == "11/04/2020":
                day2.append(int(line[2])*int(line[3]))
            elif line[0] == "12/04/2020":
                day3.append(int(line[2])*int(line[3]))
            elif line[0] == "13/04/2020":
                day4.append(int(line[2])*int(line[3]))
            elif line[0] == "14/04/2020":
                day5.append(int(line[2])*int(line[3]))
            elif line[0] == "15/04/2020":
                day6.append(int(line[2])*int(line[3]))
            elif line[0] == "16/04/2020":
                day7.append(int(line[2])*int(line[3]))

        days = []
        days.append(sum(day1))
        days.append(sum(day2))
        days.append(sum(day3))
        days.append(sum(day4))
        days.append(sum(day5))
        days.append(sum(day6))
        days.append(sum(day7))
        return days
