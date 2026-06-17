'''
Mathplotlib
------------
--This is alibrary in python for data visualization , allowing users to create a variety of plots...
Basic Structure of Mathplotib
-----------------------------
-->Figure
-->Grid
-->Title
-->Legend

Bar Graph:-
import matplotlib.pyplot as plt
Sales = ['A','B','C']
Values = [25,30,45]
plt.bar(Sales,Values,color='red',edgecolor='black')
plt.xlabel('Car Models')
plt.ylabel('Values')
plt.title('KIA')
plt.show()


import matplotlib.pyplot as plt
overs = [1,2,3,4,5]
Score = [4,9,17,20,8]
plt.plot(overs,Score,color = 'yellow')
plt.title('Score Card')
plt.xlabel('Overs')
plt.ylabel('Score')
plt.show()

import matplotlib.pyplot as plt
subjects = ['Python','Java','C']
students =[35,7,15]
plt.pie(students,labels = subjects,autopct='%1.1f%%')
plt.legend(subjects)
plt.title('Students in Courses')
plt.show()

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y =[10,15,18,20,13]
plt.scatter(x,y)
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

import matplotlib.pyplot as plt
y =[10,20,30,40,50]
plt.hist(y)
plt.title ('Histogram Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()


bar graph:-
import matplotlib.pyplot as plt
Year = ['2021','2022','2023','2024','2025','2026']
Sales = [10,57,79,89,98,90]
plt.bar(Year,Sales,color='blue')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Jaguar')
plt.show()


'''

import matplotlib.pyplot as plt
companies = ['AUDI','JAGUAR','WAGONAR']
sales =[35,7,15]
plt.pie(sales, labels = companies,autopct='%1.1f%%')
plt.legend(companies)
plt.title('Sales in companies')
plt.show()
























































































































































































































