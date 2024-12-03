import streamlit as st
from utilz.llama_response import fridge_results


def app():
    ## App to upload a picture of a fridge and get back suggested ideas

    st.title("What's for (healthy) dinner?")

    st.text(
        "Take a picture of your fridge to see what you can make for dinner?")
    col1, col2 = st.columns([3, 3])

    response = ""
    with col1:
        uploaded_file = st.file_uploader("Upload a picture of your fridge")
        if uploaded_file is not None:
            response = fridge_results(uploaded_file.getvalue())

    with col2:
        st.image("./images/fullsizerender-287.jpg")
        st.text("Or use this placeholder....")
        if st.button("Generate ideas", key="123"):
            with st.spinner(f'Musing....'):
                response = fridge_results()
    st.markdown(f"<span style='word-wrap:break-word;'>{response}",
                unsafe_allow_html=True)
