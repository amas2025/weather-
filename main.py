import streamlit as st
from visualization import display_ebooks_online
from utils import list_ebooks, upload_ebook, search_ebooks

# Set page configuration
st.set_page_config(
    page_title="E-Library",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    st.title("📚 E-Library")
    st.sidebar.title("📖 Navigation")

    menu = ["🏠 Home", "📂 Browse E-Books", "📤 Upload E-Books", "🔍 Search"]
    choice = st.sidebar.radio("Select a Page", menu)

    if choice == "🏠 Home":
        st.image("https://via.placeholder.com/1200x300?text=Welcome+to+E-Library", use_column_width=True)
        st.markdown("## Welcome to the E-Library 📚\nDiscover, upload, and read e-books online.")

    elif choice == "📂 Browse E-Books":
        st.subheader("Available E-Books")
        books = list_ebooks("uploaded_ebooks")
        if books:
            display_ebooks_online(books)
        else:
            st.info("No e-books available. Upload some to get started.")

    elif choice == "📤 Upload E-Books":
        st.subheader("Upload Your E-Books")
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
        if uploaded_file:
            upload_ebook(uploaded_file, "uploaded_ebooks")

    elif choice == "🔍 Search":
        st.subheader("Search for E-Books")
        query = st.text_input("Enter book title")
        if query:
            results = search_ebooks("uploaded_ebooks", query)
            if results:
                display_ebooks_online(results)
            else:
                st.warning("No results found.")

if __name__ == "__main__":
    main()
