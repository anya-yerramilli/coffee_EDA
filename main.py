import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt

# title of project
st.title("Coffee Quality Exploratory Data Analysis")
st.markdown('---')

# names + bio (grade + experience)
st.header("The Team")
st.write(
  "Hey I am Daniel I am in 12th Grade and I like to play video games, watch movies, and read books that interest me."
)
st.write(
  "My name is Valeria and I am in 11th grade. I like to paint and draw.")
st.write(
  "My name is Nathan Yee and I'm in 11th grade. I like to swim and play waterpolo, and I watch movies in my free time."
)
st.write(
  "My name is Jasmine Li and I'm in 11th grade. I enjoy playing instruments and music production, as well as reading and creative writing."
)
st.write(
  "My name is Ellie Chan and I'm in 7th grade. I like to practice doing archery and I like playing with my dog."
)
st.markdown('---')


# the dataset
st.header("About the Dataset")
coffee_dataframe = pd.read_csv("coffee.csv")
st.write(coffee_dataframe.head())
st.write('This data comes from the Coffee Quality Institution (CQI) which is a nonprofit whose mission is to better quality coffee worldwide. The data contains the country of origin, farm name, lot number, mill and other data.')

# context for dataset (importance, hypothesis)
st.write('<HYPOTHESIS>')
st.write('<IMPORTANCE OF DATA + ANALYSIS>')
st.markdown("---")

# cleaning the data
columns_to_drop = [
  'Grading Date', 'Owner', 'Region', 'Certification Body', 'Number of Bags',
  'Bag Weight', 'Unnamed: 0', 'ID', 'Farm Name', 'Lot Number', 'Mill',
  'ICO Number', 'Company', 'Producer', 'In-Country Partner', 'Status',
  'Certification Address', 'Certification Contact', 'Defects', 'Uniformity',
  'Clean Cup', 'Sweetness'
]

coffee_dataframe.drop(columns_to_drop, axis=1, inplace=True)
coffee_dataframe.dropna(inplace=True)
coffee_dataframe.reset_index(drop=True, inplace=True)

# 3-4 visualizations
st.header("Visualizing the Data")

# SCATTER MATRIX
st.write("What is the relationship between the aroma, flavor, aftertaste, and acidity of coffee?") 
numerical_coffee_df = coffee_dataframe[[
  'Aroma',
  'Flavor',
  'Aftertaste',
  'Acidity',
]]
fig = px.scatter_matrix(numerical_coffee_df)
st.plotly_chart(fig)
st.write('We can see a common pattern between the relationships of the different categories of Flavor, Aroma, Aftertaste, and Acidity, that being they are all displayed in a linear-like formation. This pattern can reflect the value of coffee, as the types of coffee with the best flavor and aftertaste, often have the best Aroma and Acidity and vice versa. The outliers illustrated in the graphs are priminenet examples of the best and worst types of coffe found across the globe.')
st.markdown("---")

# DOT CHART 
st.write("Which processing methods are commonly used in each country?") 
fig = plt.figure(figsize=(10, 6))
sns.scatterplot( data=coffee_dataframe, x="Country of Origin", y="Processing Method")
plt.title('Processing Method Popularity in Countries\n')
plt.xticks(rotation = 90) 
st.pyplot(fig)
st.write('In almost every coffee growing country, farms use the washed/wet, natural dry, and honey method. Countries with the best tasting coffee such as Colombia and Taiwan use numerous methods to grow their crops. Whereas in places such as Kenya and Uganda, these drier, less arable regions use the less popular wet hulling or semi-lavado methods.')
st.markdown("---")

#EXPIRATION CHART
st.write("When do most coffee bags expire?") 
coffee_dataframe['Expiration'] = coffee_dataframe['Expiration'].apply(
  lambda x: pd.to_datetime(x))
coffee_dataframe.sort_values(by=['Expiration'], inplace=True)
coffee_dataframe['Expiration'] = coffee_dataframe['Expiration'].apply(
  lambda d: str(d.year) + '-' + str(d.month) + '-' + str(d.day))

fig = plt.figure(figsize=(10, 4))
sns.countplot(x = "Expiration", data = coffee_dataframe)
plt.title('Expiration Dates')
plt.xticks(rotation = 90, fontsize = 'x-small') 
st.pyplot(fig)
st.write('<ANALYSIS>')
st.markdown("---")


