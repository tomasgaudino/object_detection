import streamlit as st
import labelme

from utils.os_utils import launch_labelme

st.set_page_config(page_title="Object Detection App", page_icon="🧊", layout="wide", initial_sidebar_state="expanded")

st.title("Object Detection App")
st.subheader("Labeling images")
st.markdown("This app launches LabelMe in your browser. LabelMe is a free, open source tool for annotating images. ")
if st.button("Open LabelMe"):
    state = launch_labelme()
    if state == "success":
        st.success("LabelMe launched successfully!")
    else:
        st.error(state)
