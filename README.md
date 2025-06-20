#  CSV Analyzer with Login – Streamlit App

This is a Streamlit web app that allows you to:

###  1. Secure Login
- Only authorized users can access the dashboard.
- Username and password are checked before allowing access.

---

###  2. Upload & Clean CSV File
- Upload any `.csv` file.
- Automatically cleans:
  - Commas in numbers (e.g., 1,000 → 1000)
  - Percent signs in growth rates (e.g., 6.5% → 6.5)
  - Converts string-based numbers into numeric format

---

###  3. Analyze the Data
- Shows top rows of the dataset
- Gives total rows, columns, and missing values
- Displays summary statistics like mean, std, min, max

---

###  4. Visualize the Data
- **Correlation Heatmap**: relationships between numeric columns
- **Histogram**: choose any numeric column to view its distribution
- **Scatter Plot**: pick any two numeric columns to see patterns

---

 
