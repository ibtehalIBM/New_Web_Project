import streamlit as st
import pandas as p


st.set_page_config(layout='wide')
col1, col2 = st.columns(2)


with col1:
    st.image('images\photo.png')


with col2:
    st.title('Ibtehal')
    content = """
                    Hi,\n
                    my name is Ibtehal,\n
                    This is my web application.\n
                """

    st.info(content)

content2='''
     more information about me, \n
     again more info, \n
     again,  \n
     '''
st.write(content2)


col3,col4 = st.columns(2)
df = p.read_csv('data.csv',sep=';')

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])

