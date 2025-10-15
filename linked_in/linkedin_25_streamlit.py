import time
import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore
from sklearn.datasets import load_iris # type: ignore

'''Making  a Simple Streamlit App'''

st.title("My First Streamlit App") # display title

''' creating some basic data and 2 demo charts'''

col_names = ["Column1", "Column2", "Column3"] # create column names
data = pd.DataFrame(np.random.randint(30, size = (30, 3)), columns=col_names) # create a dataframe

st.write("Line Chart") # display text
st.line_chart(data) # display line chart

st.write("Bar Chart") # display text
st.bar_chart(data) # display bar chart

'''Creating a Pie Chart (not natively supported in Streamlit)'''

animals = ["Cats", "Dogs", "Rabbits", "Frogs"] # create animal names
counts = [23, 17, 35, 29] # create counts

st.write("Pie Chart") # display text
fig, ax = plt.subplots() # create a subplot
ax.pie(counts, labels=animals) # create a pie chart
st.pyplot(fig) # display the pie chart

'''Creating a Growing Line Chart'''

rows = np.random.randn(1, 1) # create random data
st.write("Growing Line Chart") # display text
chart = st.line_chart(rows) # display line chart

for i in range(1, 100): # loop to update the chart
    new_rows = rows[0] + np.random.randn(1, 1) # create new random data
    chart.add_rows(new_rows) # add new data to the chart
    rows = new_rows # update the rows
    time.sleep(0.1) # wait for 0.1 seconds

'''Creating a Matplotlib Line Chart'''

values = np.random.rand(10) # create random values
st.write("Matplotlib Line Chart") # display text
fig, ax = plt.subplots() # create a subplot
ax.plot(values) # plot the values
st.pyplot(fig) # display the plot

''' Creating a Matplotlib Bar Chart'''

animals = ["Cats", "Dogs", "Rabbits", "Frogs"] # create animal names
heights = [23, 35, 15, 7] # create heights 
weights = [5, 7, 3, 1] # create weights
fig, ax = plt.subplots() # create a subplot
x = np.arange(len(animals))  # x axis columns set to number of animals in list
width = 0.35  # the width of the bars
ax.bar(x - width/2, heights, width, label='Heights', color='blue') # create bar for heights
ax.bar(x + width/2, weights, width, label='Weights', color='orange') # create bar
ax.legend(["Heights", "Weights"]) # add legend
ax.set_xticks(x) # set x ticks
ax.set_xticklabels(animals) # set x tick labels
st.pyplot(fig) # display the plot

'''Creating a Seaborn Histogram from the Iris Dataset'''

iris_data = load_iris() # load iris data
data = pd.DataFrame(data = iris_data.data, columns = iris_data.feature_names) # create dataframe
fig = plt.figure() # create a figure
sns.histplot(data = data, bins = 20) # create a histogram
st.pyplot(fig) # display the plot

'''Creating a Seaborn box Plot from the Iris Dataset'''

fig = plt.figure() # create a figure
sns.boxplot(data = data) # create a box plot
st.pyplot(fig) # display the plot

'''Creating a Seaborn Scatter Plot from the Iris Dataset'''

fig = plt.figure() # create a figure
sns.scatterplot(data = data) # create a scatter plot
st.pyplot(fig) # display the plot
