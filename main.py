import streamlit as st

# Step 1: Login credentials
USER_CREDENTIALS = {
    "Amna": "123456"
}

# Step 2: Function to verify login
def login(username, password):
    return USER_CREDENTIALS.get(username) == password

# Step 3: Function to analyze the file
def analyze_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        st.subheader("File Content")
        st.text(content)
        num_lines = content.count('\n') + 1 if content else 0
        num_words = len(content.split())
        num_characters = len(content)

        with open(output_filename, 'w', encoding='utf-8') as summary_file:
            summary_file.write(f"Lines: {num_lines}\n")
            summary_file.write(f"Words: {num_words}\n")
            summary_file.write(f"Characters: {num_characters}\n")

        return num_lines, num_words, num_characters

    except FileNotFoundError:
        st.error(f"Error: The file '{input_filename}' was not found.")
        return None, None, None

# Step 4: Main app
def main():
    st.title(" Login Page + File Analyzer")

    # Initialize login state
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.subheader("Please enter your credentials")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login(username, password):
                st.session_state.authenticated = True
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password")
    else:
        # Logged in view: show file analyzer
        st.header(" Text File Analyzer")

        input_file = st.text_input("Enter input file name (e.g., data.txt)")
        output_file = st.text_input("Enter output file name (e.g., summary.txt)")

        if st.button("Analyze File"):
            if input_file and output_file:
                lines, words, characters = analyze_file(input_file, output_file)
                if lines is not None:
                    st.success(" Analysis Complete")
                    st.write(f"**Lines:** {lines}")
                    st.write(f"**Words:** {words}")
                    st.write(f"**Characters:** {characters}")
            else:
                st.warning("Please enter both input and output file names.")

if __name__ == "__main__":
    main()
