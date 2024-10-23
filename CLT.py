import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Demonstration of CLT using StreamLit')
st.subheader('By G Prashant')
st.write('This app aims to prove the definition of CLT using a thousand flips and randomly selecting the samples, finding the means of the samples and plotting the histogram of it , thus producing an approximation of the normal distribution')

heads = st.number_input(label='P(Heads)', min_value=0.0, max_value=1.0, value=0.5)
title = st.text_input('Graph Title')

binomial = np.random.binomial(1, heads, 1000)

mean_list = [np.random.choice(binomial, 100, replace=True).mean() for _ in range(1000)]

fig, ax = plt.subplots()
ax = plt.hist(mean_list)
plt.title(title)
st.pyplot(fig)

