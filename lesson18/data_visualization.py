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

st.subheader("Genre Distribution")
fig = px.pie(books_df, names='Genre', title='most like genre (2009-2022)', color="Genre", color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of Fiction cs Non-Fiction Books over the years")
size = books_df.groupby(['Year', 'Genre']).size().reset_index(name='Count')
fig = px.bar(size, x = 'Year' , y = 'Count', color='Genre', title='Number of Fiction cs Non-Fiction Books over the years',
        color_discrete_sequence=px.colors.sequential.Plasma, barmode='group')
st.plotly_chart(fig)

st.subheader("Top 15 Authors by Counts of the books Published (2009-2022)")
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']
fig = px.bar(top_authors, x='Count', y='Author', orientation='h', title='Top 15 Authors by Counts of the books Published (2009-2022)', color='Count',
             color_continuous_scale =px.colors.sequential.Plasma, labels={'Count': 'Counts of books published', 'Author': 'Author'})
st.plotly_chart(fig)

st.subheader('filter data by Genre')
genre_filter = st.selectbox('Select Genre', books_df['Genre'].unique())
filter_df = books_df[books_df['Genre'] == genre_filter]
st.write(filter_df)
