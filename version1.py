import math
import stats
import pylab as plt



#simple framework to build project around
student_grades = {'Name': [], 'Grade': []}
number_of_students = int(input(" Enter Number of Students:"))


#csv manipulation
fp = open("studentgrades.csv","w")
fp.write("Name,Grade\n")

for i in range(number_of_students):
    name = input("Enter Student Name:")
    grade = float(input(f"Enter {name}'s Grade:"))
    student_grades['Name'].append(name)
    student_grades['Grade'].append(grade)
    fp.write(f"{name},{grade}\n")
    
print( student_grades)
# fp.write(f"{student_grades['Name']},{student_grades['Grade']}\n")
fp.close()



grades = student_grades['Grade']
#computing statistics of data by importing statspy
print(f'the sum of the grades is {stats.sum(grades)}')
print(f'The mean of the grades is {stats.mean(grades):.2f}')
print(f'the variance of the grades is {stats.variance(grades):.2f}')
print(f'the minimum of the grades is {stats.min(grades)}')
print(f'the maximum of the grades is {stats.max(grades)}')
print(f' the standard deviation of the grades is {stats.standard_dev(grades)}')   
print(f' the median of the grades is {stats.median(grades)}')   

plt.title( 'Student Grades')
plt.xlabel( 'Name' )
plt.ylabel( 'Grade' )
plt.bar(student_grades['Name'], student_grades['Grade'], color='b')
# plt.plot( student_grades.keys() ,student_grades.values() , color='b' , marker='x' )
# plt.scatter( student_grades.keys() ,student_grades.values() , color='b' , marker='x' )

#show the plot
plt.show()


