import streamlit as st
import pandas as pd
import altair as alt

# Creating a title for the application
st.title('Competitive analysis for Restaurants in the US through Yelp Ratings')


# Visualization 1: Scatterplot for different restaurant type

# Load the cleaned Yelp dataset
yelp_df = pd.read_csv('yelp_merged.csv')

# Sidebar filters
name_filter = st.sidebar.selectbox('Select the type of restaurant for the Visualization 1', yelp_df['type'].unique())


# Apply filters to the dataset
filtered_df = yelp_df[(yelp_df['type'] == name_filter)]

# Calculate the total review count for each restaurant
restaurant_review_count = filtered_df.groupby('city')['review_count'].sum().reset_index()

# Create scatterplot
scatterplot = alt.Chart(restaurant_review_count).mark_circle().encode(
    x='city',
    y='review_count',
    tooltip=['city', 'review_count']
).properties(width=800)
st.header('Visualization 1: Scatterplot for different restaurant type')
st.markdown('The below is the data set for the selected restaurant type in the US. the dataset will give the location, rating, type and timing of the restaurant. The data set is found on https://www.yelp.com/dataset and it is called Yelp Open Dataset. The dataset has 908,915 tips by 1,987,897 users. Since it is a large file, we have taken the data input from the first 1000 rows to get an idea of the restaurant business in the US. There is an option to select the restaurant type on the left sidebar in order to view the dataset.')

# Show the filtered dataset and scatterplot
st.write(filtered_df)
st.altair_chart(scatterplot, use_container_width=True)



# Visualization 2: Scatter plot for ratings in different cities

# Load data
#@st.cache_data
#def load_data():
    #yelp_url = "D:\Spring 23 semester\Interactive Data Science\HW3\yelp_merged.csv"
    #yelp_url = "https://github.com/CMU-IDS-Spring-2023/xinyu-natasha/blob/e88c7e22c8876e60034bdc263da518e497b15267/yelp_merged.csv"
    #return pd.read_csv(yelp_url)
#df = load_data()

df = pd.read_csv('yelp_merged.csv')
# Create scatterplot
chart = alt.Chart(df).mark_point().encode(
    x=alt.X("city", scale=alt.Scale(zero=False)),
    y=alt.Y("stars", scale=alt.Scale(zero=False)),
    color=alt.Y("stars")
).properties(
    width=600, height=400
).interactive()

st.header('Visualization 2: The ratings for different cities in the US')
st.markdown('The different cities in the US have different ratings which depends on the stars lying between 1 to 5, where 1 is the least rated and 5 is the highest rated. The rating density can be viewed for different cities. This will help us understand the kind density of differently rated restaurant businesses in the US.')

st.write(chart)
            

# Visualization 3: Bar graph

chart1=alt.Chart(df).mark_bar().encode(
    x='city',
    y='review_count',
    
)
st.header('Visualization 3: Review counts for different cities in the US')
st.markdown('The following graph shows the bar chart for differnt cities and their review counts. It can be an indication of how popular customer ratings are in different cities in the US.')

st.write(chart1)



# Visualization 4: Scatterplot on Map

st.header('Visualization 4: Scatterplot on maps')
st.markdown('The below scatterplot can be useful in providing insights on the different restaurant ratings on the map of the US. There is a checkbox to show the names of the restaurants for the selected rating.')

option = st.selectbox("Select the rating", ['1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'])

# Filter data based on selected option
if option == "1":
    
    filtered_data = yelp_df[(yelp_df['stars'] == 1)]
elif option == "1.5":
    filtered_data = yelp_df[(yelp_df['stars'] == 1.5)]
elif option=="2":
    filtered_data = yelp_df[(yelp_df['stars'] == 2)]
elif option=="2.5":
    filtered_data = yelp_df[(yelp_df['stars'] == 2.5)]
elif option=="3":
    filtered_data = yelp_df[(yelp_df['stars'] == 3)]
elif option=="3.5":
    filtered_data = yelp_df[(yelp_df['stars'] == 3.5)]
elif option=="4":
    filtered_data = yelp_df[(yelp_df['stars'] == 4)]
elif option=="4.5":
    filtered_data = yelp_df[(yelp_df['stars'] == 4.5)]
else:
    filtered_data = yelp_df[yelp_df['stars'] == 5]

# Create a map using st.map() function
st.map(filtered_data)

# Show names when zoomed in
if st.checkbox("Show names"):
    for i, row in filtered_data.iterrows():
        st.write(row["name"], (row["city"], row["state"]))


# Visualization 5 : Heatmap


st.header('Visualization 5: Heatmap of Restaurant Types and Time of the day')
st.markdown('Studying the heatmap of the restaurant types at different times of the day is important to understand which type of restaurants are popular during which particular time of the day.')

# combine columns M, N, and O into a new column 'combined'
yelp_df['day'] = yelp_df['Monday'] + yelp_df['Tuesday'] + yelp_df['Wednesday'] + yelp_df['Thursday']+ yelp_df['Friday'] + yelp_df['Saturday'] + yelp_df['Sunday']
# saving the resulting dataframe
yelp_df.to_csv('yelp_merged.csv', index=False)


data5 = pd.read_csv('yelp_merged.csv')

# Drop any NaN values
data5 = data5.dropna()

# Create heatmap
heatmap = alt.Chart(data5).mark_rect().encode(
    x=alt.X('day:O', title='Time of the Day'),
    y=alt.Y('type:O', title='Type of Restaurant'),
    color='count()',
    tooltip=['type', 'day', 'count()']
).properties(
    width=1000,
    height=800,
    title='Restaurant Types and Time'
).interactive()

# Display heatmap in Streamlit
st.altair_chart(heatmap)




# Visualization 6 : Bar Graph

st.header('Visualization 6: Bar chart for restaurant type and ratings')
st.markdown('This visualization enables an user to select thr restaurant type and the city which is dispalyed as a sidebar on the application page. This helps an user to understand the count of different ratings for the selected restaurant type and the city.')

# Read the data from CSV file
data6 = pd.read_csv("yelp_merged.csv")

# Create a sidebar with filter options
type_filter = st.sidebar.selectbox("Select Type of restaurant for Visualization 6", data6["type"].unique())
city_filter = st.sidebar.selectbox("Select City for Visualization 6", data6["city"].unique())


# Filter data based on user selection
filtered_df6 = data6[(data6["type"] == type_filter) & (data6["city"] == city_filter)]
#filtered_df6 = data6[(data6["type"] == type_filter)]

# Group data by day and count occurrences
grouped_df = filtered_df6.groupby(["stars"]).size().reset_index(name="Count")

# Create bar chart with Altair
chart6 = (
   alt.Chart(grouped_df)
   .mark_bar()
    .encode(
        x="stars:O",
        y="Count:Q",
        color=alt.Color("stars:N", legend=None),
        tooltip=[alt.Tooltip("stars:N"), alt.Tooltip("Count:Q")],
    )
    .properties(width=600, height=400)
).interactive()


st.altair_chart(chart6)


    
if st.checkbox("Show names", key="checkbox1"):
    for i, row in data6.iterrows():
        st.write(row["name"], (row["city"], row["stars"]))


# Visualization 7: Line graph

st.header('Visualization 7: Line Graph for review counts for different cities in the US')

st.markdown('The line graph helps an user understand the review trends for different cities. This is useful in understanding how reviews help in improving the restaurant businesses across different cities in the US.')

# Load the Yelp_merged.csv file
df7 = pd.read_csv("yelp_merged.csv")

# Group the data by business location and calculate the average rating and number of reviews
location_data = df7.groupby("city")[["stars", "review_count"]].mean().reset_index()

# Create a line graph showing the average rating and number of reviews for each business location
chart7 = alt.Chart(location_data).mark_line().encode(
    x="city",
    y="stars",
    color=alt.value("red")
).properties(
    width=1000,
    height=800,
    title="Review counts by Business Location"
) + alt.Chart(location_data).mark_line().encode(
    x="city",
    y="review_count",
    color=alt.value("blue")
).properties(
    width=1000,
    height=800,
    title="Number of Reviews by Business Location"
).interactive()

# Display the graph using Streamlit
st.altair_chart(chart7)





