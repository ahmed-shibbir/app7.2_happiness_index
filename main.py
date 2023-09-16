
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataframe
data = pd.read_csv("happy.csv")
# print(data)

# Set the title
st.title("In Search for Happiness")

# Extract column names
cols = list(data.iloc[:,1:].columns)

# Select boxes for x and y values
option_x = st. selectbox("Select the data for the x axis",
                         (cols))
option_y = st. selectbox("Select the data for the y axis",
                         (cols))
# Match case for x values
match option_x:
    case 'happiness':
        x_data = data['happiness']

    case 'gdp':
        x_data = data['gdp']

    case 'social_support':
        x_data = data['social_support']

    case 'life_expectancy':
        x_data = data['life_expectancy']

    case 'freedom_to_make_life_choices':
        x_data = data['freedom_to_make_life_choices']

    case 'generosity':
        x_data = data['generosity']

    case 'corruption':
        x_data = data['corruption']

# Match case for y values
match option_y:
    case 'happiness':
        y_data = data['happiness']

    case 'gdp':
        y_data = data['gdp']

    case 'social_support':
        y_data = data['social_support']

    case 'life_expectancy':
        y_data = data['life_expectancy']

    case 'freedom_to_make_life_choices':
        y_data = data['freedom_to_make_life_choices']

    case 'generosity':
        y_data = data['generosity']

    case 'corruption':
        y_data = data['corruption']

# st.subheader(f"{option_x} and {option_y}")

# Create a scatter plot
fig = px.scatter(x=x_data, y=y_data, labels=[option_x,option_y],
                 title=f"Scatter Plot: {option_x.capitalize()} and "
                 f"{option_y.capitalize()}",height=400, width=600)

# Format the labels
fig.update_xaxes(title_text=f"<b>{option_x.capitalize()}</b>")
fig.update_yaxes(title_text=f"<b>{option_y.capitalize()}</b>")

# Displace the figure
st.plotly_chart(fig)

# Show the plot
# fig.show()