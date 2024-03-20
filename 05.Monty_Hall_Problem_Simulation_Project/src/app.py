import streamlit as st
from src.MontyHall import Monty_Hall
import time

st.title(":zap: Monty Hall Simulation")

st.image("https://qph.cf2.quoracdn.net/main-qimg-7bc6bc567a79d8976796805553659f20.webp")

num_games = st.number_input(
    "Enter number of games to be simulated", 
    min_value=1, max_value=100000, value=100
    )

col1, col2 = st.columns(2)
col1.subheader('Win Percentage without Switching')
col2.subheader('Win Percentage with Switching')

chart1 = col1.line_chart(height=400)
chart2 = col2.line_chart(height = 400)

win_no_switch = 0
win_switch = 0
for num in range(1,num_games):
    if Monty_Hall(True):
        win_switch  += 1
    
    if Monty_Hall(False):
        win_no_switch += 1
    
    chart1.add_rows([win_no_switch/(num+1)*100])
    chart2.add_rows([win_switch/(num+1)*100])

    time.sleep(0.01)