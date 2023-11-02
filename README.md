<details>
<summary><b>🚔 Crime Data Analysis and Visualization 📊</b></summary>

This project is focused on analyzing and visualizing crime data, specifically vehicle thefts 🚗🔒, using Python 🐍 and popular data science libraries such as Pandas 🐼, Matplotlib 📈, and Folium 🗺️. The code provided here demonstrates how to load a dataset of crime incidents, filter it for geographical information in 2017, and create engaging visualizations 📈🗺️.

<details>
<summary><b>Getting Started 🚀</b></summary>

1. 📥 Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git

The project consists of the following main components:
Data Loading 📂: The code loads the crime dataset from the input directory and filters the data to remove rows with missing or invalid geographical information (latitude and longitude).
Vehicle Theft Analysis 🚗🔍: The code analyzes the dataset to determine when vehicle thefts are most likely to occur. It groups incidents by the hour of the day and creates a dynamic bar chart to visualize the distribution of thefts throughout the day.
Heatmap Visualization 🗺️🔥: The code uses Folium to create an interactive heatmap of vehicle thefts specifically at 6 PM, which is considered the worst time for thefts. The heatmap provides a visual representation of theft hotspots.
