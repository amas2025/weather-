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

# Hardcoded access code
ACCESS_CODE = "iloveamas"

# Function for access code validation
def validate_access():
    """Validate access code before allowing access to the app."""
    st.title("📚 E-Library - Access Required")
    access_code = st.text_input("Enter Access Code", type="password", key="access_code_input")
    
    if st.button("Access", key="access_button"):
        if access_code == ACCESS_CODE:
            st.session_state["has_access"] = True
            st.success("Access granted! Welcome to the E-Library.")
            st.experimental_rerun()
        else:
            st.error("Invalid access code. Please try again.")

# Main app function
def main():
    # Initialize session state for access
    if "has_access" not in st.session_state:
        st.session_state["has_access"] = False

    # Check if the user has access
    if not st.session_state["has_access"]:
        validate_access()
        return

    # Main application after access validation
    st.title("📚 E-Library")
    st.sidebar.title("📖 Navigation")

    menu = ["🏠 Home", "📂 Browse E-Books", "📤 Upload E-Books", "🔍 Search"]
    choice = st.sidebar.radio("Select a Page", menu)

    if choice == "🏠 Home":
        st.image("https://via.placeholder.com/1200x300?text=Welcome+to+E-Library", use_column_width=True)
        st.markdown("## Welcome to the E-Library 📚\nDiscover, upload, and read e-books online.")

    elif choice == "📂 Browse E-Books":
        st.subheader("Browse E-Books by Category")
        category = st.selectbox("Select a Category", ["Chemistry", "Engineering", "Computer Science", "Physics", "Medical"])
        books = list_ebooks("uploaded_ebooks", category)
        if books:
            display_ebooks_online(books)
        else:
            st.info(f"No e-books available in {category}. Upload some to get started.")

    elif choice == "📤 Upload E-Books":
        st.subheader("Upload Your E-Books")
        category = st.selectbox("Select a Category for Your Book", ["Chemistry", "Engineering", "Computer Science", "Physics", "Medical"])
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
        if uploaded_file:
            upload_ebook(uploaded_file, "uploaded_ebooks", category)

    elif choice == "🔍 Search":
        st.subheader("Search for E-Books")
        query = st.text_input("Enter book title")
        category = st.selectbox("Select a Category to Search", ["All", "Chemistry", "Engineering", "Computer Science", "Physics", "Medical"])
        results = search_ebooks("uploaded_ebooks", query, category)
        if results:
            display_ebooks_online(results)
        else:
            st.warning("No results found.")

if __name__ == "__main__":
    main()
