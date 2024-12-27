import streamlit as st
import os
from visualization import display_ebooks_online
from utils import list_ebooks, upload_ebook, search_ebooks

# Directory to store uploaded e-books
UPLOAD_DIR = "uploaded_ebooks"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def main():
    st.title("E-Library")
    st.sidebar.title("Navigation")

    menu = ["Home", "Browse E-Books", "Upload E-Books", "Search"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to the E-Library")
        st.write("Browse, upload, and read e-books conveniently.")

    elif choice == "Browse E-Books":
        st.subheader("Available E-Books")
        all_books = list_ebooks(UPLOAD_DIR)
        if all_books:
            display_ebooks_online(all_books)
        else:
            st.write("No e-books available. Upload some to get started.")

    elif choice == "Upload E-Books":
        st.subheader("Upload Your E-Books")
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
        if uploaded_file is not None:
            upload_ebook(uploaded_file, UPLOAD_DIR)

    elif choice == "Search":
        st.subheader("Search for E-Books")
        search_query = st.text_input("Enter book title")
        if search_query:
            results = search_ebooks(UPLOAD_DIR, search_query)
            if results:
                display_ebooks_online(results)
            else:
                st.write("No results found.")

if __name__ == "__main__":
    main()
