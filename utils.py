import os
import streamlit as st

def list_ebooks(upload_dir):
    return [
        {"title": file, "file": os.path.join(upload_dir, file)}
        for file in os.listdir(upload_dir) if file.endswith('.pdf')
    ]

def upload_ebook(uploaded_file, upload_dir):
    file_path = os.path.join(upload_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded {uploaded_file.name} successfully!")

def search_ebooks(upload_dir, query):
    return [
        {"title": file, "file": os.path.join(upload_dir, file)}
        for file in os.listdir(upload_dir)
        if query.lower() in file.lower()
    ]
