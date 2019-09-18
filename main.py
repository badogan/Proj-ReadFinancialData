'''Started in github.
And now continuing from my local
'''

# Import DataReader, Import date, Import matplotlib
from  pandas_datareader.data import DataReader
from datetime import date 
import matplotlib.pyplot as plt

# Set the start date
start = date(1950,1,1)

# Define the series codes
series = ['UNRATE', 'CIVPART']

# Import the data
econ_data = DataReader(series, 'fred', start=start)

# Assign new column labels
econ_data.columns = ['Unemployment Rate','Participation Rate']

# Plot econ_data
econ_data.plot(subplots=True, title='Labor Market')

# Show the plot
plt.show()


