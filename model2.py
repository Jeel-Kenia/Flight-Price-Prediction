import streamlit as st
from datetime import datetime, timedelta
import pickle

# st.set_page_config(layout="wide")

st.title(':blue[Flight Price Prediction]')
st.write(':violet[Select the necessary details to get the price of flight for the particular destination]')
st.write(' ')
st.write(' ')

col1, col2, col3, col4  = st.columns([1,1,1,1])
with col1:
    airline = st.selectbox('Airline', [None, 'AirAsia', 'Indigo', 'Vistara', 'GoFirst', 'SpiceJet', 'AirIndia'])
    airline_dict = {'AirAsia' : 0, 'Indigo' : 1, 'GoFirst' : 2, "SpiceJet" : 3, "AirIndia" : 4, "Vistara" : 5 }

with col2:
    stops =	st.selectbox('Stops', [None, '0', '1', '2 or more'])
    stops_dict = {'0' : 0, '1' : 1, '2 or more' : 2}

with col3:
    Class = st.selectbox('Class', [None, 'Economy', 'Business'])
    Class_dict = {'Economy' : 0, 'Business' : 1}

with col4:
    Departure_date = st.date_input('Select Date', min_value = datetime.today(), max_value = datetime.today() + timedelta(50) )	
    Date_diff = datetime.strptime(str(Departure_date), '%Y-%m-%d') - datetime.today()
    Date_diff = int(Date_diff.days + 1)

st.write(' ')
st.write(' ')
st.write(' ')


col1, col2  = st.columns([1,1])
with col1:
    source_city = st.selectbox('Source City', [None, 'Delhi', 'Hyderabad', 'Bangalore', 'Mumbai', 'Kolkata', 'Chennai'])
    source_city_dict = {'Delhi' : 0, 'Hyderabad' : 1, 'Bangalore' : 2, "Mumbai" : 3, "Kolkata" : 4, "Chennai" : 5 }

with col2:
    departure_time = st.selectbox('Departure Time', [None, 'Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late Night'])
    departure_time_dict = {'Early Morning' : 0, 'Morning' : 1, 'Afternoon' : 2, "Evening" : 3, "Night" : 4, "Late Night" : 5 }


col1, col2  = st.columns([1,1])
with col1:
    arrival_time = st.selectbox('Arrival Time', [None, 'Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late Night'])
    arrival_time_dict = {'Early Morning' : 0, 'Morning' : 1, 'Afternoon' : 2, "Evening" : 3, "Night" : 4, "Late Night" : 5 }

with col2:
    destination_city = st.selectbox('Destination City', [None, 'Delhi', 'Hyderabad', 'Bangalore', 'Mumbai', 'Kolkata', 'Chennai'])
    destination_city_dict = {'Delhi' : 0, 'Hyderabad' : 1, 'Mumbai' : 2, "Bangalore" : 3, "Chennai" : 4, "Kolkata" : 5 }

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
col1, col2, col3 = st.columns([1,1,1])
with col1:
    pass

with col2:
    data = [airline, source_city, departure_time, stops, arrival_time, destination_city, Class, Date_diff]
    if None not in data and st.button('Predict Price'):
        features = [airline_dict[airline], source_city_dict[source_city], departure_time_dict[departure_time], stops_dict[stops], arrival_time_dict[arrival_time], destination_city_dict[destination_city], Class_dict[Class], Date_diff]

        model = pickle.load(open('linear_model.pkl', 'rb'))
        predict = model.predict([features])[0]
        st.subheader(f':violet[Flight Price is Rs.  {predict.round(2)}]')

with col3:
    pass
    