import streamlit as st
import base64
import os

def display_ebooks_online(books):
    for book in books:
        st.markdown(f"### {book['title']}")
        with open(book['file'], "rb") as file:
            base64_pdf = base64.b64encode(file.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        # Add a download button for each book
        st.download_button(
            label="Download",
            data=open(book['file'], "rb").read(),
            file_name=book["title"],
            mime="application/pdf",
        )
        st.markdown("---")
