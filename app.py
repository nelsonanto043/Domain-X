from turtle import color
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
    st.balloons()
    st.snow()
    

import streamlit as st

st.markdown(
    """
    <style>
    /* Full app background */
    .stApp {
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #0f2027, #203a43);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: white;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Text color fix */
    h1, h2, h3, p, span {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)




               



