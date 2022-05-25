import cv2
import streamlit as st


st.title("Web app")
run = st.checkbox("Run")
frame = st.image([])

cap = cv2.VideoCapture(0)

while run:
    ret, Frame = cap.read()
    Frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
    frame.image(Frame)
    
else:
    st.write("Stopped")   