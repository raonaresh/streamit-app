import streamlit as st

num1 = st.number_input('Enter number1')

num2 = st.number_input('Enter number2')

num3 = st.number_input('Enter nnumber3')

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
st.write('The largest number is ', largest)