
import streamlit as st

try:
    st.title ("My NEW HABITS APP")
    st.write ("Track your habits and improve your life!")
    st.write ("This is a simple app to help you monitor and build new habits over time.")
    st.write ("Stay consistent and see your progress!")
    st.write ("Add your habits below and check them off as you complete them each day.")
    habit = st.text_input("Enter a new habit:")
    if st.button("Add Habit"):
        st.write(f"Habit '{habit}' added!")
    time = st.time_input("Enter time for habit") 
    if st.button("Add time"):
        st.write(f"Time '{time}' added!") 
    st.camera_input("一二三,茄子!")
    if st.button("Click me!"):
        st.write("Photo captured!")
    st.button("submit")
    def on_click():
      st.write("Habit submitted!")
    on_click()
    st.header ("   -----MAKES A NEW CHAPTER OF LIFE !-----")
except ValueError as e:
    st.error("enter valid input")
    
    

