import streamlit as st
import os
import base64

# Directory to store uploaded e-books
UPLOAD_DIR = "uploaded_ebooks"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Function to display e-books
def display_ebooks(books):
    for book in books:
        st.write(f"### {book['title']}")
        st.write(f"Author: {book.get('author', 'Unknown')}")
        with open(book['file'], "rb") as file:
            base64_pdf = base64.b64encode(file.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

# Streamlit app
def main():
    st.title("E-Library")
    st.sidebar.title("Navigation")

    menu = ["Home", "Browse E-Books", "Upload E-Books", "Search"]
    choice = st.sidebar.radio("Menu", menu)

    # Placeholder for uploaded e-books
    e_books = []

    if choice == "Home":
        st.subheader("Welcome to the E-Library")
        st.write("Browse, upload, and read e-books conveniently.")

    elif choice == "Browse E-Books":
        st.subheader("Available E-Books")
        all_books = [
            {"title": file, "file": os.path.join(UPLOAD_DIR, file)}
            for file in os.listdir(UPLOAD_DIR) if file.endswith('.pdf')
        ]
        if all_books:
            display_ebooks(all_books)
        else:
            st.write("No e-books available. Upload some to get started.")

    elif choice == "Upload E-Books":
        st.subheader("Upload Your E-Books")
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
        if uploaded_file is not None:
            file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Uploaded {uploaded_file.name} successfully!")

    elif choice == "Search":
        st.subheader("Search for E-Books")
        search_query = st.text_input("Enter book title")
        if search_query:
            results = [
                {"title": file, "file": os.path.join(UPLOAD_DIR, file)}
                for file in os.listdir(UPLOAD_DIR)
                if search_query.lower() in file.lower()
            ]
            if results:
                display_ebooks(results)
            else:
                st.write("No results found.")

if __name__ == "__main__":
    main()
