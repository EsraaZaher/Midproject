
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from PIL import Image
import base64
from datetime import datetime
import plotly.graph_objects as go
import time
def page1():
    def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_local('gamer.png')


    st.title("_Online Gaming Anxiety DASHBORD_" )
    st.write('https://www.kaggle.com/datasets/divyansh22/online-gaming-anxiety-data')
    
    df = pd.read_csv('Online Gaming Anxiety new.csv')
    
    box = st.sidebar.checkbox('_SHOW DATAFREAM_' , False , key = 1)
    if box:
        st.header('Sample of Data')
        st.dataframe(df.head(10))
    st.subheader('_comparison between GAD , SWL AND SPIN_')
    selectbox= st.selectbox('Select from this options' , ('SWL_T','GAD_T','SPIN_T'))
    
    
    if selectbox == 'SWL_T':
        st.write('SWL_T is the total score of satisfaction With Life, the higher your score the higher your sense of life satisfaction')
    if selectbox == 'GAD_T':
        st.write("GAD_T is the total score of General Anxiety dsorder, the higher your score the higher your Anxiety ")  
    if selectbox == 'SPIN_T':
        st.write("SPIN_T is the total score of Social Phopia Inventory, with higher scores indicating greater sererity of social Anxiety")   
        
        
    tab1 , tab2 , tab3 = st.tabs(['Hours' , 'Age' , 'Game'])

    with tab1:
        if selectbox == 'SWL_T':
            col1,col2 = st.columns(2)
            with col1:
                
                SWL = df.groupby('Hours')['SWL_T'].mean().reset_index()
                fig = px.line(SWL , x ='Hours' , y = 'SWL_T' )
                st.plotly_chart(fig , use_container_width= True)
            with col2:
                
                SWL1 = df.groupby(['Hours' , 'Gender'])['SWL_T'].mean().reset_index()
                fig = px.histogram(SWL1 , x='Hours', y='SWL_T',
                color='Gender', barmode='group' , title='Hours VS SWL_T')
                st.plotly_chart(fig , use_container_width= True)

        if selectbox == 'GAD_T':
            col1,col2 = st.columns(2)
            with col1:
                GAD = df.groupby('Hours')['GAD_T'].mean().reset_index()
                fig = px.line(GAD , x ='Hours' , y = 'GAD_T' )
                st.plotly_chart(fig , use_container_width= True)
            with col2:
                GAD1 = df.groupby(['Hours' , 'Gender'])['GAD_T'].mean().reset_index()
                fig = px.histogram(GAD1 , x='Hours', y= 'GAD_T',
                color='Gender', barmode='group' , title='HOURS VS GAD_T')
                st.plotly_chart(fig , use_container_width= True)
            
            
        if selectbox == 'SPIN_T':
            col1,col2 = st.columns(2)
            with col1:
                SPIN = df.groupby('Hours')['SPIN_T'].mean().reset_index()
                fig = px.line(SPIN , x ='Hours' , y = 'SPIN_T' )
                st.plotly_chart(fig , use_container_width= True)
            with col2:
                SPIN1 = df.groupby(['Hours' , 'Gender'])['SPIN_T'].mean().reset_index()
                fig = px.histogram(SPIN1, x='Hours', y='SPIN_T',
                color='Gender', barmode='group' , title='HOURS VS SPIN_T')
                st.plotly_chart(fig , use_container_width= True)
            
    with tab2:
        
        if selectbox == 'SWL_T':
            col1,col2 = st.columns(2)
            with col1:
                SWL = df.groupby('Age')['SWL_T'].mean().reset_index()
                fig = px.line(SWL , x ='Age' , y = 'SWL_T' )
                st.plotly_chart(fig , use_container_width= True)
            with col2:
                SWL1 = df.groupby(['Age' , 'Gender'])['SWL_T'].mean().reset_index()
                fig = px.histogram(SWL1, x='Age', y='SWL_T',
                color='Gender', barmode='group' , title='AGE VS SWL_T')
                st.plotly_chart(fig , use_container_width= True)
            
            
        if selectbox == 'GAD_T':
            col1,col2 = st.columns(2)
            with col1:
                
                GAD = df.groupby('Age')['GAD_T'].mean().reset_index()
                fig = px.line(GAD , x ='Age' , y = 'GAD_T' )
                st.plotly_chart(fig , use_container_width= True)
                
            with col2:
                GAD1 = df.groupby(['Age' , 'Gender'])['GAD_T'].mean().reset_index()
                fig = px.histogram(GAD1, x='Age', y='GAD_T',
                color='Gender', barmode='group' , title='AGE VS GAD_T')
                st.plotly_chart(fig , use_container_width= True)
            
            
        if selectbox == 'SPIN_T':
            col1,col2 = st.columns(2)
            with col1:
                SPIN = df.groupby('Age')['SPIN_T'].mean().reset_index()
                fig = px.line(SPIN , x ='Age' , y = 'SPIN_T' )
                st.plotly_chart(fig , use_container_width= True)
                
            with col2:
                
                SPIN1 = df.groupby(['Age' , 'Gender'])['SPIN_T'].mean().reset_index()
                fig = px.histogram(SPIN1, x='Age', y='SPIN_T',
                color='Gender', barmode='group' , title='AGE VS SPIN_T')
                st.plotly_chart(fig , use_container_width= True)
            
            
    with tab3:
        
        if selectbox == 'SWL_T':
            col1,col2 = st.columns(2)
            with col1:
                SWL = df.groupby('Game')['SWL_T'].mean().reset_index()
                fig = px.line(SWL , x ='Game' , y = 'SWL_T' )
                st.plotly_chart(fig , use_container_width= True)
                
            with col2:
                SWL1 = df.groupby(['Game' , 'Gender'])['SWL_T'].mean().reset_index()
                fig = px.histogram(SWL1 , x='Game', y='SWL_T',
                color='Gender', barmode='group' , title='GAME VS SWL_T')
                st.plotly_chart(fig , use_container_width= True)
            
            
            
        if selectbox == 'GAD_T':
            col1,col2 = st.columns(2)
            with col1:
                GAD = df.groupby('Game')['GAD_T'].mean().reset_index()
                fig = px.line(GAD , x ='Game' , y = 'GAD_T' )
                st.plotly_chart(fig , use_container_width= True)
            with col2:
                GAD1 = df.groupby(['Game' , 'Gender'])['GAD_T'].mean().reset_index()
                fig = px.histogram(GAD1, x ='Game', y = 'GAD_T',
                 color='Gender', barmode='group' , title='GAME VS GAD_T')
                st.plotly_chart(fig , use_container_width= True)
            
            
            
        if selectbox == 'SPIN_T':
            col1,col2 = st.columns(2)
            with col1:
                SPIN = df.groupby('Game')['SPIN_T'].mean().reset_index()
                fig = px.line(SPIN , x ='Game' , y = 'SPIN_T' )
                st.plotly_chart(fig , use_container_width= True)
            with col2:
                SPIN1 = df.groupby(['Game' , 'Gender'])['SPIN_T'].mean().reset_index()
                fig = px.histogram(SPIN1, x='Game', y='SPIN_T',
                color='Gender', barmode='group' , title='GAME VS SPIN_T')
                st.plotly_chart(fig , use_container_width= True)
                
  

    box = st.sidebar.checkbox('_WHYPLAY ANALYSIS_' , False , key = 2)
    if box: 
        st.subheader('_WHYPLAY ANALYSIS_')
        st.write('_Reason to play the game._')
        tab1 , tab2 , tab3 = st.tabs(['GAD_T' , 'SPIN_T' , 'SWL_T'])
        
        with tab1:
            fig = px.scatter(df.head(5000),x = 'whyplay' , y='GAD_T' , 
                            color = 'Gender' ,size='GAD_T' , title= 'CATEGORY VS GAD_T')
            st.plotly_chart(fig , use_container_width= True)
            
            
        with tab2:
            fig = px.scatter(df.head(5000),x = 'whyplay' , y='SPIN_T' , 
                            color = 'Gender' ,size='SPIN_T' , title= 'CATEGORY VS SPIN_T')
            st.plotly_chart(fig , use_container_width= True)
            
            
        with tab3:
            fig = px.scatter(df.head(5000),x = 'whyplay' , y='SWL_T' , 
                            color = 'Gender' ,size='SWL_T' , title= 'CATEGORY VS SWL_T')
            st.plotly_chart(fig , use_container_width= True)
            
        st.subheader('_** TOTAL WHYPLAY ANALYISS FOR WHO HAVE HIGH LEVEL OF GAD & SPIN and low level of SWL :_')
        df1 = df[ (df['GAD_T'] > 10) & (df['SPIN_T'] > 40) & (df["SWL_T"] < 20)]
        fig = px.sunburst(df1,path=['whyplay','Gender','Game'] , values = 'Hours' , title= 'WHYPLAY ANALYSIS'  ,height= 650 ,width= 650)
        st.plotly_chart(fig , use_container_width= True)
        
def page2():
    def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_local('gamer.png') 


    st.title("_Online Gaming Anxiety DASHBORD_" )
    
    df = pd.read_csv('Online Gaming Anxiety new.csv')
    
    box = st.sidebar.checkbox('_Age_' , False , key = 3)
    st.subheader('_Age Analysis_')
    st.write('_the Age of Gamer_')
    if box :
        age = st.slider('choose the Age' ,15 ,60 ,1 )
        new_df = df[df['Age'] == age]
        fig = px.scatter(new_df,x = 'whyplay' , y='Age' , 
        color = 'Gender' ,size='Age' , title= 'CATEGORY VS Age')
        fig.show()
    
    
    box = st.sidebar.checkbox('_Residence Analysis_' , False , key = 4)
    st.subheader('_Residence Analysis_')
    st.write('_Place where the gamer currently resides._')
    if box:
        st.map(df,
        latitude='latitude',
        longitude='longitude',color = 'Gender')
        
        Residence = st.selectbox('select the Residence' , df['Residence'].unique())
        r = df.groupby(['Residence' , 'Platform' ,'Gender','whyplay'] )[['SWL_T' , 'GAD_T' , 'SPIN_T']].mean().reset_index()
        new_df = r[r['Residence'] == Residence]
        tab1 , tab2 , tab3 = st.tabs(['SWL_T' , 'GAD_T' , 'SPIN_T'])

        with tab1:
            col1,col2 = st.columns(2)
            with col1 :
                fig = px.scatter(new_df, y='SWL_T', x='Platform' , color = 'Gender' , symbol='Gender' , title= f'Platform for {Residence}'.title())
                fig.update_traces(marker_size=10)
                st.plotly_chart(fig , use_container_width= True)

            with col2:

                fig = px.scatter(new_df, y='SWL_T', x='whyplay' , color = 'Gender' , symbol='Gender' , title= f'whyplay for {Residence}'.title())
                fig.update_traces(marker_size=10)
                st.plotly_chart(fig , use_container_width= True)
        with tab2:
            col1,col2 = st.columns(2)
            with col1 :
                fig = px.scatter(new_df, y='GAD_T', x='Platform' , color = 'Gender' , symbol='Gender' , title= f'Platform for {Residence}'.title())
                fig.update_traces(marker_size=10)
                st.plotly_chart(fig , use_container_width= True)

            with col2:

                fig = px.scatter(new_df, y='GAD_T', x='whyplay' , color = 'Gender' , symbol='Gender' , title= f'whyplay for {Residence}'.title())
                fig.update_traces(marker_size=10)
                st.plotly_chart(fig , use_container_width= True)
        with tab3:
            col1,col2 = st.columns(2)
            with col1 :
                fig = px.scatter(new_df, y='SPIN_T', x='Platform' , color = 'Gender' , symbol='Gender' , title= f'Platform for {Residence}'.title())
                fig.update_traces(marker_size=10)
                st.plotly_chart(fig , use_container_width= True)

            with col2:

                fig = px.scatter(new_df, y='SPIN_T', x='whyplay' , color = 'Gender' , symbol='Gender' , title= f'whyplay for {Residence}'.title())
                fig.update_traces(marker_size=10)
                st.plotly_chart(fig , use_container_width= True)
        
        
        col1,col2,col3 = st.columns(3)
        with col1:
            r = df.groupby('Residence')[['SWL_T' , 'GAD_T' , 'SPIN_T']].mean().reset_index()
            fig = px.histogram(r.head(500), x='SWL_T', y='Residence' , color_discrete_sequence=['purple' , 'red'])
            st.plotly_chart(fig , use_container_width= True)
        with col2:
            r = df.groupby('Residence')[['SWL_T' , 'GAD_T' , 'SPIN_T']].mean().reset_index()
            fig = px.histogram(r.head(500), x='GAD_T', y='Residence' , color_discrete_sequence=['purple' , 'red'])
            st.plotly_chart(fig , use_container_width= True)
        with col3:
            r = df.groupby('Residence')[['SWL_T' , 'GAD_T' , 'SPIN_T']].mean().reset_index()
            fig = px.histogram(r.head(500), x='SPIN_T', y='Residence' , color_discrete_sequence=['purple' , 'red'])
            st.plotly_chart(fig , use_container_width= True)
    box = st.sidebar.checkbox('_Work Analysis_' , False , key = 5)
    st.subheader('_Work Analysis_')
    st.write('_The Work status of the gamer._')
    if box:
        col1,col2 = st.columns(2)
        
        with col1:
            W = df.groupby('Work')[['SWL_T' , 'GAD_T' , 'SPIN_T']].mean().reset_index()
            fig = px.bar(W , x="Work", y=['SWL_T', 'GAD_T' , 'SPIN_T'], title="The Work status of GAD, SWL & SPIN")
            st.plotly_chart(fig , use_container_width= True)
            
        with col2:
            fig = px.bar(df , x="Work", y= 'Age' , color='Gender', barmode='group' ,title="The Work status of GAD, SWL & SPIN")
            st.plotly_chart(fig , use_container_width= True)
            
        labels = ['Student at college / university', 'Employed', 'Student at school',
       'Unemployed / between jobs']
        values = [7052, 2719, 2213, 1374]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        st.plotly_chart(fig , use_container_width= True)
        
    box = st.sidebar.checkbox('_Game Analysis_' , False , key = 6)
    st.subheader('_Game Analysis_')
    st.write('_The game that gamer play._')
    if box:
        col1,col2 = st.columns(2)
        with col1:
            fig = px.histogram(df.head(50) , x='Game',
                color="Playstyle",width=500 , title='the playstyle for Games')
            st.plotly_chart(fig , use_container_width= True)
        
        with col2:
            
            g = df.groupby('Game')['Hours'].mean().reset_index()
            fig =px.bar(g ,x = 'Game', y='Hours' , title = 'avrage hours for each game')
            st.plotly_chart(fig , use_container_width= True)
        
        
        
        fig = px.sunburst(df, path=['Game', 'Narcissism'], values='GAD_T',
                  color='Age',
                  color_continuous_midpoint=np.average(df['Age'], weights=df['GAD_T']) , title= ' Game Analysis',
                         height= 650 ,width= 650)
        st.plotly_chart(fig , use_container_width= True)

        
            

pages = {'Main Analysis' : page1 , 'Other Analysis' : page2}
select_page = st.sidebar.selectbox('_select page_', pages.keys())
pages[select_page]()
