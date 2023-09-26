# Import necessary libraries
import streamlit as st
import pandas as pd

# Define a function to load data
@st.cache_resource()
def load_data(relative_path):
    data = pd.read_csv(r"data\split_1.csv") 
    return data

# Set the relative path to the csv and load data with function
rel_path = r"data\split_1.csv"
loaded_df = load_data(rel_path)

# Set up the Streamlit sidebar for navigation
st.sidebar.header('Navigation')
menu = ['Home', 'About the App']
choice = st.sidebar.selectbox("Select an option", menu)

# Set the title for the app
st.title("Store sales prediction")

# Create a container for the header section
header = st.container()
header.write("This app predicts the total sales of items sold at different stores")

# Create a container for previewing the dataset
dataset = st.container()
with dataset:
    if dataset.button("Preview the Dataset"):
        dataset.write(loaded_df)

# Create a form for user inputs
# form = st.form(key='Information', clear_on_submit=True)

# Create a container for user inputs and predictions
predictions = st.container()
with predictions:
    predictions.subheader("Inputs")
    predictions.write("This section will take all your inputs")

    # Define columns for user input fields
    col1, col2 = predictions.columns(2)

    Store_type = ["A", "B", "C", "D", "E"]
    clusters = ["1", "2", "3", "4", "5","6", "7", "8", "9", "10", "11","12", "13", "14", "15", "15","17"]
    categories = ['AUTOMOTIVE', 'BEAUTY AND FASHION', 'BEVERAGES AND LIQUOR',
       'SCHOOL AND OFFICE SUPPLIES', 'GROCERY', 'HOME CARE AND GARDEN',
       'FROZEN FOODS', 'HOME AND KITCHEN', 'PET SUPPLIES']
    events = ['1', '0']

    # Section 1: User inputs for date and store-related information
    with col1:
        col1.write('Section 1')
        start_date = st.date_input("Start Date")
        start_date = pd.to_datetime(start_date)
        end_date = st.date_input("End Date")
        end_date = pd.to_datetime(end_date)
        onpromotion = st.number_input("How many products are on promotion?", min_value=0, step=1)
        store_nbr = st.number_input("What is the store number", min_value=0, max_value=25)

    # Section 2: User inputs for event and product-related information
    with col2:
        col2.write('Section 2')
        events = st.selectbox("Is it a holiday? (1)Yes or (0)No", events)
        selected_category = st.selectbox("Product_Category", categories)
        selected_store = st.selectbox("Store_type", Store_type)
        selected_cluster = st.selectbox("Cluster", clusters)

    # Create an empty DataFrame for predicted data
    predicted_data = pd.DataFrame(columns=['Start Date', 'End Date', 'Store', 'Category', 'On Promotion', 'City', 'Cluster', 'Predicted Sales'])

