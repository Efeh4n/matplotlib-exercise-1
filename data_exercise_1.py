#                       a exercise about car data set 
#   ---question 1--- 
#Import the automobiles data contained in auto-mpg.csv file as a pandas dataframe.
#Look at the first few rows of data.
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\efeha\OneDrive\Masaüstü\auto-mpg.csv")
auto_mpg_data_df = pd.DataFrame(data)
print(auto_mpg_data_df.head())


#   ---question 2--- 
#Which column should be considered as index column?
#Determine and import the data again with the index_col option.
data_2 = pd.read_csv(r"C:\Users\efeha\OneDrive\Masaüstü\auto-mpg.csv", index_col= 8)
auto_mpg_data_df_2 = pd.DataFrame(data)

#   ---question 3--- 
#Generate a scatter plot with hp on the x-axis and mpg on the y-axis.
#Add a title to the plot.
#Specify the x-axis and y-axis labels.

hp = auto_mpg_data_df_2['hp']
mpg = auto_mpg_data_df_2['mpg']
auto_mpg_data_df_2.plot(kind='scatter',x= 'hp',y='mpg')
plt.title('Fuel efficiency vs Horse-power')
plt.xlabel('hp')
plt.ylabel('mpg')
plt.show()

#   ---question 4--- 
#Now add the argument c = "cyl" on your plot.
#What happened to the plot.
#Make a comment.
auto_mpg_data_df_2.plot(kind='scatter',x= 'hp',y='mpg',c = 'cyl')
plt.show()

#   ---question 5--- 
#Now we are going to create boxplots.
#Create two seperate boxplots one for weight and one for mpg.
weight = auto_mpg_data_df_2['weight']
mpg = auto_mpg_data_df_2['mpg']
box_plots_1 = weight.plot(kind='box')
plt.show()
box_plots_2 = mpg.plot(kind='box')
plt.show()
         
 #   ---question 6---
#Next draw boxplot with two columns together.
#Make a list called cols of the column names to be plotted: weight and mpg.
#Call plot on df[cols] to generate a box plot of the two columns in a single figure.
#To do this, specify the additional argument subplots = True.
cols =["weight", "mpg"]
auto_mpg_data_df_2[cols].plot(kind ="box", subplots = True)
plt.show()

#   ---question 7---
#Describe the automobile data and find summary statistics.
#Find the median of the mpg column.
#Find the standard deviation of cyl.
#Find the maximum value of acceleration.
#Find the minimum value of mpg.
print(auto_mpg_data_df_2.describe())
print(auto_mpg_data_df_2["mpg"].median())
print(auto_mpg_data_df_2["cyl"].std())
print(auto_mpg_data_df_2["accel"].max())
print(auto_mpg_data_df_2["mpg"].min())


#   ---question 8---
#Create a new dataframe from the US cars.
#Create a new dataframe form the Asia cars.
#Compare the minimum, maximum, mean and median of US and Asia cars.
#Draw boxplots for both Asia and US cars.
us_cars_only = auto_mpg_data_df_2['origin']=='US'
us_cars = auto_mpg_data_df_2[us_cars_only]
print(us_cars.head())
asia_cars_only = auto_mpg_data_df_2['origin']=='Asia'
asia_cars = auto_mpg_data_df_2[asia_cars_only]

print(us_cars.describe())
print(asia_cars.describe())

us_cars.plot(kind="box")
plt.show()

asia_cars.plot(kind="box")
plt.show()





