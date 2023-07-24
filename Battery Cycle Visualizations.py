#!/usr/bin/env python
# coding: utf-8

# # 1_1 Multiple Line Chart: Predicted Number of EV’s in the Parc by Make and Year of Construction

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

def plot_line_graph(csv_file_path):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Extract car brands from the first column
    car_brands = df.iloc[:, 0]

    # Extract data for the last 5 years (columns)
    last_5_years_data = df.iloc[:, -5:]

    # Create the line graph
    plt.figure(figsize=(15, 10))  # Set the figure size to 15 (width) and 10 (height)
    for i in range(len(last_5_years_data.columns)):
        plt.plot(car_brands, last_5_years_data.iloc[:, i], label=str(last_5_years_data.columns[i]))

    plt.xlabel("Car Brands", fontsize=16)  # Set x-axis label font size to 16
    plt.ylabel("Number of EVs", fontsize=16)  # Set y-axis label font size to 16
    plt.title("Predicted Number of EVs in the Parc by Make and Year of Construction", fontsize=16)  # Set title font size to 16
    plt.legend(fontsize=16)
    plt.xticks(rotation=90, ha='right')  # Rotate x-axis labels horizontally and align them to the right
    plt.grid(True)

    # Display the plot
    plt.show()

if __name__ == "__main__":
    csv_file_path = "https://raw.githubusercontent.com/varunraaju/1_1-Predicted-Number-of-EV-s-in-the-Parc-by-Make-and-Year-of-Construction/main/1_1.csv"  # Replace with the actual path to your CSV file
    plot_line_graph(csv_file_path)


# # 1_3 Top 10 Makes of EVs in the Parc 

# In[40]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_donut_pie_chart(csv_file_path):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Extract car brands from the first column
    car_brands = df.iloc[:, 0]

    # Extract data for the last year (last column)
    last_year_data = df.iloc[:, -1]

    # Calculate percentages
    total_ev_count = last_year_data.sum()
    percentages = (last_year_data / total_ev_count) * 100

    # Explode the top percentage
    max_percentage_index = np.argmax(percentages)
    explode = [0] * len(car_brands)
    explode[max_percentage_index] = 0.1

    # Create the donut pie chart
    plt.figure(figsize=(8, 8))  # Set the figure size to 10 (width) and 10 (height)

    # Outer ring (donut)
    plt.pie(percentages,  startangle=-30, explode=explode, wedgeprops=dict(width=.6), autopct='%1.1f%%')

    # Inner circle (white)
    centre_circle = plt.Circle((0, 0), 0.2, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Add labels outside
    plt.gca().set_aspect('equal')
    plt.legend(car_brands, bbox_to_anchor=(1, .65), loc='best')
    plt.title("Top 10 Makes of EVs in the Parc", fontsize=16)

    
    plt.show()
    # Display the plot
    plt.show()

if __name__ == "__main__":
    csv_file_path = "https://raw.githubusercontent.com/varunraaju/1_3-Top-10-Makes-of-EVs-in-the-Parc-/main/1_3.csv"  # Replace with the actual path to your CSV file
    plot_donut_pie_chart(csv_file_path)


# # 1_5 Bar chart of the number of EVs by year of construction 

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt

def plot_stacked_horizontal_bar_graph_from_github(csv_file_path):
    # Read the CSV file from GitHub into a Pandas DataFrame
    gf3 = pd.read_csv(csv_file_path)

    # Create a figure
    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(7)

    # Create a horizontal bar chart with font size 20 for the title
    ax = gf3.plot(x='YEAR', kind='barh', stacked=True, title='BAR CHART OF THE NUMBER OF EVS BY YEAR OF CONSTRUCTION', figsize=(15, 10))

    # Invert the y-axis
    ax.invert_yaxis()

    # Set labels and title with modified font size
    ax.set_xlabel('TOTAL QUANTITY BUILT', fontsize=15)
    ax.set_ylabel('YEAR', fontsize=15)
    ax.set_title('BAR CHART OF THE NUMBER OF EVS BY YEAR OF CONSTRUCTION', fontsize=20)

    # Set background color and remove grid
    ax.set_facecolor('white')

    # Add box outline
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(1)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    csv_file_path = "https://raw.githubusercontent.com/varunraaju/1_5-Bar-chart-of-the-number-of-EVs-by-year-of-construction-/main/1_5.csv"
    plot_stacked_horizontal_bar_graph_from_github(csv_file_path)


# # 3_2 Bar chart of the number of EVs by year of construction 

# In[50]:


import pandas as pd
import matplotlib.pyplot as plt

def plot_stacked_horizontal_bar_graph_from_github(csv_file_path):
    # Read the CSV file from GitHub into a Pandas DataFrame
    df3_2 = pd.read_csv(csv_file_path)

    # Create a figure
    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(7)

    # Create a horizontal bar chart with font size 20 for the title
    ax = df3_2.plot(x='YEAR', kind='barh', stacked=True, title='BAR CHART OF THE NUMBER OF EVS BY YEAR OF CONSTRUCTION', figsize=(15, 10))

    # Invert the y-axis
    ax.invert_yaxis()

    # Set labels and title with modified font size
    ax.set_xlabel('TOTAL QUANTITY BUILT', fontsize=15)
    ax.set_ylabel('YEAR', fontsize=15)
    ax.set_title('BAR CHART OF THE NUMBER OF EVS BY YEAR OF CONSTRUCTION', fontsize=16)

    # Set background color and remove grid
    ax.set_facecolor('white')

    # Add box outline
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(1)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    csv_file_path = "https://raw.githubusercontent.com/varunraaju/3_2-Bar-chart-of-the-number-of-EVs-by-year-of-construction-/main/3_2.csv"
    plot_stacked_horizontal_bar_graph_from_github(csv_file_path)


# # 5_1 Total Number of EVs by Make over Time in the UK

# In[52]:


import pandas as pd
import matplotlib.pyplot as plt

def plot_multi_line_graph(csv_file_path):
    # Read the CSV file from GitHub into a Pandas DataFrame
    df = pd.read_csv(csv_file_path, index_col=0)

    # Transpose the DataFrame for plotting
    df_transposed = df.T

    # Create the multi-line plot
    plt.figure(figsize=(15, 10))  # Set the figure size
    for brand in df_transposed.columns:
        plt.plot(df_transposed.index, df_transposed[brand], label=brand)

    # Set labels and title
    plt.xlabel("Year",fontsize=15)
    plt.ylabel("Number of EVs",fontsize=15)
    plt.title("Total Number of EVs by Make over Time in the UK", fontsize=16)
    plt.legend()

    # Display the plot
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    csv_file_path = "https://raw.githubusercontent.com/varunraaju/5_1-Total-Number-of-EVs-by-Make-over-Time-in-the-UK/main/5_1.csv"
    plot_multi_line_graph(csv_file_path)


# In[ ]:




