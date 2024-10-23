import time

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from pyarrow.dataset import dataset

st.title('Data Analyzer')
st.write('Using this app, you can analyse the dataset, visualize the columns of the dataset and get insights')

dataset_file = st.file_uploader('Upload your dataset')
@st.cache_data
def load_file(dataset_file):
    time.sleep(3)
    if dataset_file is not None:
        dataset = pd.read_csv(dataset_file)
    else:
        dataset = pd.read_csv('datasets/penguins_lter.csv')
    return dataset

dataset = load_file(dataset_file)

st.write(dataset.head())

num_category = dataset.select_dtypes(['number']).columns
species_names = dataset['Species'].unique()
# st.write(num_category)

st.subheader('Scatter plot visualization of numerical columns')
species_select = st.selectbox('Select the penguin species', species_names)
x_axis = st.selectbox('Select the x axis column', num_category)
y_axis = st.selectbox('Select the y axis column', num_category)
scatter_chart = (alt.Chart(dataset[dataset['Species'] == species_select], title=f'Scatter plot of {x_axis} and {y_axis}').
                 mark_circle().
                 encode(x=x_axis, y=y_axis, color='Species').
                 interactive())
st.altair_chart(scatter_chart, use_container_width=True)








