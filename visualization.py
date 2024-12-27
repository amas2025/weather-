import streamlit as st
import base64
import os

def display_ebooks_online(books):
    for idx, book in enumerate(books):
        st.markdown(f"### {book['title']}")
        with open(book['file'], "rb") as file:
            base64_pdf = base64.b64encode(file.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500"></iframe>'

        # Add download button
        st.download_button(
            label="Download",
            data=open(book['file'], "rb").read(),
            file_name=os.path.basename(book['file']),
            mime="application/pdf",
        )

        # Add "Read Online" button below the download button
        if st.button(f"Read Online", key=f"read_online_{idx}"):
            st.markdown(pdf_display, unsafe_allow_html=True)

        # Add a horizontal divider between books
        st.markdown("---")
