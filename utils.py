import os
import streamlit as st

def list_ebooks(upload_dir, category):
    """List all uploaded e-books by category."""
    category_dir = os.path.join(upload_dir, category)
    if not os.path.exists(category_dir):
        return []
    return [
        {"title": file, "file": os.path.join(category_dir, file)}
        for file in os.listdir(category_dir) if file.endswith('.pdf')
    ]

def upload_ebook(uploaded_file, upload_dir, category):
    """Handle file upload for e-books with category."""
    category_dir = os.path.join(upload_dir, category)
    os.makedirs(category_dir, exist_ok=True)
    file_path = os.path.join(category_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded {uploaded_file.name} successfully to {category} category!")

def search_ebooks(upload_dir, query, category):
    """Search for e-books by title and category."""
    if category == "All":
        results = []
        for cat in os.listdir(upload_dir):
            cat_dir = os.path.join(upload_dir, cat)
            if os.path.isdir(cat_dir):
                results.extend([
                    {"title": file, "file": os.path.join(cat_dir, file)}
                    for file in os.listdir(cat_dir) if query.lower() in file.lower()
                ])
        return results
    else:
        return list_ebooks(upload_dir, category)
