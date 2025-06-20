import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1: Login Credentials ---
USER_CREDENTIALS = {"Amna": "123456"}

def login(username, password):
    return USER_CREDENTIALS.get(username) == password

# --- Step 2: Load CSV File ---
def load_csv(file):
    try:
        df = pd.read_csv(file)

        # Clean numeric columns
        df['Revenue (USD millions)'] = df['Revenue (USD millions)'].str.replace(',', '').astype(float)
        df['Revenue growth'] = df['Revenue growth'].str.replace('%', '').astype(float)
        df['Employees'] = df['Employees'].str.replace(',', '').astype(int)

        return df

    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None
 
    

# --- Step 3: Analyze Data ---
def analyze_data(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().sum(),
        "summary": df.describe()
    }

# --- Step 4: Plot Graphs ---
def plot_graphs(df):
    st.subheader(" Data Visualizations")

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if not numeric_cols:
        st.warning("No numeric columns to visualize.")
        return

    # --- Heatmap ---
    st.subheader(" Correlation Heatmap")
    corr = df[numeric_cols].corr()
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax1)
    st.pyplot(fig1)

    # --- Histogram ---
    st.subheader(" Histogram")
    selected_hist_col = st.selectbox("Choose column for histogram", numeric_cols, key='hist')
    if selected_hist_col:
        fig2, ax2 = plt.subplots()
        sns.histplot(df[selected_hist_col], kde=True, ax=ax2)
        ax2.set_title(f'Histogram of {selected_hist_col}')
        st.pyplot(fig2)

    # --- Scatter Plot ---
    if len(numeric_cols) >= 2:
        st.subheader(" Scatter Plot")
        col1 = st.selectbox("X-axis", numeric_cols, key='x')
        col2 = st.selectbox("Y-axis", numeric_cols, key='y')
        fig3, ax3 = plt.subplots()
        sns.scatterplot(data=df, x=col1, y=col2, ax=ax3)
        ax3.set_title(f'{col1} vs {col2}')
        st.pyplot(fig3)



# --- Step 5: Main App ---
def main():
    st.title(" Login + CSV Data Analyzer Dashboard")

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.subheader("Login")
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
        st.sidebar.success(" Logged in as Amna")
        st.header(" Upload and Analyze CSV File")

        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

        if uploaded_file is not None:
            df = load_csv(uploaded_file)

            if df is not None:
                st.subheader(" Data Preview")
                st.dataframe(df.head())

                st.subheader(" Dataset Summary")
                stats = analyze_data(df)
                st.write(f"**Rows:** {stats['rows']}")
                st.write(f"**Columns:** {stats['columns']}")
                st.write(f"**Missing Values:** {stats['missing_values']}")
                st.dataframe(stats["summary"])

                plot_graphs(df)
 

if __name__ == "__main__":
    main()

