#calc the trendline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv = pd.read_csv('ALT 2 project.csv')

#select your data columns
data = csv[['GDP Growth in 2014', '%GDP spent on education']]

#Lets you say which will be x and y
x = data['%GDP spent on education']
y = data['GDP Growth in 2014']

#choose your graph type
plt.scatter(x, y)

#some maths
z = np.polyfit(x, y, 1) 
f = np.poly1d(z)
plt.plot(x,f(x),"r--")

#z returns two values in a list eg. [-3.91792431e-05  1.56428161e+01]
#The first value z[0] is the slope and the second x[1] is the y intercept
print("z will give you ", z)


print("The slope is", z[0])
print("The intercept is", z[1])

#here we can round off things to 2 digits so that the equation isn't too ugly and long
#This is the equation of a line    y=        m             x    +    c
print("The equation of the line is y="+str(round(z[0],2))+"x+"+str(round(z[1],2)))

#shows your graph in a new window
plt.show()



#The .csv file used in this example looks like this:

# Pirates   Temp      Year
# 45000   14.06   1820
# 35000   14.25   1860
# 20000   14.61   1880
# 15000   14.91   1920
# 5000    15.41   1940
# 3000    15.52   1980
# 17      15.92   2000