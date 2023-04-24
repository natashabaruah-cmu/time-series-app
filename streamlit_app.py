#%%

from re import U
import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def load_data():
    yelp_url = "https://github.com/github/CMU-IDS-Spring-2023/xinyu-natasha/blob/b212af08a6cffbb434f3c8a2795a579e092792fd/streamlit_app.py"
    return pd.read_csv(yelp_url)

df = load_data()

st.write("Let's look at raw data in the Yelp Data Frame.")

st.write(df)



chart = alt.Chart(df).mark_point().encode(
    x=alt.X("city", scale=alt.Scale(zero=False)),
    y=alt.Y("stars", scale=alt.Scale(zero=False)),
    color=alt.Y("stars")
).properties(
    width=600, height=400
).interactive()

st.write(chart)

st.markdown("The ratings per city")
            


chart1=alt.Chart(df).mark_bar().encode(
    x='city',
    y='review_count',
    
)
st.write(chart1)

st.markdown("Graph for the number of reviews in a city")


##chart = alt.Chart(df).encode(
    #x='count(city)',
    #y='city'
#)
