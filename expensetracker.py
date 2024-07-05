import streamlit as st
import pandas as pd

# Set up the page title
st.title("Expense Tracker")

# Initialize the session state to store expenses
if "expenses" not in st.session_state:
    st.session_state["expenses"] = []

# Function to add an expense
def add_expense(description, amount, date):
    expense = {"Description": description, "Amount": amount, "Date": date}
    st.session_state["expenses"].append(expense)

# Sidebar inputs for adding expenses
with st.sidebar:
    st.header("Add a new expense")
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    date = st.date_input("Date")

    if st.button("Add Expense"):
        if description and amount:
            add_expense(description, amount, date)
            st.success("Expense added successfully!")
        else:
            st.error("Please provide both description and amount")

# Displaying the expenses
if st.session_state["expenses"]:
    st.header("Expenses")
    expenses_df = pd.DataFrame(st.session_state["expenses"])
    st.dataframe(expenses_df)

    # Calculate the total amount
    total_amount = expenses_df["Amount"].sum()
    st.subheader(f"Total Amount: ${total_amount:.2f}")
else:
    st.write("No expenses added yet.")

# Run the app using 'streamlit run <filename>.py'
