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

# Hardcoded credentials
USERNAME = "amas"
PASSWORD = "2025"

# Available categories
CATEGORIES = ["Chemistry", "Engineering", "Computer Science", "Physics", "Medical"]

# Function for user authentication
def authenticate_user():
    """Authenticate user before allowing access to the app."""
    st.title("📚 E-Library - Sign In")
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")
    
    if st.button("Sign In", key="sign_in_button"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["authenticated"] = True
            st.success("You have successfully signed in!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password. Please try again.")

# Main app function
def main():
    # Initialize session state for authentication
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    # Check if the user is authenticated
    if not st.session_state["authenticated"]:
        authenticate_user()
        return

    # Main application after authentication
    st.title("📚 E-Library")
    st.sidebar.title("📖 Navigation")

    menu = ["🏠 Home", "📂 Browse E-Books", "📤 Upload E-Books", "🔍 Search"]
    choice = st.sidebar.radio("Select a Page", menu)

    if choice == "🏠 Home":
        st.image("https://via.placeholder.com/1200x300?text=Welcome+to+E-Library", use_column_width=True)
        st.markdown("## Welcome to the E-Library 📚\nDiscover, upload, and read e-books online.")

    elif choice == "📂 Browse E-Books":
        st.subheader("Browse E-Books by Category")
        category = st.selectbox("Select a Category", CATEGORIES)
        books = list_ebooks("uploaded_ebooks", category)
        if books:
            display_ebooks_online(books)
        else:
            st.info(f"No e-books available in {category}. Upload some to get started.")

    elif choice == "📤 Upload E-Books":
        st.subheader("Upload Your E-Books")
        category = st.selectbox("Select a Category for Your Book", CATEGORIES)
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
        if uploaded_file:
            upload_ebook(uploaded_file, "uploaded_ebooks", category)

    elif choice == "🔍 Search":
        st.subheader("Search for E-Books")
        query = st.text_input("Enter book title")
        category = st.selectbox("Select a Category to Search", ["All"] + CATEGORIES)
        results = search_ebooks("uploaded_ebooks", query, category)
        if results:
            display_ebooks_online(results)
        else:
            st.warning("No results found.")

if __name__ == "__main__":
    main()
