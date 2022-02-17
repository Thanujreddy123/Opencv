import cv2
import streamlit as st
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.cap=cv2.VideoCapture(0)
while st.cap.isOpened():
    st.ret,st.frame=st.cap.read()
    cv2.imshow("frame",st.frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
st.cap.release()
cv2.destroyAllWindows()

