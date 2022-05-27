# import cv2
# import streamlit as st
# import time


from streamlit_webrtc import webrtc_streamer
# st.title("Web app")

webrtc_streamer(key="sample")


# run = st.checkbox("Run")
# frame = st.image([])

# cap = cv2.VideoCapture(0)

# while run:
#     ret, Frame = cap.read()
#     time.sleep(5)
#     st.write("Wait ends")
#     Frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
#     frame.image(Frame)
    
# else:
#     st.write("Stopped")   
