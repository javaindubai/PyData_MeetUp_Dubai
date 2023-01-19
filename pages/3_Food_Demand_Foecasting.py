
import pandas as pd
import plotly.figure_factory as ff
import streamlit as st
# import streamlit.components.v1 as components

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Food Demand Forecasting')


@st.cache(suppress_st_warning=True)
def load_data(numberOfRows):
    data = pd.read_csv('training_dataset.csv', nrows=numberOfRows)
    return data


@st.cache(suppress_st_warning=True)
def load_center_data(nrows):
    data = pd.read_csv('center_info.csv', nrows=nrows)
    return data


@st.cache
def load_meal_data(nrows):
    data = pd.read_csv('meal_info.csv', nrows=nrows)
    return data


weekly_data = load_data(1000)
center_info_data = load_center_data(1000)
meal_data = load_meal_data(1000)

# WeeklyDemand Data
st.subheader('Weekly Demand Data')
st.write(weekly_data)
# st.markdown('----')
st.bar_chart(weekly_data['num_orders'][:100])
# st.line_chart(weekly_data['base_price'])
# st.bar_chart(pd.DataFrame(weekly_data[:100],  columns=['num_orders', 'base_price']))
st.markdown('----')
df = pd.DataFrame(weekly_data[:200], columns=['num_orders', 'checkout_price', 'base_price'])
# st.line_chart(df)
df.hist()
st.pyplot()
st.markdown('----')
st.line_chart(df)
st.markdown('----')
chart_data = pd.DataFrame(weekly_data[:100], columns=['num_orders', 'base_price'])
st.area_chart(chart_data)
st.markdown('----')
# Center Information
st.subheader('Center Information')
if st.checkbox('Show Center Information data'):
    st.subheader('Center Information data')
    st.write(center_info_data)
    st.markdown('----')

st.bar_chart(center_info_data['region_code'])
st.markdown('----')
st.bar_chart(center_info_data['center_type'])
st.markdown('----')

hist_data = [center_info_data['center_id'], center_info_data['region_code']]
group_labels = ['Center Id', 'Region Code']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
st.plotly_chart(fig, use_container_width=True)
st.markdown('----')
st.subheader('Meal Information')
st.write(meal_data)
st.markdown('----')
st.bar_chart(meal_data['cuisine'])
st.markdown('----')
agree = st.button('Click to see Categories of Meal')
if agree:
    st.bar_chart(meal_data['category'])
    st.markdown('----')

data = load_data(1000)
hist_data = [data['checkout_price'], data['base_price'], data['num_orders']]
group_labels = ['checkout_price', 'base_price', 'num_orders']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
st.plotly_chart(fig, use_container_width=True)