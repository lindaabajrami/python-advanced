import  streamlit as st
import  pandas as pd
import plotly.express as px

books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("bestselling book analysis")
st.write("this app  analyzes the amazon top selling books from 2009 to 2022")

st.subheader("summery statistics")
total_books = books_df.shape[0]
unique_title = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("total books", total_books)
col2.metric("unique titles", unique_title)
col3.metric("average rating", f'{average_rating:.2f}')
col4.metric("average price", f'${average_price:.2f}')

st.subheader('dataset preview')
st.write(books_df.head())

col1, col2, = st.columns(2)

with col1:
    st.subheader("top 10 book titles")
    top_title = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_title)

with col2:
        st.subheader("top 10 Authors")
        top_authors = books_df['Author'].value_counts().head(10)
        st.bar_chart(top_authors)