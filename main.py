def main():
    # Load custom font
    load_custom_css()

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
    st.image("https://via.placeholder.com/1200x300?text=Welcome+to+E-Library", use_container_width=True)
    st.markdown("## Welcome to the E-Library 📚\nDiscover, upload, and read e-books online.")
    st.markdown("### بەخێربێن بۆ یەکەم ئاپی کوردی تایبەت بە کتیبی ئۆنلاین")  # Kurdish text

