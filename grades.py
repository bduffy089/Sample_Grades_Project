# Sample Grades Project
# by Britney Duffy

# import stat functions
import statistics as stat

def output_stats(list):
    print("Mean:                 ", round(stat.mean(list),2))
    print("Median:               ", round(stat.median(list), 2))
    print("Standard Deviation:   ", round(stat.stdev(list), 2))
    print()

def final_output():
    print("Spring 2016")
    output_stats(spring_grades)

    print("Fall 2016")
    output_stats(fall_grades)

# data variables
fall_grades = []
spring_grades = []

# Read in the CSV file
file = open("sample_grades.csv")

for line in file:
    # print(line.rstrip())
    list = line.rstrip().split(",")
    # print(list)
    if list[1] == 'Spring 2016':
        spring_grades.append(eval(list[2]))
    else:
        fall_grades.append(eval(list[2]))

file.close()

final_output()
