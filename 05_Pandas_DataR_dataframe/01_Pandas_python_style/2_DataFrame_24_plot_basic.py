'''
Draw basic plots using DataFrame.plot() method or DataFrame.plot.<plotting_method>().

##########################

1. Histogram: 
   + df.plot(kind = "hist") 
   + df.plot.hist()

2. Density/KDE plot: 
   + df.plot(kind = "density"/"kde")
   + df.plot.density()
   + df.plot.kde()

3. Box plot: 
   + df.plot(kind = "box")
   + df.plot.box()

4. Pie chart: 
   + df.plot(kind = "pie")
   + df.plot.pie()

5. Bar plot: 
   + df.plot(kind = "bar")
   + df.plot.bar()

6. Barh plot (horizontal): 
   + df.plot(kind = "barh")
   + df.plot.barh()

7. Scatter plot: 
   + df.plot(kind = "scatter", x = <x_column>, y = <y_column>), 
   + df.plot.scatter(x = <x_column>, y = <y_column>)

8. Line plot: 
   + df.plot(kinde = "line")
   + df.plot()
   + df.plot.line()

9. Area plot: 
   + df.plot(kind = "area")
   + df.plot.area()

10. Hexbin plot: 
    + df.plot(kind = "hexbin", x = <x_column>, y = <y_column>, gridsize = <size>)
    + df.plot.hexbin(x = <x_column>, y = <y_column>, gridsize = <size>)
'''

import pandas as pd
import matplotlib.pyplot as plt

df_pokemon = (
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/pokemon.csv",
        dtype = {
            "Type 1": "category",
            "Type 2": "category",
            "Generation": "category",
            "Legendary": "bool"
        }
    )
    .drop(columns = ["#"])
    .pipe(lambda df: df.set_axis(df.columns.str.strip().str.replace(r"\s+", "_", regex = True).str.replace(".", ""), axis=1))
    .assign(Generation = lambda df: df['Generation'].cat.as_ordered())
)

print(df_pokemon.info())
# RangeIndex: 800 entries, 0 to 799
# Data columns (total 12 columns):
#  #   Column      Non-Null Count  Dtype   
# ---  ------      --------------  -----   
#  0   Name        800 non-null    object  
#  1   Type_1      800 non-null    category
#  2   Type_2      414 non-null    category
#  3   Total       800 non-null    int64   
#  4   HP          800 non-null    int64   
#  5   Attack      800 non-null    int64   
#  6   Defense     800 non-null    int64   
#  7   Sp_Atk      800 non-null    int64   
#  8   Sp_Def      800 non-null    int64   
#  9   Speed       800 non-null    int64   
#  10  Generation  800 non-null    category
#  11  Legendary   800 non-null    bool    
# dtypes: bool(1), category(3), int64(7), object(1)
# memory usage: 54.7+ KB


#--------------------------------------------------------------------------------------------------------#
#------------------------------------------ 1. Histogram ------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
'''
Histogram describes the distribution of a numerical variable by splitting the data into bins (intervals) 
and counting the number of observations that fall into each bin.
'''

##################################
##    df.plot(kind = "hist")    ##
##################################

#----------
## Draw histogram of "Attack" column
#----------

df_pokemon.plot(
    kind = "hist",
    y = "Attack",
    bins = 30,                     # Number of bins (intervals)
    color = "skyblue",             # Color of the bars
    edgecolor = "black",           # Color of the bar edges
    alpha = 0.7,                   # Transparency level (0 to 1)
    title = "Histogram of Pokemon Attack",  # Title of the plot
    xlabel = "Attack",             # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

#----------
## Draw histogram of "Attack" and "Defense" columns
#----------

df_pokemon.plot(
    kind = "hist",
    y = ["Attack", "Defense"],
    bins = 30,                     # Number of bins (intervals)
    color = ["skyblue", "salmon"], # Colors for each column
    edgecolor = "black",           # Color of the bar edges
    alpha = 0.7,                   # Transparency level (0 to 1)
    title = "Histogram of Pokemon Attack and Defense",  # Title of the plot
    xlabel = "Value",              # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

##########################
##    df.plot.hist()    ##
##########################

#----------
## Draw histogram of "Attack" column
#----------

df_pokemon.plot.hist(
    y = "Attack",
    bins = 30,                     # Number of bins (intervals)
    color = "skyblue",             # Color of the bars
    edgecolor = "black",           # Color of the bar edges
    alpha = 0.7,                   # Transparency level (0 to 1)
    title = "Histogram of Pokemon Attack",  # Title of the plot
    xlabel = "Attack",             # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

#----------
## Draw histogram of "Attack" and "Defense" columns
#----------

df_pokemon.plot.hist(
    y = ["Attack", "Defense"],
    bins = 30,                     # Number of bins (intervals)
    color = ["skyblue", "salmon"], # Colors for each column
    edgecolor = "black",           # Color of the bar edges
    alpha = 0.7,                   # Transparency level (0 to 1)
    title = "Histogram of Pokemon Attack and Defense",  # Title of the plot
    xlabel = "Value",              # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot


#--------------------------------------------------------------------------------------------------------#
#------------------------------------------ 2. Density/KDE plot -----------------------------------------#
#--------------------------------------------------------------------------------------------------------#
'''
Density plot (or Kernel Density Estimate - KDE) is a smoothed version of the histogram that estimates
the probability density function of a continuous variable.
'''

#####################################
##    df.plot(kind = "density")    ##
#####################################

#----------
## Draw density plot of "Attack" column
#----------

# kind = "density"
df_pokemon.plot(
    kind = "density",
    y = "Attack",
    color = "blue",             # Color of the density line
    title = "Density Plot of Pokemon Attack",  # Title of the plot
    xlabel = "Attack",             # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

# kind = "kde"
df_pokemon.plot(
    kind = "kde",
    y = "Attack",
    color = "blue",             # Color of the density line
    title = "Density Plot of Pokemon Attack",  # Title of the plot
    xlabel = "Attack",             # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

#----------
## Draw density plot of "Attack" and "Defense" columns
#----------

# kind = "density"
df_pokemon.plot(
    kind = "density",
    y = ["Attack", "Defense"],
    color = ["blue", "red"], # Colors for each column
    title = "Density Plot of Pokemon Attack and Defense",  # Title of the plot
    xlabel = "Value",              # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

# kind = "kde"
df_pokemon.plot(
    kind = "kde",
    y = ["Attack", "Defense"],
    color = ["blue", "red"], # Colors for each column
    title = "Density Plot of Pokemon Attack and Defense",  # Title of the plot
    xlabel = "Value",              # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

#############################
##    df.plot.density()    ##
#############################

#----------
## Draw density plot of "Attack" column
#----------

df_pokemon.plot.density(
    y = "Attack",
    color = "blue",             # Color of the density line
    title = "Density Plot of Pokemon Attack",  # Title of the plot
    xlabel = "Attack",             # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

#----------
## Draw density plot of "Attack" and "Defense" columns
#----------

df_pokemon.plot.density(
    y = ["Attack", "Defense"],
    color = ["blue", "red"], # Colors for each column
    title = "Density Plot of Pokemon Attack and Defense",  # Title of the plot
    xlabel = "Value",              # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

#########################
##    df.plot.kde()    ##
#########################

#----------
## Draw density plot of "Attack" column
#----------

df_pokemon.plot.kde(
    y = "Attack",
    color = "blue",             # Color of the density line
    title = "Density Plot of Pokemon Attack",  # Title of the plot
    xlabel = "Attack",             # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

#----------
## Draw density plot of "Attack" and "Defense" columns
#----------

df_pokemon.plot.kde(
    y = ["Attack", "Defense"],
    color = ["blue", "red"], # Colors for each column
    title = "Density Plot of Pokemon Attack and Defense",  # Title of the plot
    xlabel = "Value",              # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot


#--------------------------------------------------------------------------------------------------------#
#------------------------------------------- 3. Box plot ------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
'''
Box plot (or box-and-whisker plot) is a graphical representation of the distribution of a dataset
that displays the median, quartiles, and potential outliers.

Also support notched box plot by setting notch = True.
'''

#################################
##    df.plot(kind = "box")    ##
#################################

#----------
## Draw box plot of "Attack" column
#----------

df_pokemon.plot(
    kind = "box",
    column = "Attack",
    color = "purple",             # Color of the box
    title = "Box Plot of Pokemon Attack",  # Title of the plot
    ylabel = "Attack",             # Label for the y-axis
    figsize = (8, 6)              # Size of the figure
)
plt.show() # Display the plot

#----------
## Draw box plot of "Attack" between different "Generation"
#----------

df_pokemon.plot(
    kind = "box",
    column = "Attack",            # Dependent variable
    by = "Generation",            # Group by "Generation" column
    notch = True,
    color = "purple",             # Color of the box
    title = "Box Plot of Pokemon Attack by Generation",  # Title of the plot
    ylabel = "Attack",             # Label for the y-axis
    xlabel = "Generation",         # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot

#########################
##    df.plot.box()    ##
#########################

#----------
## Draw box plot of "Attack" column
#----------

df_pokemon.plot.box(
    column = "Attack",           # Dependent variable
    color = "green",             # Color of the box
    title = "Box Plot of Pokemon Attack",  # Title of the plot
    ylabel = "Attack",             # Label for the y-axis
    figsize = (8, 6)              # Size of the figure
)
plt.show() # Display the plot

#----------
## Draw box plot of "Attack" between different "Generation"
#----------

df_pokemon.plot.box(
    column = "Attack",            # Dependent variable
    by = "Generation",            # Group by "Generation" column
    notch = True,
    color = "green",             # Color of the box
    title = "Box Plot of Pokemon Attack by Generation",  # Title of the plot
    ylabel = "Attack",             # Label for the y-axis
    xlabel = "Generation",         # Label for the x-axis
    figsize = (10, 6)              # Size of the figure
)
plt.show() # Display the plot