import streamlit as st
import os
import base64

# Sample data: List of e-books
e_books = [
    {"title": "E-Book 1", "author": "Author A", "file": "ebooks/ebook1.pdf"},
    {"title": "E-Book 2", "author": "Author B", "file": "ebooks/ebook2.pdf"},
    {"title": "E-Book 3", "author": "Author C", "file": "ebooks/ebook3.pdf"},
]

# Function to display e-books
def display_ebooks(books):
    for book in books:
        st.write(f"### {book['title']}")
        st.write(f"Author: {book['author']}")
        with open(book['file'], "rb") as file:
            base64_pdf = base64.b64encode(file.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

# Streamlit app
def main():
    st.title("E-Library")
    st.sidebar.title("Navigation")

    menu = ["Home", "Browse E-Books", "Search"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to the E-Library")
        st.write("Browse and read e-books conveniently.")

    elif choice == "Browse E-Books":
        st.subheader("Available E-Books")
        display_ebooks(e_books)

    elif choice == "Search":
        st.subheader("Search for E-Books")
        search_query = st.text_input("Enter book title or author")
        if search_query:
            results = [
                book for book in e_books
                if search_query.lower() in book["title"].lower()
                or search_query.lower() in book["author"].lower()
            ]
            if results:
                display_ebooks(results)
            else:
                st.write("No results found.")

if __name__ == "__main__":
    # Ensure the e-books folder exists and contains sample files
    os.makedirs("ebooks", exist_ok=True)
    for idx, book in enumerate(e_books, start=1):
        file_path = book['file']
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(f"Sample content for {book['title']}")
    
    main()
