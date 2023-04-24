# Project name : Competitive analysis for Restaurants in the US through Yelp Ratings

!![2](https://user-images.githubusercontent.com/125951399/223501783-a8e20546-255b-45a2-87ef-efad7e509056.JPG)


The main goal of the project is to visualize the different restaurants types and their review counts in the cities of the US. This can be helpful in the competitive analysis for a product manager of the food business.

## Project Goals

1. Using the data to compare the performance of different businesses in the food industry.
2. Business ratings and reviews: showing the distribution of ratings and reviews for different types of restaurants. 
3. Understanding the user behavior: exploring the patterns of user behavior, such as

     a) which types of businesses they tend to review the most.
  
     b) what times of day they are most active.
  
     c) which areas they are most likely to search in the food business.


## Design

Literature review has been performed to identify the criteria of a path creation for visualization. 
!![3](https://user-images.githubusercontent.com/125951399/223502590-00d594c6-99d3-4804-8432-6fa868149d14.JPG)


**Literature review:**

Kaleru, S., & Dhanikonda, S. R. (2018). Exploratory Data Analysis and Latent Dirichlet Allocation on Yelp Database. Int. J. Appl. Eng. Res, 13(21), 15035-15039.
http://ripublication.com/ijaer18/ijaerv13n21_28.pdf

Alamoudi, E. S., & Al Azwari, S. (2021, March). Exploratory data analysis and data mining on yelp restaurant review. In 2021 National Computing Colleges Conference (NCCC) (pp. 1-6). IEEE.
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9428850


**Design Path**

1. Exploration analysis : Exploring correlations between user behaviors, reviews,  and different restaurant business. 
2. Understanding the graphs and visualization used in literature review to implement the kind of visualization needed for the project. 
3. Draft design: brainstorming ideas of analysing the data which is understood by users. 
4. Data cleaning : brainstorming on cleaning the data. The attributes were split into different categories such as different restaurant types. The days and timings have been split from the raw data. The data was initially split into different restaurant types and later merged as a single file called ‘yelp_merged.csv’.
5. Developing the application for visualization 
6. Merging  files and uploading on Github. Deploying on the Streamlit app called ‘app.py’ on Github (https://cmu-ids-spring-2023-xinyu-natasha-app-w1d0l4.streamlit.app/)
7. Write-up

The visual encodings and interaction techniques were chosen based on the literature review and exploration analysis ideation through brainstorming sessions. 

**Visualization 1:** Scatter plot for different restaurant types
This graph gives an overview of the restaurant type and displays the complete dataset. It also displays a scatter plt of the review counts as per the city. 

**Visualization 2:** The ratings for different cities in the US
This graph shows the density of different yelp ratings for various restaurants in the US. The ratings vary from 1 to 5, where 1 is the lowest rating and 5 is the highest. The visualization lets an user view the experiences of people with a restaurant as per the ratings allocated. We can view the density of satisfied ratings in different cities.

**Visualization 3:** Review counts for different cities in the US
This bar graph shows the number of review counts for the different cities in the US. This helps in understanding the places where rating a restaurant is more popular which can be helpful in marketing of a business and its growth. This also shows how the ratings change the perspective of people towards a restaurant. It is more likely that a highly rated restaurant would be visited by more people in the future as compared to a lower rating. This analysis also helps in understanding where restaurant ratings are popular.

**Visualization 4:** Scatterplot on maps
The scatterplot on maps enables an uder to select the rating for a restaurant and list the restaurant names. It also displays the density of the restaurants on the map of the US. This is a good visualization to understand how restaurants of different ratings are scattered across the country. 

**Visualization 5:** Heatmap of Restaurant Types and Time of the day
This visualization shows the heatmap of the restaurant type count and the time of the day. This analysis gives an insight of the popularity of different restaurant types such as burgers, pizza, bakeries, coffee, etc. in a given time of the day. This will enable businesses in growing their production on certain time of the day based on what the restaurant offers.

**Visualization 6:** Bar chart for restaurant type and ratings
This visualization has a sidebar on the left side of the application page where an user can select the restaurant type and the city. This gives the user the count of the restaurants as per the yelp ratings. 

**Visualization 7:** Line Graph for review counts for different cities in the US
The line graph helps an user understand the review trends for different cities. This is useful in understanding how reviews help in improving the restaurant businesses across different cities in the US.

Alternative visualization that were considered are as follows : -

1. Creating a heatmap with time of the day as grid and cities for different yelp ratings.
2. Creating visualizations with other attributes such as - pet friendly, take outs, outdoor seating, parking options, theme of the restaurant such as romantic, casual, etc.
3. Creating a scatterplot map where the name of the restaurant is displayed when the cursor is hovered over.

The ultimate choices were arrived through better understanding of the goal of the project. We chose to focus on restaurant types and their yelp ratings. Hence, the alternative visualization options were dropped from the project.


## Development

The breakdown of the work among the team members is mentioned below:

1. Exploration analysis : Xinyu & Natasha 
2. Understanding the graphs and visualization used in literature review to implement the kind of visualization needed for the project : Xinyu & Natasha 
3. Draft design: brainstorming ideas of analysing the data which is understood by users: Xinyu
4. Data cleaning : Xinyu
5. Developing the application for visualization on Streamlit: Natasha 
6. Merging  files and uploading on Github: Natasha
7. Write-up : Natasha & Xinyu

On an average the project required 40 hours to develop the application. The time was split over the two weeks between 2 members. Writing the code for visualization took the most time.


## Success Story

The project has helped understand how to build an application for an interactive data visualization with real world data. The project helped us to learn how to push codes on Github which an important platform for data science enthusiasts. From the visualization, it has been observed that bigger cities such as Philadelphia, Nashville, Santa Barbara have higher review counts and how reviews are popular in bigger cities. Coffee is preferred more in the morning and evenings whereas bars are distributed throughout the day. Visualization of data can help businesses understand patterns, trends and growth opportunities.
